#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:21:02 2019

@author: Nicoleta Cristea cristn@uw.edu 
"""
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from scipy.io import loadmat
from xrviz.dashboard import Dashboard
import pandas as pd
import seaborn as sns
#import csv

# <codecell>
path = '/Users/carina/Desktop/data/Water_table_skagit/Map.Soil.TableDepth.asc.historic'

values = np.loadtxt(path)
# <codecell>
path_grids = '/Users/carina/Desktop/code/SkagitLandslideHazards/y_x_grids.mat'

# <codecell>
grids = loadmat(path_grids)
#wd = pd.DataFrame(data=values[1:,1:],    # values
#             index=data[1:,0],    # 1st column as index
#             columns=data[0,1:])  # 1st row as the column names 
# <codecell>
path_dates = '/Users/carina/Desktop/data/Water_table_skagit/dates_max_sat_sauk_old_files /export_historic_dates'
#dates = np.loadtxt(path_dates + "export_historic_dates",  delimiter='\t')
#in_txt = csv.reader(open((path_dates + "export_historic_dates"), "rb"), delimiter = '\t')
#list(csv.reader(open(path_dates+'export_historic_dates.txt', 'rb'), delimiter='\t'))

dates = pd.read_csv(path_dates, sep=" ", header=None)
#df = pd.read_fwf('path_dates + "export_historic_dates")
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

x_ = np.linspace(1, 916, num = 916)
y_ = np.linspace(1, 1020, num = 1020)

#test interpolation

x = grids["X_"][:1]
y = grids["Y_"][:, 1:2]

# check grids 
x = x.T
#y = y.T

fig = plt.figure(figsize=(6, 3.2))
plt.plot(x_, x)

fig = plt.figure(figsize=(6, 3.2))
plt.plot(y_, y)

x1_ = np.linspace(1, 916, num = 2725)
y1_ = np.linspace(1, 916, num = 2720)

x1 = grids["X_1"][:1]
y1 =grids["Y_1"][:, 1:2]

# check grids 
x1 = x1.T
t = y_.shape
y = y.reshape(t) 

t = x_.shape
x = x.reshape(t) 

fig = plt.figure(figsize=(6, 3.2))
plt.plot(x1_, x1)

fig = plt.figure(figsize=(6, 3.2))
plt.plot(y1_, y1)



# <codecell>

ds_wt = xr.Dataset(data_vars = {'wt': (('time', 'y', 'x'), all_arrays)})

#%% 
#ds_wt['time'] = years 
ds_wt['time'] = dates["date"].tolist()
ds_wt['y'] = y
ds_wt['x'] = x
#ds_wt = ds_wt.set_coords(['time','y', 'x'])
ds_wt.isel(time=[0]).to_array().plot() #shows upsidedown than imshow

# <codecell>


y1 = y1.reshape(y1.shape[0])
x1 = x1.reshape(x1.shape[0])

dsi = ds_wt.interp(y = y1, x = x1)


# <codecell>

#first image to numpy 
#one_image_res = dsi.isel(time=[0]).to_array().values

#plot first image 

dsi.isel(time=[0]).to_array().plot() #shows upsidedown than imshow

# <codecell>
# or, select by date/name
dsi.sel(time= '05/31/1969-00').to_array().plot()
 
# <codecell>
#dsi.to_netcdf('dtw_historic_with_dates.nc')
dsi.to_netcdf('dtw_historic_with_dates_netcdf3.nc', format = 'NETCDF3_64BIT')
# <codecell>

dashboard = Dashboard(ds_wt)
dashboard.show()
# 
#%% select points to plot tiime variation and probability distribution

one_location = ds_wt.isel(x=[600], y = [500]).to_array()

#plot one_location 

#ds_wt.isel(x=[500], y = [500]).to_array().plot() #shows upsidedown than imshow


# <codecell> how to define an xrray dataset 

sns.distplot(one_location);

sns.distplot(one_location, bins=20, kde=False, rug=True); 


# ds = xr.Dataset({'temperature': (['x', 'y', 'time'],  temp),
#   ....:                  'precipitation': (['x', 'y', 'time'], precip)},
#   ....:                 coords={'lon': (['x', 'y'], lon),
#   ....:                         'lat': (['x', 'y'], lat),
#   ....:                         'time': pd.date_range('2014-09-06', periods=3),
#   ....:                         'reference_time': pd.Timestamp('2014-09-05')})

 