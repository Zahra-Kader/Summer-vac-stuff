#!/usr/bin/python
import math
import numpy as np

#import matplotlib.pyplot as plt
#from matplotlib import rc
#from matplotlib.patches import Circle

#import astropy.units as u
#from astropy.coordinates import SkyCoord
#from astropy.coordinates import EarthLocation, SkyCoord, ICRS, AltAz
#from astropy.utils.data import download_file
#from astropy.utils import iers
#iers.IERS.iers_table = iers.IERS_A.open(download_file(iers.IERS_A_URL, cache=True))
#from astropy.time import Time
#from datetime import datetime

import subprocess
import argparse
import re

#rc('text', usetex=True)

# read in parameters

parser = argparse.ArgumentParser(description='Fold with PRESTO')
parser.add_argument('-f', '--input_filename', metavar='Input file name', nargs='+', required=True, help='Input file name')
parser.add_argument('-snr', '--snr_threshold', metavar='SNR threshold', nargs='+', required=True, help='SNR threshold')
parser.add_argument('-clip', '--clip_sigma', metavar='Clipping sigma', nargs='+', required=True, help='Clipping sigma')

args = parser.parse_args()

in_filename = args.input_filename[0]
snr = float(args.snr_threshold[0])
clip = args.clip_sigma[0]
print in_filename, snr

#################################################################
# RFI mask
rfi_root = "rfi_root"

#################################################################
# ACCEL_sift > candlist
'''
candlist = 'candlist.txt'
proc = subprocess.Popen(['python', '/data/too043/apps/pulsarsoft/workspace/psr-presto-build/python/ACCEL_sift.py'], shell=False, stdout=subprocess.PIPE)
f = open(candlist, 'w')
f.write(proc.stdout.read())
f.close()
'''

#################################################################
# prepfold
rfi_mask = rfi_root + '_rfifind.mask'
candlist = 'candlist.txt'
nsubband = 32

file_cand = []
num_cand = []
snr_cand = []
DM_f = []
p_f = []
f = open(candlist, 'r')
for line in f:
	if re.search(in_filename,line):
		#print line
		snr_temp = float(line.split()[2])
		if snr_temp >= snr:
			temp = line.split()[0]
			file_cand.append(temp.split(":")[0] + '.cand')
			num_cand.append(temp.split(":")[1])

			DM_f.append(float(line.split()[1]))
			snr_cand.append(float(line.split()[2]))
			p_f.append(float(line.split()[7])*1e-3)   # second

f.close()

#print snr_cand, DM_f, p_f, file_cand, num_cand

for i in range(len(file_cand)):
	fold_out = in_filename + '_ACCEL_DM' + str(DM_f[i]) + '_P' + str(p_f[i])
	#subprocess.call(['prepfold', '-noscales', '-nooffsets', '-psrfits', '-npart', '256', '-noxwin', '-clip', clip, '-mask', rfi_mask, '-dm', str(DM_f[i]), '-nsub', str(nsubband), '-nosearch', '-o', fold_out, '-accelcand', num_cand[i], '-accelfile', file_cand[i], in_filename], shell=False)
	subprocess.call(['prepfold', '-ncpus', '6', '-noscales', '-nooffsets', '-psrfits', '-npart', '256', '-noxwin', '-clip', clip, '-mask', rfi_mask, '-dm', str(DM_f[i]), '-nsub', str(nsubband), '-nosearch', '-o', fold_out, '-accelcand', num_cand[i], '-accelfile', file_cand[i], in_filename], shell=False)
