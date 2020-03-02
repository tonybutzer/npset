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

    # INTERESTING STUFF TO FOLLOW Tony
