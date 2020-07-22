#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:28:21 2017

@author: sudheep
"""

import pandas as pd 

df1 = pd.read_excel('/home/sudheep/Desktop/IBM/Custom Analytics/Schneider/Incident Data.xlsx')
df2 = pd.read_excel('/home/sudheep/Desktop/IBM/Custom Analytics/Schneider/Automation_Output.xlsx')
#df3 = pd.read_excel('/home/sudheep/Desktop/IBM/Custom Analytics/TE Connectivity/IPC&SR/Incident dump/Inc with Notes/Consolidated_Master_Output.xlsx')

#df2 = df2[['number', 'closure_code']]
#df4 = df3[['number', 'SUMMARY', 'assignment_group', 'priority', 'sys_created_on', 'resolved_at']]

#df5=df1.merge(df2, on='Name')

merge=pd.merge(left=df1,right=df2,on='Job_Name',how='left')

#Write as Excel output
merge.to_excel('/home/sudheep/Desktop/IBM/Custom Analytics/TE Connectivity/IPC&SR/Incident/DA Analysis/Automation_Final_Output.xlsx',index=False)
