import csv
import os
from homework_1p5_team_2.src import averager, maximum, minimum, data_length, summer




datadir = '../data'
infilename = os.path.join(datadir, 'data.csv')

###############################################################################
## Compute averages
###############################################################################

infile = open(infilename, 'r')

# Students write this function in a separate file called averager.py
print averager.compute_average(infile)

infile.close()


###############################################################################
## Get the maximum
###############################################################################
infile = open(infilename, 'r')

print maximum.compute_maximum(infile)

infile.close()


###############################################################################
## Get the minimum
###############################################################################
infile = open(infilename, 'r')

print minimum.compute_minimum(infile)

infile.close()


###############################################################################
## Get the length
###############################################################################
infile = open(infilename, 'r')

print data_length.compute_length(infile)

infile.close()


###############################################################################
## Get the sum
###############################################################################
infile = open(infilename, 'r')

print summer.compute_sum(infile)

infile.close()






