# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
''' GET THE DATA
import argparse
parser = argparse.ArgumentParser(description='Do FFT with PRESTO')
parser.add_argument('-f', '--input_file', metavar='Input file name', nargs='+', required=True, help='Input file name')
args = parser.parse_args()
in_file = args.input_file[0]
data=np.loadtxt(in_file)
data=data[:,2]
data=data.reshape(1024,100)
plt.imshow(data,aspect='auto',cmap='hot')
plt.show()
'''
#a=np.array([1,1,1,1,0,0,0,0,1,1,1,1])
#data=np.vstack((a,a))
#data=np.vstack((data,data))
#data=np.random.randn(128,128)
'''
mat=np.linspace(8,8.5,8)
mat=mat.reshape(2,4)
a=np.random.rand(1,4)
mat=np.vstack((mat,a))
mat=np.vstack((a,mat))
b=np.random.rand(6,4)
mat=np.hstack((b,mat))
'''
#data=np.hstack((mat,b))
data=np.random.rand(16)
data=data.reshape(4,4)
print data
var_orig=np.var(data)
print var_orig,'orig var'
#res_row,res_col=(1+rows/2,1+col/2)
res_row,res_col=data.shape

data_t=np.transpose(data)
rows_t,col_t=data_t.shape
print data_t,"transposed data,orig"
var_row_i=[]
var_col_i=[]

var_colrow_i=[]
    


def variance_rows(inp):
    for i in range (2,res_row):

        for x in range(0,i):
            print x,"x"
            print i, "i"
            print inp,"before moving columns"
            rows,col=inp.shape
            inp_x_mod=inp[:,x:col]
            rows,col=inp_x_mod.shape
            k=col%i
            print k,"k"
            print inp_x_mod, "after moving one col right in transposed"
            print inp_x_mod.shape
            

            if k==0:
                inp_reshape=inp_x_mod.reshape(-1,i)
                print inp_reshape,"transposed data, zero k"
                inp_avg=np.mean(inp_reshape,axis=1)
                print inp_avg, "averaged col data"
            #column=column.reshape(rows/i,col)...don't need to reshape after taking the mean, since you calc variance
            #of flattened array
                var_col_i.append(np.var(inp_avg))
                print var_col_i,"variance for columns"
            else:
                print rows
                inp_nondiv_mod=np.delete(inp_x_mod,np.s_[col-k:col],axis=1)
                print inp_nondiv_mod,"after taking out extra columns"
                #column=column[0][0:-k] #have to include the [0] because the matrix is ([[..]]) and you want to eliminate
                #array element so first you must extract array, so ([[..]])[0]=([..])
                inp_reshape=inp_nondiv_mod.reshape(-1,i)
                print inp_reshape,"transposed data,non zero k"
                inp_avg=np.mean(inp_reshape,axis=1)
                print inp_avg, "averaged col data"
                var_col_i.append(np.var(inp_avg))
                print var_col_i,"variance for columns"
    return var_col_i

variance_rows(data_t)

"Using function to average columns only in orig data"

#For averaging rows only
for i in range(2,res_col):
    for x in range(0,i):
        print i,"i rows"
        print x,"x"
        print data
        rows,col=data.shape
        print col
        data=data[:,x:col]
        print data
        rows,col=data.shape
        print data, "after moving one col right"
        print data.shape
        j=col%i
        print j,"j"
        if j==0:
            row=data.reshape(-1,i)
            print row
            row=np.mean(row,axis=1)
            print row,"averaged row only"
            row_shaped=row.reshape(-1,col/i)
            print row_shaped,"new matrix row after averaging"
            rows0,col0=row_shaped.shape
            var_row_i.append(np.var(row))
            print var_row_i,"variance for rows"
    
            variance_rows(row_shaped)
    
        else:
            print data
            row1=np.delete(data,np.s_[col-j:col],axis=1)
            print row1
            row1=row1.reshape(-1,i)
            print row1
            row1=np.mean(row1,axis=1)
            print row1
            row1=row1.reshape(-1,(col-j)/i)
            print row1,"row1 reshaped"
            rows1,col1=row1.shape
            var_row_i.append(np.var(row1))
            print var_row_i,"variance for rows"
    
             #Axis=1 means taking average of each row, which here means averaging
    #over time
            variance_rows(row1)

print var_colrow_i,"variance for columns and rows"
print var_row_i,'row'
print var_col_i,'col'

var_row_i=np.array(var_row_i)
var_col_i=np.array(var_col_i)
var_col_i=np.flipud(var_col_i)

var_colrow_i=np.array(var_colrow_i)

var_colrow_i=var_colrow_i.reshape(res_col-2,res_row-2)
var_col_i=np.append(var_col_i,[var_orig])
var_col_i=var_col_i.reshape(-1,1)
#var_colrow_i = zip(*var_colrow_i[::-1])
#var_colrow_i = zip(*var_colrow_i[::-1])
#var_colrow_i = zip(*var_colrow_i[::-1])
var_colrow_i=np.transpose(var_colrow_i)
var_colrow_i=np.flipud(var_colrow_i)
print var_colrow_i
print type(var_colrow_i)


final_matrix=np.vstack((var_colrow_i,var_row_i))
print final_matrix



print var_col_i
final_matrix=np.hstack((var_col_i,final_matrix))
print final_matrix
final_matrix=np.flipud(final_matrix)
print var_orig
print final_matrix
#mean = np.mean(data,axis=1)
#plt.plot(mean)
fig, ax = plt.subplots()
im = ax.imshow(final_matrix,cmap=plt.get_cmap('hot'),aspect='auto', interpolation='nearest',origin='lower')
fig.colorbar(im)
plt.show()
#plt.imshow(final_matrix, aspect='auto', cmap='hot',origin='lower')
#plt.imshow(var, aspect='auto', cmap='hot')
#plt.plot(np.arange(len(mean)), mean)
#plt.plot(np.arange(39720,39745), mean[39720:39745])
#ax = plt.gca()
#plt.plot(np.arange(39720,39745), mean[39720:39745])

plt.show()

























