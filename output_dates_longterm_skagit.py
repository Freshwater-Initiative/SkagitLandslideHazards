#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:18:30 2018
Updated May 4, 2019

@author: Nicoleta Cristea (cristn@uw.edu)
"""
#Use DHSVM saturation extent output to identify dates witn maximum saturated area in each water year
# export dates in DHSVM config format for outputting maps of saturation in
# subsequent runs as in example below:  
#Map Date 1 1 = 08/01/1987-00 # output for this variable
#Map Date 2 1 = 08/01/1988-00 # Vary the first number from
#Map Date 3 1 = 08/01/1989-00
#Map Date 4 1 = 08/01/1990-00

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr
import time

# <codecell>
#load files, place data in pandas dataframes
sat_his = pd.read_csv('/Users/carina/Desktop/code/SkagitLandslideHazards/saturation_methods/skagit_extent/output_SCLlandslide_historic/saturation_extent.txt', sep='\s+', header=None, names=["time", "sat_value"])
sat_CNRM_CM5_rcp85 = pd.read_csv('/Users/carina/Desktop/code/SkagitLandslideHazards/saturation_methods/skagit_extent/output_SCLlandslide_bclivlow_G_CNRM-CM5__rcp85/saturation_extent.txt', sep='\s+', header=None, names=["time", "sat_value"])
sat_CNRM_CM5_rcp45 = pd.read_csv('/Users/carina/Desktop/code/SkagitLandslideHazards/saturation_methods/skagit_extent/output_SCLlandslide_bclivlow_G_CNRM-CM5__rcp45/saturation_extent.txt', sep='\s+', header=None, names=["time", "sat_value"])
sat_HadGEM2_ES365_rcp85 = pd.read_csv('/Users/carina/Desktop/code/SkagitLandslideHazards/saturation_methods/skagit_extent/output_SCLlandslide_bclivlow_G_NorESM1_M__rcp45/saturation_extent.txt', sep='\s+', header=None, names=["time", "sat_value"])
sat_HadGEM2_ES365_rcp45 = pd.read_csv('/Users/carina/Desktop/code/SkagitLandslideHazards/saturation_methods/skagit_extent/output_SCLlandslide_bclivlow_G_HadGEM2-ES365__rcp45/saturation_extent.txt', sep='\s+', header=None, names=["time", "sat_value"])
sat_NorESM1_M_rcp85 = pd.read_csv('/Users/carina/Desktop/code/SkagitLandslideHazards/saturation_methods/skagit_extent/output_SCLlandslide_bclivlow_G_NorESM1_M__rcp85/saturation_extent.txt', sep='\s+', header=None, names=["time", "sat_value"])
sat_NorESM1_M_rcp45 = pd.read_csv('/Users/carina/Desktop/code/SkagitLandslideHazards/saturation_methods/skagit_extent/output_SCLlandslide_bclivlow_G_NorESM1_M__rcp45/saturation_extent.txt', sep='\s+', header=None, names=["time", "sat_value"])

# <codecell>
def calc_water_year(date):
    date = pd.to_datetime(date)
    if 10 <= date.month <= 12:
        return date.year + 1
    else:
        return date.year
        
def calc_water_year_apply(df):
    df['water_year'] = df.datetime.apply(lambda row: calc_water_year(row))  

# <codecell>
def list_dates(sat_dataframe):
#    sat_dataframe = data1
    sat_dataframe.time = sat_dataframe.time.apply(pd.to_datetime, dayfirst=False, yearfirst=False)
    sat_dataframe.index = sat_dataframe['time']
    del sat_dataframe['time']
    sat_dataframe['doy']= sat_dataframe.index.dayofyear
    sat_dataframe['cal_year'] = sat_dataframe.index.year
    sat_dataframe['month'] = sat_dataframe.index.month
    sat_dataframe['datetime'] = sat_dataframe.index
    #calc_water_year_apply(sat_dataframe)['datetime']
    calc_water_year_apply(sat_dataframe)
    grouped = sat_dataframe.groupby('water_year')
    out_all = []
    for name,group in grouped:
         a = group.sort_values(by=['sat_value'], ascending=False)
         out = a.iloc[0]
         out_all.append(out.datetime)
    return out_all
# <codecell>
#list_dates_test = list_dates(sat_his)

# <codecell>
def make_list_dates_output(list_dates):
    list_ = []    
    for index in range(len(list_dates)):
        date_test = list_dates[index]
        date_string = "Map date {} 1= {}".format(index + 1, date_test.to_pydatetime().strftime("%m/%d/%Y-%H"))
    #    print("Map date {} {}".format(index + 1, date_test.to_pydatetime().strftime("%m/%d/%Y-%H")))
        list_.append(date_string)
    return list_    
  
# <codecell>
#test for function
#export in text file - historic
temp = list_dates(sat_his)
list_ = make_list_dates_output(temp)    
with open('export_historic_dates', 'w') as f:
    for item in list_:
        f.write("%s\n" % item)
# <codecell>
#find dattes for climate runs      
temp_1 = list_dates(sat_CNRM_CM5_rcp85)
list_1= make_list_dates_output(temp_1)    
with open('export_dates_sat_CNRM_CM5_rcp85', 'w') as f:
    for item in list_1:
        f.write("%s\n" % item)
# <codecell>
#find dattes for climate runs      
temp_2 = list_dates(sat_CNRM_CM5_rcp45)
list_2= make_list_dates_output(temp_2)    
with open('export_dates_sat_CNRM_CM5_rcp45', 'w') as f:
    for item in list_2:
        f.write("%s\n" % item)
# <codecell>
#find dattes for climate runs      
temp_3 = list_dates(sat_HadGEM2_ES365_rcp85)
list_3= make_list_dates_output(temp_3)    
with open('export_dates_sat_HadGEM2_ES365_rcp85', 'w') as f:
    for item in list_3:
        f.write("%s\n" % item)

# <codecell>
#find dattes for climate runs      
temp_4 = list_dates(sat_HadGEM2_ES365_rcp45)
list_4= make_list_dates_output(temp_4)    
with open('export_dates_sat_HadGEM2_ES365_rcp45', 'w') as f:
    for item in list_4:
        f.write("%s\n" % item)
# <codecell>
#find dattes for climate runs      
temp_5 = list_dates(sat_NorESM1_M_rcp85)
list_5= make_list_dates_output(temp_5)    
with open('export_dates_sat_NorESM1_M_rcp85', 'w') as f:
    for item in list_5:
        f.write("%s\n" % item)
# <codecell>
#find dattes for climate runs      
temp_6 = list_dates(sat_NorESM1_M_rcp45)
list_6 = make_list_dates_output(temp_6)    
with open('export_dates_sat_NorESM1_M_rcp45', 'w') as f:
    for item in list_6:
        f.write("%s\n" % item)






