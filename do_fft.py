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

parser = argparse.ArgumentParser(description='Do FFT with PRESTO')
parser.add_argument('-n0', '--num_1st', metavar='Number of the 1st file name', nargs='+', required=True, help='Number of the 1st file name')
parser.add_argument('-n1', '--num_last', metavar='Number of the last file name', nargs='+', required=True, help='Number of the last file name')

args = parser.parse_args()

n0 = int(args.num_1st[0])
n1 = int(args.num_last[0])


#################################################################
# realfft
all_files = sorted(glob.glob("*.dat"))
for i in np.arange(n0,n1):
	dat_file = all_files[i]
	print dat_file
	subprocess.call(["realfft", "-fwd", dat_file], shell=False)

