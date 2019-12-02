#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:21:02 2019

@author: Nicoleta Cristea cristn@uw.edu 
"""
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
#from scipy.io import loadmat
from xrviz.dashboard import Dashboard
import pandas as pd
import seaborn as sns
import pickle
#import csv

# <codecell>
path = '/Users/carina/Desktop/data/Water_table_skagit/Map.Soil.TableDepth.asc.historic'

values = np.loadtxt(path)
# <codecell>
path_grids = '/Users/carina/Desktop/code/SkagitLandslideHazards/grids.pkl'

# <codecell>
#grids = loadmat(path_grids)

with open(path_grids, 'rb') as f:
    grids = pickle.load(f)
    
# <codecell>
path_dates = '/Users/carina/Desktop/data/Water_table_skagit/dates_max_sat_sauk_old_files /export_historic_dates'

dates = pd.read_csv(path_dates, sep=" ", header=None)

dates.columns = ["Map", "txt", "number", "date"] #this works with the new format
#dates.columns = ["Index","Map", "txt", "number", "date"] #this works with the new format
dates['date']

# <codecell>
# concatenate data into xarray 
no_time = values.shape[0]/1020
one_image = values[:1020]
second_image = values[1020:2040]

fig = plt.figure(figsize=(6, 3.2))

#plot one image to check 

ax = fig.add_subplot(111)
ax.set_title('colorMap')
plt.imshow(one_image)
ax.set_aspect('equal')

cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(orientation='vertical')
plt.show()
# <codecell>
list_arrays = np.vsplit(values, no_time)
#all_arrays = np.vstack(list_arrays)
all_arrays =  np.asarray(list_arrays)



# <codecell>
#get sizes and reshape arrays to match dimensions and sizes 
#plot to check results

num = dates['date'].size

years = np.linspace(1, no_time, num)

#get x index for plotting and reshaping 
x_ = np.linspace(1, 916, num = 916)
y_ = np.linspace(1, 1020, num = 1020)

#test coordinates for interpolation 
# X_ and Y_ are coordinates for the coarser grid 

x = grids["X_"][:1]
y = grids["Y_"][:, 1:2]

# <codecell>
# check grids 
x = x.T
y = y.reshape(y.shape[0])
x = x.reshape(x.shape[0])

# <codecell>
# check grids 
fig = plt.figure(figsize=(6, 3.2))
plt.plot(x_, x)
# <codecell>

fig = plt.figure(figsize=(6, 3.2))
plt.plot(y_, y)

# <codecell>
#get x index for plotting and reshaping 

x1_ = np.linspace(1, 916, num = 2725)
y1_ = np.linspace(1, 916, num = 2720)

#get higher res x1 and y1 

x1 = grids["X_1"][:1]
y1 =grids["Y_1"][:, 1:2]

# <codecell>
# check higher res grids 
x1 = x1.T

# <codecell>


y1 = y1.reshape(y1.shape[0])
x1 = x1.reshape(x1.shape[0])

# <codecell>
fig = plt.figure(figsize=(6, 3.2))
plt.plot(x1_, x1)

fig = plt.figure(figsize=(6, 3.2))
plt.plot(y1_, y1)



# <codecell>

ds_wt = xr.Dataset(data_vars = {'wt': (('time', 'y', 'x'), all_arrays)})

#%% 
#ds_wt['time'] = years 
#assign coordinates

ds_wt['time'] = dates["date"].tolist()
ds_wt['y'] = y
ds_wt['x'] = x
#ds_wt = ds_wt.set_coords(['time','y', 'x'])
ds_wt.isel(time=[0]).to_array().plot() #shows upsidedown than imshow

# <codecell>
#get the numpy for imshow plotting
a = ds_wt.isel(time=[0]).to_array()
b = a[0,0].values
plt.imshow(b)

# <codecell>

# interpolate to get higher res grids


dsi = ds_wt.interp(y = y1, x = x1)


# <codecell>

#first image to numpy 
#one_image_res = dsi.isel(time=[0]).to_array().values

#plot first image, select by index

dsi.isel(time=[0]).to_array().plot() 

# <codecell>
# or, select by date/name
dsi.sel(time= '05/31/1969-00').to_array().plot()
 
# <codecell>
#save file 
#dsi.to_netcdf('dtw_historic_with_dates.nc')

#dsi.to_netcdf('dtw_historic_with_dates_netcdf3.nc', format = 'NETCDF3_64BIT')
# <codecell>

dashboard = Dashboard(ds_wt)
dashboard.show()
# 
#%% select points to plot tiime variation and probability distribution

one_location = ds_wt.isel(x=[600], y = [500]).to_array()

#plot one_location 

#ds_wt.isel(x=[500], y = [500]).to_array().plot() 


# <codecell> how to define an xrray dataset 

sns.distplot(one_location);

sns.distplot(one_location, bins=20, kde=False, rug=True); 

 