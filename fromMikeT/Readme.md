
Hi All,

Here are a few things that you mentioned being interested in during the call.

 

-- gcm_getter.py  --> this will move the maca data to your amazon ec2 instance. The version that you have will get CSIRO-mk3-6-0, but you can swap that out for the names of other GCMS.

 

-- rcp_splitter.py -- simple script that copies the different rcps into separate directories. Run this in the directory that has the *.nc from the script above

 

-- param_splitter.py  -- run this in the folder containing the separated rcp data

 

--sort_ren.py --> run this in the folders containing the separated *.nc files for each parameter. It renames the files so that the output of the reprojection and resampling steps below are easier to sort through.

 

--maca_processor_v3.py -- > This will take the maca netcdf files and make tifs that have the same resolution, projection, extent, as daymet. I did all this so that my historical and gcm output datasets line up, and so that I can use the same DEM, soil layer etc.

 

I imagine you will want to adjust all this and probably use some other projection, resolution, but at least the steps worked for me.

 

A few  notes to make the last script run properly:

 

-- I use anaconda (from the community AMI containing anaconda preinstalled on ubuntu 16.04). This runs well on an M5a.xlarge.  On the command line write:

 

```
conda create -n py355 python=3.5.5.

source activate py355

conda install -c conda-forge nco

conda install gdal
```

 

but *do not*  run sudo apt install gdal-bin or sudo apt install netcdf-bin. Interestingly you can run these apt command both in the base environment and in the py355 environment with exciting results that don't work in different ways.

 

As I mentioned on the phone, using the native ubuntu C libraries or using different versions of python will sometimes bring in different versions of gdal and the nco tools like ncks and nccopy. There are several ways for that to go wrong. In the most obvious case it will create an "environment that has conflicts' and runs very slow. In the worst case it will appear to run fine without throwing any errors but produce garbage data. I wish I had a better explanation as to why these things happen or which actual versions were bad. My approach was just to spin up a bunch of machines and try every possible combination of installations that I could think of until I got results that were ok. By ok, I mean comparing the original maca data to the reprojected output and making sure that it looked way it should on a day to day basis. It's is fairly obvious when you have a problem. Either the data will contain huge holes of no data or have, .e.g. no precip in places that had rainstorms that day. Then I wrote this information down and have never changed it. I'm sure there is a better way but that's what I came up with. I'd be curious to see any improvements that you find.

 

Our results (historical and the GCM runs that are complete so far) are available on a THREDDS that I set up (with Docker by the way) here:

 

http://www.yellowstone.solutions/thredds/catalog.html

 

This would let you subset our results  to particular regions or times and compare them to your outputs. Maybe that would help at some point. I have this server running on a slow instance, so if you plan to do a lot of work with it, please let me know. I can boost it up to something more powerful.

 

It was fun to talk to you and I'm looking forward to more collaboration. Feel free to write with any questions. I'll do the same!

Mike

 

