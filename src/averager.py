def compute_average(infile):
	"""
	Returns the average of the data entries in the one-column file 'infile'.

	Parameters
	----------
	infile : File object
	Should be opened with 'r' permissions
	File should have a header row and all numeric values

	Notes
	-----
	Treats values in the column as floating point numbers
	"""
	import numpy
	from numpy import genfromtxt

	# take csv data in as an array
	data = genfromtxt(infile,delimiter = ',')
	data = data[1:]
	total = sum(data)
	count = len(data)
	avg = total/count
	return avg

