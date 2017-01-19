# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:19:11 2016

@author: Rodger
"""

import json
import yaml
import time

data = {    
        'Header': { \
            'Project Name': 'ProjectName', \
            'Date': time.strftime("%d/%m/%Y"), \
            'Time': time.strftime("%H:%M:%S"), \
            'Physics': 'Electromagnetics', \
            'Solver Type': ['Forward','DE','Transient-Explicit','FD'], \
            'Coordinate System': 'Cartesian', \
            'Unit': {'Length Unit': 'meter', \
                     'Time Unit': 'second' } }, \
                 
        'Simulation': { \
            'Mesh Data': "C:/Test/Mesh.txt", \
            'Time Control': {'Time Step': 5e-12, 'Time Window': 5e-9}},\
        
        'Physics Entities': {
            'Background': {'Attribute':{'OprType': 'Interface','GeoType': 'Volume', \
                                        'PhyType': 'Material','Ranking': 1}}, \
            'Entity Parameters': { 'Relative Permitivitty': 1, 'Relative Permeability'
            
            }            
            }                           
       }   

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, sort_keys=True, separators=(',', ':'))
    
