# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:38:04 2018

@author: kad017
"""

import math
import numpy as np

import matplotlib.pyplot as plt
#from matplotlib import rc
#from matplotlib.patches import Circle

#import subprocess
import argparse
#import glob

import pyfits

#rc('text', usetex=True)
# read in parameters
parser = argparse.ArgumentParser(description='Do FFT with PRESTO')
parser.add_argument('-f', '--input_file', metavar='Input file name', nargs='+', required=True, help='Input file name')

args = parser.parse_args()

in_file = args.input_file[0]

hdulist = pyfits.open(in_file)
tbdata = hdulist['SUBINT'].data
hdulist.close()

subint=hdulist['SUBINT']
nchan=subint.header['NCHAN']
nsamp_per_row=subint.header['NSBLK']
nbits = subint.header['NBITS']
#################################################################
#data = np.reshape(np.squeeze(tbdata['DATA']), (1024*2311,512))
#data0 = np.reshape(np.squeeze(tbdata['DATA'][:200]), (1024*200,512)).astype(int)
data0 = np.reshape(np.squeeze(tbdata['DATA'][:200]), (nsamp_per_row*200*nbits/8,nchan)).astype(int)

'''
-take first 200 rows of the tbdata out of 5496 (in the case of this data)
-4096 samples per row but divide by 4 if you are going from 8 bit to 2 bit. Reason being that
pyfits reads in 8 bit data and search mode data is two bit. So altogether you have 1024 samples/row
and we look at 200 rows.
-And we have 512 channels
-We are reshaping the data to form rows equal to sample no. and columns equal to channel number,
hence np.reshape. The reason for this is to construct freq vs time plot.
'''
#data0 = np.reshape(np.squeeze(tbdata['DATA'][0]), (1024,512)).astype(int)
#print data0

'''
data = np.empty((2048*20,512))
for i in np.arange(512):
    print i
    for j in np.arange(1024*20):
        for k in np.arange(2):
            mask = 2**(nbits*k)*(2**nbits-1)
            #print mask,data0[j,i]
            #val = (int(data0[j,i]) & mask) 
            val = ((int(data0[j,i]) & mask) >> (k*nbits))
            data[2*j+1-k,i] = val
'''

data = np.bitwise_and(data0, 2**nbits-1)
#print data[0,:]
print data.shape   #This shape is of course the dimensions you reshaped it to, which is given in
#the reshape command
for k in np.arange(0,8/nbits):
    mask = 2**(nbits*k)*(2**nbits-1)
    temp = np.right_shift(np.bitwise_and(data0, mask),(k*nbits))
    print temp.shape
    #data = np.insert(data,np.arange(1024*200),temp,axis=0)
    data = np.insert(data,np.arange(nchan),temp,axis=1)
#print temp[0,:]
'''
Consider simple case of an integer such as 147 with binary 10010011. This is base two, 8 bit.
We want base 2, two bit. So we shift digits to the right in groups of two.
For the mask, we get 3 for k=0, which is 11 in binary. So this returns the last two digits of the 
data0. Then we want these two at the right end, which is where they are. So np.rightshift is zero,
since k is 0, which makes sense. 
For k=1, we have 12, 1100 in binary, returns fifth and sixth digits and we shift this right,...
Then we insert temp as a column before every column in the data set
'''
data = np.reshape(data,(-1,nchan)) 
print data.shape,'shape of data'
var_orig=np.var(data)
print var_orig,'orig var'
rows,col=data.shape
#print data[1,:]
#print data
n=1
mylist=[]
for i in range(1,n+1):
    num=2**i
    mylist.append(num)
var=[]
var_row=[]
var_col=[]
for i in mylist:

    mean_col_only=np.transpose(data)    
    mean_col_only=mean_col_only.reshape(-1,i)
    mean_col_only=np.mean(mean_col_only,axis=1)
    mean_col_only=mean_col_only.reshape(rows/i,col)
    var_col.append(np.var(mean_col_only))
    print var_col    
    
    mean_rows=np.mean(data.reshape(-1,i),axis=1)
    print mean_rows #Axis=1 means taking average of each row, which here means averaging
#over time
    mean_rows=mean_rows.reshape(-1,nchan/i)
#plt.imshow(mean_rows, aspect='auto', cmap='hot')
    var_row.append(np.var(mean_rows))
    print var_row    
    mean_col=np.transpose(mean_rows)
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
print np.transpose(mylist)
Xnew = np.hstack((np.transpose(mylist),np.transpose(var)))
print Xnew
print Xnew.shape
trans=np.transpose(Xnew)
print trans
print trans.shape
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