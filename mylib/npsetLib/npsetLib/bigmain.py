if __name__ == '__main__':
    # If not using daymet swe, then add accumswe to output_params list. Otherwise, same output can be obtained from daymet source files.
    #multiprocessing.log_to_stderr(logging.INFO)
    melt_factor = 4.0
    precip_fraction = 0.167
    web = True
    start_time = time.time()  
    PET_type = 'oudin'
    agdd_base = 10 # Degrees C
    end_times = []
    result_list = []
    first_year = 1980
    last_year = 2017
    if web == False:
        years = [1980,1981,1982,1983]
        input_data_path =  '/media/mt/0CED00122A266FA8/daymet_wb/'
        output_data_path = '/media/mt/0CED00122A266FA8/daymet_wb/'
        npz_cores  = 4
        collate_cores = 5
        first_day = 0
        last_day = 5
    else:
        years = list(range(first_year,last_year+1))
        input_data_path =  '/home/wbdata/'
        output_data_path = '/home/results/'
        npz_cores  = 8
        collate_cores = 8 # This can be raised once the model loops finish.
        first_day = 0
        last_day = 365
    year_list = [str(x) for x in years]
    years_done = []
    pool = 'null'
    leapyears = leapyearlist()       
    output_params = ['PET','AET','Deficit','rain','runoff','agdd','soil_water','accumswe']
    output_units = {'PET':'mm','AET':'mm','Deficit':'mm','accumswe':'mm','melt':'mm','days_snow':'mm','rain':'mm','water_input_to_soil':'mm','runoff':'mm','agdd':'C','accum_precip':'mm'}       
    accum_precip = np.zeros((8075,7814)).astype(np.float32)
    agdd = np.zeros((8075,7814)).astype(np.float32)
    last_accumswe = np.zeros((8075,7814)).astype(np.float32)
    latitude = get_latitude_radians('1980','tmax') #Radians
    if (np.nanmax(latitude) > 1.5) or (np.nanmin(latitude) < 0.1) : raise Exception('Latitude is not in radians or wrong file has been used. Terminating.')
    #Global vars used here to save duplication in memory associated with passing to funcs
    elevation = np.load(input_data_path + 'etopo1_aligned_array.npy') # In meters
    if (np.nanmax(elevation) > 5700) or (np.nanmin(elevation) < 0): raise Exception('Do you have the wrong elevation file? Terminating.')
    heat_load = np.load(input_data_path + 'heat_load_based_on_etopo1.npy')
    soil_whc = get_soil_whc()
    soil_water = np.copy(soil_whc) # Initialize soil values at full.
    intercept_file = np.load('intercept1_from_senay.npz') # Vegetation intercept layer from Gabriel Senay et al. pers. comm.
    Igrid = intercept_file['intercept']
    snow_thresh_file = np.load('jennings_t50_coefficients.npz') # Jennings, K. et al. 2018. Spatial variation of the rain-snow temperature threshold across the northern hemisphere. Nature Communications 9: 1148. DOI: 10.1038/s41467-018-03629-7
    snow_thresh_temperatures = snow_thresh_file['t50']
    low_thresh_temperatures = snow_thresh_temperatures - 3.0 # The Jennings coefficients are T50, i.e. where precip is half snow, half rain
    high_thresh_temperatures = snow_thresh_temperatures + 3.0 # This sets up a 6 degree span, which corresponds to the 1/6 = 0.167 precip fraction.
    
    if PET_type == 'penman_montieth':
        #slope = np.load('aligned_slope_in_radians.npy') # radians needed for numpy trig functions
        #aspect = np.load('aligned_folded_aspect_in_radians.npy')
        atmospheric_pressure = calc_atmospheric_pressure() # Used to calculate gamma. 
        gamma = calc_gamma() 
    current_collate_year = 'null'    
    runoff_check = []
    pet_check = []
    deficit_check =[]
    jobs = []
    for year in year_list:        
        var_dict = {}
        if year in leapyears: leap_offset = 1
        else: leap_offset = 0
        
        for day_index in range(first_day,last_day): #365 days in every daymet year; no Feb 29
            print('Calculating: ',year, 'day = ', day_index)
            tmean,tmax,tmin = get_tmean(year,day_index)
            low_temperature_differences = tmean - low_thresh_temperatures
            if day_index == 273 + leap_offset: # October 1 is the 274th day of the year and 275th in leap years. Indexes start at 0 so subtract one = 273.
                precip = get_param_one_day(year, 'prcp',day_index)
                precip = Igrid_adjust_precip(precip)
                accum_precip = precip
                agdd = nonneg(tmean - agdd_base)
            else:
                precip = get_param_one_day(year, 'prcp',day_index)
                precip = Igrid_adjust_precip(precip)
                accum_precip = accum_precip + precip
                gdd = nonneg(tmean - agdd_base)
                agdd = agdd + gdd
                
            if day_index == 0 and year == year_list[0]: accumswe = get_param_one_day(year, 'swe', day_index) # Daymet SWE is in kg/m2 = mm of depth.
            else: accumswe = est_snow()
            if PET_type != 'oudin': daylength = get_param_one_day(year, 'dayl', day_index)/3600 # Duration of daylight period. File is in seconds but converted to hours here.
            PET = calc_todays_PET(PET_type)
            PET_adjusted = heat_load_adjust_pet()        
            #if np.nanmin(PET_adjusted < 0): raise Exception("{y} {d} Negative PET in at least one cell. Terminating Program.".format(y = year, d = day_index))
            snow_diff = accumswe - last_accumswe
            melt = onlyabsneg(snow_diff)
            daily_snow = nonneg(snow_diff)
            rain = nonneg(precip - daily_snow)
            w = rain + melt 
            
            AET,runoff = calc_aet_and_runoff_and_soilw() # Soil water is calculated in this function with reference to PET, but the NDVI correction to PET considers soil water. Here, we NDVI-adjust PET with reference to soil water from yesterday and then use the adjusted PET as an ingredient in calculating soil water for today.
            deficit = nonneg(PET_adjusted - AET)
            last_accumswe = accumswe
            
            mp_write_daily() 
            if int(year) > int(year_list[0]):
                next_collate_year = find_next_collate_year() #Will not let collation start on a new year until prev is finished.
                if year != next_collate_year: 
                    pool = launch_new_collation() 
if web == True: collate_cores = 8 # Once model loops are over, don't need the npz cores any more.        
#Finish collating remaining npz into netCDF files
cleanup_count = 0    
print('Years collated so far: ',years_done)
while (len(years_done) < len(year_list)) and (cleanup_count <= len(year_list)) :
    next_collate_year = find_next_collate_year()
    pool = launch_new_collation()
    
print('Done Launching Collations')
pool.join()
print('Results: ',current_collate_year,result_list)
#np.save('pet_check.npy',np.array(pet_check))
#np.save('runoff_check.npy',np.array(runoff_check))
#np.save('deficit_check.npy',np.array(deficit_check))
print('Done!!')
    
