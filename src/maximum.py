import numpy as np
import csv

def compute_maximum(infile):
    """
    Returns the maximum number in a file with one column and a header row.

    Parameters
    ----------
    infile : File object
        Should be opened with 'r' permissions
        File should have a header row and all numeric values
    
    Notes
    -----
    Treats values in the column as floating point numbers
    """
    # Try using the csv module 
