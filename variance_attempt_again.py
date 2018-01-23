# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 20:35:15 2018

@author: KaderF
"""

import numpy as np

#import matplotlib.pyplot as plt
m=16
data=np.arange(m) 
data=data.reshape(-1,4)
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
    if j==0:
        row=data.reshape(-1,i)
        row=np.mean(row,axis=1)
        row_shaped=row.reshape(-1,col/i)
        rows0,col0=row_shaped.shape
        var_row_i.append(np.var(row))
        print var_row_i,"variance for rows"
        
        for n in range (2,rows):
            print n, "n"
            k=rows%n
            print k,"k"
            row_t=np.transpose(row_shaped)        
            if k==0:  
                column=row_t.reshape(-1,i)
                print column,"transposed data, zero k"
                column=np.mean(column,axis=1)
                print column, "averaged col data"
                var_colrow_i.append(np.var(column))
                print var_colrow_i,"variance for columns and rows"
    #column=column.reshape(rows/i,col)...don't need to reshape after taking the mean, since you calc variance
    #of flattened array 
            else:
                column1=np.delete(row_t,np.s_[rows0-k:rows0],axis=1)
        #column=column[0][0:-k] #have to include the [0] because the matrix is ([[..]]) and you want to eliminate
        #array element so first you must extract array, so ([[..]])[0]=([..])
                column1=column1.reshape(-1,i)
                print column1,"transposed data,non zero k"
                column1=np.mean(column1,axis=1)
                print column1, "averaged col data"
    #column=column.reshape(rows/i,col)...don't need to reshape after taking the mean, since you calc variance
    #of flattened array
                var_colrow_i.append(np.var(column1))
                print var_colrow_i,"variance for columns and rows"
    else:
        row1=np.delete(data,np.s_[col-j:col],axis=1)
        row1=row1.reshape(-1,i)
        row1=np.mean(row1,axis=1)
        row1_shaped=row1.reshape(-1,(col-j)/i)
        rows1,col1=row1_shaped.shape
        var_row_i.append(np.var(row1))    
        print var_row_i,"variance for rows"
         #Axis=1 means taking average of each row, which here means averaging
#over time
        for n in range (2,rows):
            print "LAST PART"
            row1_t=np.transpose(row1_shaped)
            print row1_t
            print n, "n"
            k=rows%n
            print k,"k"
             
            if k==0: 
                column=row1_t.reshape(-1,n)
                print column,"transposed data, zero k"
                column=np.mean(column,axis=1)
                print column, "averaged col data"
                var_colrow_i.append(np.var(column))
                print var_colrow_i,"variance for columns and rows"
    #column=column.reshape(rows/i,col)...don't need to reshape after taking the mean, since you calc variance
    #of flattened array 
            else:
                column1=np.delete(row_t,np.s_[rows0-k:rows0],axis=1)
        #column=column[0][0:-k] #have to include the [0] because the matrix is ([[..]]) and you want to eliminate
        #array element so first you must extract array, so ([[..]])[0]=([..])
                column1=column1.reshape(-1,n)
                print column1,"transposed data,non zero k"
                column1=np.mean(column1,axis=1)
                print column1, "averaged col data"
    #column=column.reshape(rows/i,col)...don't need to reshape after taking the mean, since you calc variance
    #of flattened array
                var_colrow_i.append(np.var(column1))
                print var_colrow_i,"variance for columns and rows"    

print var_colrow_i,"variance for columns and rows"    
print var_row_i,'row'
print var_col_i,'col'

var_row_i=np.array(var_row_i)
var_col_i=np.array(var_col_i)
var_colrow_i=np.array(var_colrow_i)

var_colrow_i=var_colrow_i.reshape(2,2)
final_matrix=np.vstack((var_colrow_i,var_row_i))
print final_matrix

var_col_i=np.append(var_col_i,[var_orig])
var_col_i=var_col_i.reshape(-1,1)

print var_col_i
final_matrix=np.hstack((var_col_i,final_matrix))
print final_matrix

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