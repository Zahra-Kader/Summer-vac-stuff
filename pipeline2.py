# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:50:47 2017

@author: kad017
"""
#!/usr/bin/spyder
import os
#import argparse
#import numpy as np

def myexecute(cmd):
    print "'%s'"%cmd
    os.system(cmd)

filename=input("Enter filename ")
print "you entered", filename

#parser=argparse.ArgumentParser(description='find RFIs with PRESTO')
myexecute("rfifind -psrfits -nooffsets -noscales -time 2 -o rfi_root filename") #small integration time of 2 seconds for rfi. compared to 2$

#centrefreq=vap -c freq $filename | awk 'FNR == 2 {print $2}'
#bandwidth=vap -c bw $filename | awk 'FNR == 2 {print $2}'
#channelnum=vap -c nchan $filename | awk 'FNR == 2 {print $2}'
#sampletime=vap -c tsamp $filename | awk 'FNR == 2 {print $2}'
#DDplan.py -l 0 -d 100.0 -f $centrefreq -b $bandwidth -n $channelnum -t $sampletime