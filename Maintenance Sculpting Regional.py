# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

docs = pd.read_excel("C:/Users/ytohidi/Desktop/Work/Maintenance Sculpting Profile.xlsx",
                           na_filter=True, keep_default_na=True)

docs['NewSheet'] = docs['Child Name'].str[:4]

shname = list(pd.unique(docs['NewSheet']))

with pd.ExcelWriter("C:/Users/ytohidi/Desktop/Work/1982_Maintenance_Profile.xlsx", engine="openpyxl") as writer:
    for i in shname:
        newDF = docs[(docs['NewSheet'] == i)]
        newDF.to_excel(writer, sheet_name=i, index=False)