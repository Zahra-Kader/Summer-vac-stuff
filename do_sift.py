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
#rc('text', usetex=True)

#################################################################
# ACCEL_sift > candlist
candlist = 'candlist.txt'
proc = subprocess.Popen(['python', '/pulsar/psr/software/current/src/workspace/psr-presto-build/label/jessie/presto/python/ACCEL_sift.py'], shell=False, stdout=subprocess.PIPE)
f = open(candlist, 'w')
f.write(proc.stdout.read())
f.close()

