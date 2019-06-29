#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:21:02 2019

@author: Nicoleta Cristea cristn@uw.edu 
"""
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd

# <codecell>
path = '/Users/carina/Desktop/code/SkagitLandslideHazards/'
values = np.loadtxt(path + "Map.Soil.TableDepth.asc.txt")
#wd = pd.DataFrame(data=values[1:,1:],    # values
#             index=data[1:,0],    # 1st column as index
#             columns=data[0,1:])  # 1st row as the column names 
# <codecell>
# concatenate data into xarray 
no_days = values.shape[0]/1020
one_image = values[:1020]
second_image = values[1020:2040]

fig = plt.figure(figsize=(6, 3.2))

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
list_arrays = np.vsplit(values, no_days)
#all_arrays = np.vstack(list_arrays)
all_arrays =  np.asarray(list_arrays)

# <codecell>
# define an xarray dataset 
#ds_wt = xr.Dataset({'dt_wt': (all_arrays)})
years = np.linspace(1, 62, num = 62)
x = np.linspace(1, 916, num = 916)
y = np.linspace(1, 1020, num = 1020)

#create tuples 
xx = (x, x)
yy = (y, y)


# <codecell>
ds_wt = xr.Dataset({'dt_wt': (['time','y','x'], all_arrays)})
ds_wt['time'] = years 

ds_wt['y'] = y
ds_wt['x'] = x

#ds_wt = ds_wt.set_coords(['time','y', 'x'])

# 
# <codecell> how to define an xrray dataset 


# ds = xr.Dataset({'temperature': (['x', 'y', 'time'],  temp),
#   ....:                  'precipitation': (['x', 'y', 'time'], precip)},
#   ....:                 coords={'lon': (['x', 'y'], lon),
#   ....:                         'lat': (['x', 'y'], lat),
#   ....:                         'time': pd.date_range('2014-09-06', periods=3),
#   ....:                         'reference_time': pd.Timestamp('2014-09-05')})

 