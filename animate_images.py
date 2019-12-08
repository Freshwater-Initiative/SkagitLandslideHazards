#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:30:41 2019

@author: carina
"""

ds_test = dsi.isel(time=range(10))
for i in range(10):
    ds_test.isel(time=[i]).to_array().plot()
    plt.savefig(f"Python_Animation_01_frame_{i:04}.png")
    plt.close()
    
 # with ImageMagick installed
 !convert Python_Animation_01_frame_*.png Python_Animation.gif  