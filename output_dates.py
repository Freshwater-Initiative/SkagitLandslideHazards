# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr

# <codecell>
def calc_water_year(date):
    date = pd.to_datetime(date)
    if 10 <= date.month <= 12:
        water_year = date.year + 1
        return water_year
    else:
        return date.year
        
def calc_water_year_apply(df):
    df['water_year'] = df.datetime.apply(lambda row: calc_water_year(row))        
# <codecell>
#load file
data = pd.read_csv('/Users/carina/Desktop/code/SkagitLandslideHazards/saturation_extent.txt', sep='\s+', header=
None, names=["time", "sat_value"])
data.shape
#data.head # what the data looks like

# <codecell>
 #type(data.time[2])
# time is string, convert to datetime format
data.time = data.time.apply(pd.to_datetime, dayfirst=False, yearfirst=False)
data.plot(x = 'time', y = 'sat_value')
data.head()

# <codecell>

data.index = data['time']
del data['time']
data.head()

# <codecell>

data['doy']= data.index.dayofyear
data['cal_year'] = data.index.year
data['month'] = data.index.month
data['datetime'] = data.index
data.head()

# <codecell>

calc_water_year_apply(data)
data.head()
# <codecell>
grouped = data.groupby('water_year')

out_all = []
for name,group in grouped:
    #a = group.groupby(['sat_value']).max()
    a =group.sort_values(by=['sat_value'], ascending=False)
    out = a.iloc[0]
    out_all.append(out.datetime)
out_all
# <codecell>
temp = group
tem = temp.sort_values(by=['sat_value'], ascending=False)


