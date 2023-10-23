import numpy as np
import pandas as pd

def merge_data(birth_1, birth_2, birth_3, county, eitc):
    #first we combine all the birth data
    births = pd.concat([birth_1, birth_2, birth_3])

    birth_county = pd.merge(births, county, on = ['cofips', 'stfips', 'year'], how = 'inner')

    birth_county_eitc = pd.merge(birth_county, eitc, on = ['stfips', 'year', 'numchildren'], how = 'outer')

    #changing order of columns for my sanity
    birth_county_eitc.set_index(birth_county_eitc.pop('year'), inplace=True)
    birth_county_eitc.reset_index(inplace=True)

    return birth_county_eitc

if __name__ == "__main__":
    raise RuntimeError("This script is not intended to be run directly.")