# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:06:32 2018

@author: kad017
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:46:34 2018

@author: kad017
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
rows,col=data.shape
#res_row,res_col=(1+rows/2,1+col/2)
res_row,res_col=data.shape
print rows,"rows"

column_t=np.transpose(data)
print column_t,"transposed data,orig"
var_row_i=[]
var_col_i=[]

var_colrow_i=[]


        
for i in range (2,res_row):

    print i, "i"
    k=rows%i
    print k,"k"
    
    def col0(inp):
        column=inp[:,[x,rows]]
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
        rownum,colnum=column1.shape
        print column1
        #column=column[0][0:-k] #have to include the [0] because the matrix is ([[..]]) and you want to eliminate
        #array element so first you must extract array, so ([[..]])[0]=([..])
        column1=column1.reshape(-1,i)
        print column1,"transposed data,non zero k"
        column1=np.mean(column1,axis=1)
        print column1, "averaged col data"
        column1=column1.reshape(rownum,colnum/i)
        print column1,"col1 reshaped"
    #column=column.reshape(rows/i,col)...don't need to reshape after taking the mean, since you calc variance
    #of flattened array
        column2=inp[:,[nrow-k,nrow-1]]
        print column2,"column2"
        column2=np.mean(column2,axis=1)
        print column2,"mean column 2"
        column2=column2.reshape(-1,1)
        print column2,"reshaped"
        column2=np.hstack((column1,column2))
        print column2,"combined"
        var_col_i.append(np.var(column2))
        print var_col_i,"variance for columns"
        return var_col_i
    
    if k==0:
        col0(column_t)
    else:

        coln0(column_t,rows)

"Using function to average columns only in orig data"

#For averaging rows only
for i in range(2,res_col):
    print i,"i"
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
       
        for n in range (2,res_row):
            print n, "n"
            k=rows%n
            print k,"k"
            row_t=np.transpose(row_shaped)
            if k==0:
                column=row_t.reshape(-1,n)
                print column,"transposed data, zero k"
                column=np.mean(column,axis=1)
                print column, "averaged col data"
                var_colrow_i.append(np.var(column))
                print var_colrow_i,"variance for columns and rows"
    #column=column.reshape(rows/i,col)...don't need to reshape after taking the mean, since you calc variance
    #of flattened array
            else:
                column1=np.delete(row_t,np.s_[rows0-k:rows0],axis=1)
                print column1
                rownum1,colnum1=column1.shape
        #column=column[0][0:-k] #have to include the [0] because the matrix is ([[..]]) and you want to eliminate
        #array element so first you must extract array, so ([[..]])[0]=([..])
                column1=column1.reshape(-1,n)
                print column1,"transposed data,non zero k"
                column1=np.mean(column1,axis=1)
                column1=column1.reshape(rownum1,colnum1/n)
                print column1, "averaged col data"
                column2=row_t[:,[rows0-k,rows0-1]]
                print column2,"column2"
                column2=np.mean(column2,axis=1)
                print column2,"mean column 2"
                column2=column2.reshape(-1,1)
                print column2,"reshaped"
                column2=np.hstack((column1,column2))
                print column2,"combined"
                var_colrow_i.append(np.var(column2))
                print var_colrow_i,"variance for columns and rows"
        
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
        row2=data[:,[col-j,col-1]]
        print row2,"row2"
        row2=np.mean(row2,axis=1)
        print row2,"mean row 2"
        row2=row2.reshape(-1,1)
        print row2,"reshaped row 2"
        row1=np.hstack((row1,row2))
        print row1,"combined"
        var_row_i.append(np.var(row1))
        print var_row_i,"variance for rows"

         #Axis=1 means taking average of each row, which here means averaging
#over time
        for n in range (2,res_row):
            print "LAST PART"
            row1_t=np.transpose(row1)
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
                print row1,"row1"
                print row1_t,"transposed row1"
                column1=np.delete(row1_t,np.s_[rows1-k:rows1],axis=1)
                print column1
                rownum2,colnum2=column1.shape
        #column=column[0][0:-k] #have to include the [0] because the matrix is ([[..]]) and you want to eliminate
        #array element so first you must extract array, so ([[..]])[0]=([..])
                column1=column1.reshape(-1,n)
                print column1,"transposed data,non zero k"

                column1=np.mean(column1,axis=1)
                print column1, "averaged col data"
                column1=column1.reshape(rownum2,colnum2/n)
                print column1, "reshaped col1"
                column2=row1_t[:,[rows1-k,rows1-1]]
                print column2,"column2"
                column2=np.mean(column2,axis=1)
                print column2,"mean column 2"
                column2=column2.reshape(-1,1)
                print column2,"reshaped col2"
                column2=np.hstack((column1,column2))
                print column2,"combined"
                var_colrow_i.append(np.var(column2))
                print var_colrow_i,"variance for columns and rows"

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