import numpy as np
import pandas as pd

def clean_county(filepath_u, filepath_r):
    output_1 = pd.read_stata(filepath_u)

    output_2 = pd.read_stata(filepath_r)

    output_2['unemp'] = output_2['unemp']*100

    #we want to use rural county data for any county code 999
    output_2['cofips'] = pd.Series([999 for x in range(len(output_2.index))])

    #drop indicator of small county in rural county
    output_2 = output_2.drop(columns = ['pop_lt_100k'])

    output = pd.concat([output_1, output_2])

    return output


if __name__ == "__main__":
    raise RuntimeError("This script is not intended to be run directly.")


