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
    # Just for fun, try not using use the csv module here
