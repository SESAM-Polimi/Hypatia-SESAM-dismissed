# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:31:10 2022

@author: Gianluca Pellecchia
"""

import pandas as pd
import numpy as np

# stampare i dati
pd.read_excel("Input_RES.xlsx", sheet_name="Sheet1") 

#salvare i dati dentro una variabile
xlsx = pd.read_excel("Input_RES.xlsx", sheet_name="Sheet1") 
# a=xlsx.iloc[8759][125]

avg = np.zeros((24,3))
d = 0

for j in range(0,3,1):
    for r in range (0,24,1):
        for i in range(r,8760,24):
            d = d + xlsx.iloc[i][j]
        avg[r,j] = d/365
        d = 0
        
df1 = pd.DataFrame(avg)
df1.to_excel('Average_RES.xlsx')
        
        
        