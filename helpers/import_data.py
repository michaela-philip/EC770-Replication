import numpy as np
import pandas as pd

def import_data(filepath, colspecs, columns, dropcols, limit):
    output = pd.read_fwf( filepath, colspecs = colspecs, header = None, nrows=limit)
    output.columns = columns
    output = output.drop(columns=dropcols)

    return output

if __name__ == "__main__":
    raise RuntimeError("This script is not intended to be run directly.")