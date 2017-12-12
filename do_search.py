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
import glob

#rc('text', usetex=True)

# read in parameters

parser = argparse.ArgumentParser(description='Do search with PRESTO')
parser.add_argument('-n0', '--num_1st', metavar='Number of the 1st file name', nargs='+', required=True, help='Number of the 1st file name')
parser.add_argument('-n1', '--num_last', metavar='Number of the last file name', nargs='+', required=True, help='Number of the last file name')
parser.add_argument('-zmax', '--zmax_int', metavar='Acceleration search', nargs='+', required=True, help='Acceleration search')

args = parser.parse_args()

n0 = int(args.num_1st[0])
n1 = int(args.num_last[0])
zmax = args.zmax_int[0]

#################################################################
# accelsearch
#zmax = '0'
numharm = '16'
all_files = sorted(glob.glob("*.fft"))
for i in np.arange(n0,n1):
	fft_file = all_files[i]
	print fft_file
	subprocess.call(["accelsearch", "-zmax", zmax, "-numharm", numharm, fft_file], shell=False)
