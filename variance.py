
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

import matplotlib.pyplot as plt

data=np.arange(0,16) 
data=data.reshape(-1,4)
print data
var_orig=np.var(data)
print var_orig,'orig var'
rows,col=data.shape
#print data[1,:]
#print data
n=4
var=[]
var_row=[]
var_col=[]
for i in range(2,n):
    k=rows%i
    column=np.transpose(data)     
    if k==0:     
        column=column.reshape(-1,i)     
    else:
        column=data.reshape(1,-1)
        column=column[0][0:-k] #have to include the [0] because the matrix is ([[..]]) and you want to eliminate
        #array element so first you must extract array, so ([[..]])[0]=([..])
        column=np.transpose(column.reshape(-1,i))
    column=np.mean(column,axis=1)
    #column=column.reshape(rows/i,col)...don't need to reshape after taking the mean, since you calc variance
    #of flattened array
    var_col.append(np.var(column))
    print var_col     

for i in range(2,n):
    j=col%i
    if j==0:
        row=np.mean(data.reshape(-1,i),axis=1)
        print row #Axis=1 means taking average of each row, which here means averaging
#over time
    else:
        row=data.reshape(1,-1)
        row=row[0][0:-j]
        row=row.reshape(-1,i)
        row=np.mean(row,axis=1)
#plt.imshow(mean_rows, aspect='auto', cmap='hot')
    var_row.append(np.var(row))
    print var_row  
    
    mean_col=np.transpose(row)
    print mean_col.shape
    mean_col=mean_col.reshape(-1,i)

    rows_col,col_col=mean_col.shape
    mean_col=np.mean(mean_col,axis=1)
    print mean_col.shape

    mean_col=mean_col.reshape(rows_col/i,col_col)
    print mean_col.shape

    mean_col=np.transpose(mean_col)
    print mean_col.shape
    
    #var=np.var(mean_col)
    var.append(np.var(mean_col))
    print var,i
    
print var,'both'
print var_row,'row'
print var_col,'col'
print np.transpose(var)

#mean = np.mean(data,axis=1)
#plt.plot(mean)
#plt.imshow(np.transpose(mean_col), aspect='auto', cmap='hot')
#plt.imshow(var, aspect='auto', cmap='hot')
plt.plot(var,'o')
#plt.plot(np.arange(len(mean)), mean)
#print mean[39000:40100].shape, np.arange(39000,40100).shape
#plt.plot(np.arange(39720,39745), mean[39720:39745])
ax = plt.gca()
#plt.plot(np.arange(39720,39745), mean[39720:39745])

plt.show()
