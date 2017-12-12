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
import glob

#rc('text', usetex=True)

# read in parameters

parser = argparse.ArgumentParser(description='Prepsubband and FFT with PRESTO')
parser.add_argument('-f', '--input_filename', metavar='Input file name', nargs='+', required=True, help='Input file name')
parser.add_argument('-dmlo', '--DM_low', metavar='Lower bound of DM', nargs='+', required=True, help='Lower bound of DM')
parser.add_argument('-dmhi', '--DM_high', metavar='Higher bound of DM', nargs='+', required=True, help='Higher bound of DM')
parser.add_argument('-clip', '--clip_sigma', metavar='Clipping sigma', nargs='+', required=True, help='Clipping sigma')

args = parser.parse_args()

in_filename = args.input_filename[0]
dmlo = float(args.DM_low[0])
dmhi = float(args.DM_high[0])
clip = args.clip_sigma[0]
print in_filename, dmlo, dmhi, clip

#################################################################
# RFI mask
rfi_root = "rfi_root"

#################################################################
# read bw, nchan, nout
#bw = 'readfile $rawfile | grep 'Total Bandwidth' | awk '{print int($5)}'`'
#nchan = 'readfile $rawfile | grep 'Number of channels' | awk '{print int($5)}'`'
#nout = 'readfile $rawfile | grep 'Spectra' | grep "file" | awk '{print int($5)}'`'
#print bw, nchan, nout

proc = subprocess.Popen(["readfile", in_filename], shell=False, stdout=subprocess.PIPE)
lines = proc.stdout.readlines()
#print lines
for line in lines:
	#print line
	if "Total Bandwidth" in line:
		#print line.split()
		bw = float(line.split()[4])
		print "Total Bandwidth:", bw, 'MHz'
	elif "Number of channels" in line:
		#print line.split()
		nchan = int(line.split()[4])
		print "Number of channels:", nchan
	elif "Spectra per file" in line:
		#print line.split()
		nout = int(line.split()[4])
		print "Spectra per file:", nout
	elif "Sample time" in line:
		#print line.split()
		tsamp = float(line.split()[4])/1e6
		print 'Sample time:', tsamp, 's'

#################################################################
# run DDplay.py
# DDplan.py -l $dmlo -d $dmhi -b $bw -n $nchan -o t.eps > $ddplano

#ddplan_out = 'ddplan.out.txt'
ddplan_fig = 'ddplan_fig.eps'
proc = subprocess.Popen(["DDplan.py", "-l", str(dmlo), "-d", str(dmhi), "-b", str(bw), "-n", str(nchan), "-t", str(tsamp), "-o", ddplan_fig], shell=False, stdout=subprocess.PIPE)

lines = proc.stdout.readlines()
#print proc.stdout.read()
dmlos = []
dmhis = []
ddm = []
dms = []
for line in lines:
	numbers = re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", line)
	print line
	if len(numbers) == 6:
		dmlos.append(float(line.split()[0]))
		dmhis.append(float(line.split()[1]))
		ddm.append(float(line.split()[2]))
		dms.append(float(line.split()[4]))
		#ddm.append(float(line.split()[2])/10.0)
		#dms.append(float(line.split()[4])*10.0)
#print dmlos
#print dmhis
#print ddm
#print dms
#print lines

#################################################################
# prepsubband
nsubband = 32
rfi_mask = rfi_root + '_rfifind.mask'

for i in range(len(dmlos)):
	lodm = str(dmlos[i])
	dmstep = str(ddm[i])
	ndm = str(int(dms[i]))
	print lodm, dmstep, ndm, nout
	#subprocess.call(['prepsubband', '-nooffsets', '-noscales', '-psrfits', '-mask', rfi_mask, '-lodm', lodm, '-dmstep', dmstep, '-numdms', ndm, '-numout', str(nout), '-nsub', str(nsubband), '-o', in_filename, in_filename], shell=False)
	#subprocess.call(['prepsubband', '-nooffsets', '-noscales', '-psrfits', '-clip', clip, '-mask', rfi_mask, '-lodm', lodm, '-dmstep', dmstep, '-numdms', ndm, '-numout', str(nout), '-nsub', str(nsubband), '-o', in_filename, in_filename], shell=False)
	subprocess.call(['prepsubband', '-ncpus', '8', '-nooffsets', '-noscales', '-psrfits', '-clip', clip, '-mask', rfi_mask, '-lodm', lodm, '-dmstep', dmstep, '-numdms', ndm, '-numout', str(nout), '-nsub', str(nsubband), '-o', in_filename, in_filename], shell=False)
	#subprocess.call(['prepsubband', '-ncpus', '10', '-clip', clip, '-mask', rfi_mask, '-lodm', lodm, '-dmstep', dmstep, '-numdms', ndm, '-numout', str(nout), '-nsub', str(nsubband), '-o', in_filename, in_filename], shell=False)

#################################################################
# realfft
#for dat_file in glob.glob("*.dat"):
#	print dat_file
#	subprocess.call(["realfft", "-men", "-fwd"], shell=False)
#	subprocess.call(["realfft", "-fwd", dat_file], shell=False)

