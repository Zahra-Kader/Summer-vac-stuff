#!/bin/bash
#SBATCH --time=08:00:00

source ~/.bashrc-pulsar
module load qt
#time ./do_fft.py -n0 1790 -n1 2500
time ./do_fft.py -n0 2400 -n1 2500

