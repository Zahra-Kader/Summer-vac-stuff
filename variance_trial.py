# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 09:39:20 2018

@author: kad017
"""

import numpy as np

#import matplotlib.pyplot as plt
m=16
data=np.arange(m) 
data=data.reshape(-1,np.sqrt(m))
print data
var_orig=np.var(data)
print var_orig,'orig var'
rows,col=data.shape
print rows,"rows"
var_row=[]
var_col=[]

"Function for averaging columns only"
def func(input):
    column=np.transpose(data)
    for i in range (2,rows):
        print i, "i"
        k=rows%i
        print k,"k"
             
        if k==0: 
            column=column.reshape(-1,i)
            print column,"transposed data, zero k"
        else:
            print k,"k"
            column=np.delete(column,np.s_[rows-k:rows],axis=1)
        #column=column[0][0:-k] #have to include the [0] because the matrix is ([[..]]) and you want to eliminate
        #array element so first you must extract array, so ([[..]])[0]=([..])
            column=column.reshape(-1,i)
            print column,"transposed data,non zero k"
        column=np.mean(column,axis=1)
        print column, "averaged col data"
    #column=column.reshape(rows/i,col)...don't need to reshape after taking the mean, since you calc variance
    #of flattened array
        var_col.append(np.var(column))
        print var_col,"variance for columns"
        return var_col     

"Using function to average columns only in orig data"
col_only=func(data)
#For averaging rows only
for i in range(2,col):
    j=col%i
    if j==0:
        row=data.reshape(-1,i)
        row=np.mean(row,axis=1)
        row=row.reshape(-1,col/i)
         #Axis=1 means taking average of each row, which here means averaging
#over time
    else:
        row=np.delete(data,np.s_[col-j:col],axis=1)
        row=row.reshape(-1,i)
        row=np.mean(row,axis=1)
        row=row.reshape(-1,(col-j)/i)
    var_row.append(np.var(row))
    print var_row     
     
    row_col=func(row)
    
print var_row,'row'
print var_col,'col'

#mean = np.mean(data,axis=1)
#plt.plot(mean)
#plt.imshow(np.transpose(mean_col), aspect='auto', cmap='hot')
#plt.imshow(var, aspect='auto', cmap='hot')
#plt.plot(np.arange(len(mean)), mean)
#print mean[39000:40100].shape, np.arange(39000,40100).shape
#plt.plot(np.arange(39720,39745), mean[39720:39745])
#ax = plt.gca()
#plt.plot(np.arange(39720,39745), mean[39720:39745])

#plt.show()