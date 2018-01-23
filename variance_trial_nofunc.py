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



column_t=np.transpose(data)
var_row_i=[]
var_col_i=[]
var_colrow_i=[]
for i in range (2,rows):
    print i, "i"
    k=rows%i
    print k,"k"
    def col0(inp):
        column=inp.reshape(-1,i)
        print column,"transposed data, zero k"
        column=np.mean(column,axis=1)
        print column, "averaged col data"
    #column=column.reshape(rows/i,col)...don't need to reshape after taking the mean, since you calc variance
    #of flattened array
        var_col_i.append(np.var(column))
        print var_col_i,"variance for columns"
        return var_col_i
    def coln0(inp,nrow):
        print inp
        column1=np.delete(inp,np.s_[nrow-k:nrow],axis=1)
        print column1
        #column=column[0][0:-k] #have to include the [0] because the matrix is ([[..]]) and you want to eliminate
        #array element so first you must extract array, so ([[..]])[0]=([..])
        column1=column1.reshape(-1,i)
        print column1,"transposed data,non zero k"
        column1=np.mean(column1,axis=1)
        print column1, "averaged col data"
    #column=column.reshape(rows/i,col)...don't need to reshape after taking the mean, since you calc variance
    #of flattened array
        var_col_i.append(np.var(column1))
        print var_col_i,"variance for columns"
        return var_col_i
        
    if k==0: 
        col0(column_t)
    else:
        
        coln0(column_t,rows)

"Using function to average columns only in orig data"

#For averaging rows only
for i in range(2,col):
    print i,"i"
    j=col%i
    print j,"j"
    def row0(inp):
        row=inp.reshape(-1,i)
        row=np.mean(row,axis=1)
        row_shaped=row.reshape(-1,col/i)
        rows0,col0=row_shaped.shape
        var_row_i.append(np.var(row))
        print var_row_i,i,"variance for rows"  
        return var_row_i,row_shaped,rows0

    

    def rown0(inp):
        print inp, "input data"
        row1=np.delete(inp,np.s_[col-j:col],axis=1)
        row1=row1.reshape(-1,i)
        row1=np.mean(row1,axis=1)
        row1_shaped=row1.reshape(-1,(col-j)/i)
        rows1,col1=row1_shaped.shape
        var_row_i.append(np.var(row1))
        print var_row_i,i,"variance for rows"
        return var_row_i,row1_shaped,rows1  

    
    if j==0:
    variance_row,shaped_row,rows0=row0(data)
        variance_row
         #Axis=1 means taking average of each row, which here means averaging
#over time
    else:
        variance_row1,shaped_row1,rows1=rown0(data)        
        variance_row1


    for i in range (2,rows):
        print "PENULT"
        print shaped_row,"row0"
        row_t=np.transpose(shaped_row)
        print i, "i"
        k=rows0%i
        print k,"k"
                
        if k==0: 
            col0(row_t) 
        else:
            coln0(row_t,rows0)

    for i in range (2,rows):
        print "LAST PART"
        variance_row1,shaped_row1,rows1=rown0(data)        
        row1_t=np.transpose(shaped_row1)
        print i, "i"
        k=rows1%i
        print k,"k"
             
        if k==0: 
            col0(row1_t) 
        else:
            coln0(row1_t,rows1)    
    
print var_row_i,'row'
print var_col_i,'col'

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