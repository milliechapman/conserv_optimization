#!/usr/bin/env python3

import sys
import knapsack as kp
import pandas as pd

if (len(sys.argv) != 3):
        sys.exit("Usage: ./analsis <budget> <data_file.csv>")

budget = int(sys.argv[1])
data_filename=str(sys.argv[2])


df = pd.read_csv(data_filename, low_memory=False)

# limit analysis to cells within budget
# requires the data be sorted by price in ascending order
num = 0
for i in range(0,len(df)):
    if (df['price'].data[i] <= budget):
        num += 1

# populate input lists for knapsack analysis
weight = [0]*(num+1)
benefit = [0]*(num+1)
W = int(budget/1000)
print("budget = {}".format(W*1000))
for i in range(0,num+1):
    weight[i] = int(df['price'].data[i]/1000)
    benefit[i] = int(df['area'].data[i])

# call the knap sack function
B = kp.solve(weight, benefit, W)
# find the maximum area possible for purchase
C = kp.capacity(B)
# find the indicies 
idx = kp.indices(B, weight)

price_total_round = 0
price_total_actual = 0
area_total = 0;
for i in range(len(idx)):
    j = idx[i]-1
    price_total_round += weight[j]*1000
    price_total_actual += df['price'].data[j]
    area_total += benefit[j]


# updates the decision variable
def assoc_idx(data_frame, idx):
    for i in range(len(idx)):
        for j in range(len(df)):
            if (j-1) == (idx[i]-1):
                print("cell[{}]: weight={}, benefit={}".format(j-1, weight[idx[i]-1], benefit[idx[i]-1]))
                df['decision'].data[j-1] = 1


# add decision column all zeros
df['decision'] = [0]*len(df)
assoc_idx(df, idx)

# loop for each cell of the optimized solution
# loop thru the data frame and match the cell "idx[i]" to
# the data frame index. 
#for i in range(len(idx)):
#    for j in range(len(df)):
#        if (j == (idx[i]-1)):
#            df['decision'].data[j] = 1

            
print("Total Price Calculated = {}.00[$]".format(price_total_round))
print("Total Price Actual = {:8.2f}[$]".format(price_total_actual)) 
print("Total Area = {} [hA]".format(area_total))
print("Cells Chosen to Maximize Conserved Area Within Budget")
print(idx)


# print decision data
print("Saving data with appended decision data as './data.csv'")
print("Conservation decision performed to optimize land use")
df.to_csv('decision.csv')
print("")
