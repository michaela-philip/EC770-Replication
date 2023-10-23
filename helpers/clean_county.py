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
# filepath_u = "./inputs/county_vars.dta"
# filepath_r = "./inputs/ruralcounty_vars.dta"

# county = clean_county(filepath_u, filepath_r)

# unemp_14 = county

# county.query('unemp == 1.4')

