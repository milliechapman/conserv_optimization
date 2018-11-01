#!/usr/bin/env python3


import sys
import pandas as pd
import numpy as np

sys.path.append('../')

if (len(sys.argv) != 3):
        sys.exit("Usage: ./parse_data <input_file.csv> <output_file.csv>")

input_file = str(sys.argv[1])
output_file = str(sys.argv[2])

print("Cleaning data contained in '{}'".format(input_file))

#import csv as panda data frame
df = pd.read_csv(input_file, low_memory=False)
columns = ['OBJECTID', 'Area_ha', 'ativo', 'coda', 'MEAN_12_13', 's_EcoServ', 's_Prob2020']
df = df[columns]
df.reset_index(inplace=True)

# replace all 0s with np.Nan, drop incomplete data, restore zeros
df.replace(0.0, np.nan, inplace=True)
df.dropna(axis=0, subset=['MEAN_12_13'], inplace=True)
df.dropna(axis=0, subset=['Area_ha'], inplace=True)
df.dropna(axis=0, subset=['ativo'], inplace=True)
df.replace(np.nan, 0.0, inplace=True)


#rename fields
df.rename(columns={'OBJECTID':'obj_id', 'Area_ha':'area', 'ativo':'ativo', 'MEAN_12_13':'mean','s_EcoServ':'ecoserv', 's_Prob2020':'prob2020'}, inplace=True)

# add column for price [$/ha] * [ha]
price = df['mean']*df['area']
df = df.assign(price=price.values)

# change types of some variables
#df['coda'] = df['coda'].astype(int)
#df['obj_id'] = df['obj_id'].astype(int)
#df['price'] = df['price'].astype(int)
#df['area'] = df['area'].astype(int)

# sort by price
df.sort_values(by='price', ascending=True, inplace=True)
df.reset_index(inplace=True)
del df['index']
del df['level_0']

# print data preview
print("A preview of the first 5 columns of price sorted data:")
print("")
print(df.head())
print("")

# save to csv
print("Writing data to '{}' ...".format(output_file))
df.to_csv(output_file)
print("Success!")
