import numpy as np
import csv

def compute_sum(infile):
    """
    Returns the sum of numbers in a file with one column and a header row.

    Parameters
    ----------
    infile : File object
        Should be opened with 'r' permissions

    Notes
    -----
    Treats values in the column as floating point numbers
    """
    # Try using the csv module 
