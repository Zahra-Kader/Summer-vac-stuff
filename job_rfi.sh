#!/bin/bash
#SBATCH --time=15:00:00
#SBATCH --ntasks-per-node=10

source ~/.bashrc-pulsar
module load qt
time ./rfi_mask.py -f beam01.fil -time 20.0 -timesig 10.0 -freqsig 4.0 -clip 6.0

