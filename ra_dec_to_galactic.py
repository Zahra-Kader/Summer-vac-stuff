# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 22:54:42 2018

@author: KaderF
"""

from astropy import units as u
from astropy.coordinates import SkyCoord
c_icrs = SkyCoord(ra=163.5000*u.degree, dec= -21.3500*u.degree, frame='icrs')
print c_icrs.galactic  