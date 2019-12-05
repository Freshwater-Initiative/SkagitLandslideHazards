import os
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import itertools

def ronda(path_dtw,path_dates,DHSVM_cols,nc3out,nc4out,HSDout):

    #long file of repeating dates 
    values = np.loadtxt(path_dtw)
    print("Processing")
    print(path_dtw)
    print("with dates from")
    print(path_dates)
    
    path_grids='grids.pkl'
    with open(path_grids, 'rb') as f:
        grids = pickle.load(f)
    
    #model dates selected for printing in DHSVM
    dates = pd.read_csv(path_dates, sep=" ", header=None) #dates need to be converted from string to dates
    dates.columns = ["Map", "txt", "number", "date"] 
    
    #read in the data
    DHSVMgrid = values.shape[0]/DHSVM_cols
    list_arrays = np.vsplit(values, DHSVMgrid)
    all_arrays =  np.asarray(list_arrays)
    
    #build DHSVM  resolution array
    num = dates['date'].size
    years = np.linspace(1, DHSVM_cols, num)
    x_ = np.linspace(1, 916, num = 916)
    y_ = np.linspace(1, 1020, num = 1020)
    x = grids["X_"][:1]
    y = grids["Y_"][:, 1:2]
      
    #build Landlab resolution array
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
    
    print('Dimensions of DHSVM Model Grid')
    print(x.shape)
    print(y.shape)
    
    print('Dimensions of Landlab Model Grid')
    print(x1_.shape)
    print(y1_.shape)

    #Put data into xarray 
    ds_wt = xr.Dataset(data_vars = {'wt': (('time', 'y', 'x'), all_arrays)})
    ds_wt['time'] = dates['date'].tolist() #hese dates are strings
    ds_wt['y'] = y
    ds_wt['x'] = x
    print('Formatted for xarray dataset')
          
    #Reshape DHSVM grid to Landlab Grid
    y1 = y1.reshape(y1.shape[0])
    x1 = x1.reshape(x1.shape[0])
    dsi = ds_wt.interp(y = y1, x = x1)
    
    #WRite netcdf outputs to file
    print('Printing netcdf4')
    dsi.to_netcdf(nc4out)
    print('Printing netcdf3')
    dsi.to_netcdf(nc3out, format = 'NETCDF3_64BIT')

    
    #Create python dictionary of depth to water tabls
   
#    HSD_dict_annualmaxDWT_hist={}
#    counter=0
#    for j in range(len(x)):
#        for k in range(len(y)):
#            one_location=dsi.isel(x=[j],y=[k]).to_array()
#            loc1list=np.array(one_location.variable)
#            b = list(itertools.chain(*loc1list))
#            c = list(itertools.chain(*b))
#            d = list(itertools.chain(*c))
#            HSD_dict_annualmaxDWT_hist[counter] = {keys[counter]:d} 
#            counter=counter+1
#
#    with open(HSDout, 'w') as output:
#        pickle.dump(HSD_dict_annualmaxDWT_hist, output)
    

    
path_historic='dtw_DHSVMoutput_20190502/output_SCLlandslide_historic/Map.Soil.TableDepth.asc'
path_dates = 'export_historic_dates'
Skagit150colsize=1020  #low resolution model columns
HSDout='HSD_dict_annualmaxDWT_hist.pkl'
nc4out='dtw_historic_with_dates_netcdf4.nc'
nc3out='dtw_historic_with_dates_netcdf3.nc'
#historic
ronda(path_historic,path_dates,Skagit150colsize,nc3out,nc4out,HSDout)



path_45_C='dtw_DHSVMoutput_20190502/output_SCLlandslide_bclivlow_G_CNRM-CM5__rcp45/Map.Soil.TableDepth.asc'
path_85_C='dtw_DHSVMoutput_20190502/output_SCLlandslide_bclivlow_G_CNRM-CM5__rcp85/Map.Soil.TableDepth.asc'
path_45_H='dtw_DHSVMoutput_20190502/output_SCLlandslide_bclivlow_G_HadGEM2-ES365__rcp45/Map.Soil.TableDepth.asc'
path_85_H='dtw_DHSVMoutput_20190502/output_SCLlandslide_bclivlow_G_HadGEM2-ES365__rcp85/Map.Soil.TableDepth.asc'
path_45_N='dtw_DHSVMoutput_20190502/output_SCLlandslide_bclivlow_G_NorESM1_M__rcp45/Map.Soil.TableDepth.asc'
path_85_N='dtw_DHSVMoutput_20190502/output_SCLlandslide_bclivlow_G_NorESM1_M__rcp85/Map.Soil.TableDepth.asc'
pathlist=[path_historic,path_45_C,path_85_C,path_45_H,path_85_H,path_45_N,path_85_N]


path_45_C_dates='export_dates_sat_CNRM_CM5_rcp45'
path_85_C_dates='export_dates_sat_CNRM_CM5_rcp85'
path_45_H_dates='export_dates_sat_HadGEM2_ES365_rcp45'
path_85_H_dates='export_dates_sat_HadGEM2_ES365_rcp85'
path_45_N_dates='export_dates_sat_NorESM1_M_rcp45'
path_85_N_dates='export_dates_sat_NorESM1_M_rcp85'
datelist=[path_dates,path_45_C_dates,path_85_C_dates,path_45_H_dates,path_85_H_dates,path_45_N_dates,path_85_N_dates]

path_grids='grids.pkl'
with open(path_grids, 'rb') as f:
    grids = pickle.load(f)
    
    

