   
def compute_length(infile):
    """
    Returns the length (number of rows) of the csv file.

    Parameters
    ----------
    infile : File object
        Should be opened with 'r' permissions
    """
    # Try using the csv module 
    import csv
    rows = list(csv.reader(infile))
    row_count = len(rows)
    return row_count
