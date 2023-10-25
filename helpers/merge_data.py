import numpy as np
import pandas as pd

def merge_data(birth_1, birth_2, birth_3, county, eitc):
    #first we combine all the birth data
    births = pd.concat([birth_1, birth_2, birth_3])

    birth_county = pd.merge(births, county, on = ['cofips', 'stfips', 'year'], how = 'inner')

    birth_county_eitc = pd.merge(birth_county, eitc, on = ['stfips', 'year', 'numchildren'], how = 'inner')

    return birth_county_eitc

def merge_data_2(birth_1, birth_2, birth_3, county, eitc):
    #first we combine all the birth data
    births = pd.concat([birth_1, birth_2, birth_3])    

    county_eitc = pd.merge(county, eitc, on = ['stfips', 'year'], how = 'inner')

    birth_county_eitc = pd.merge(births, county_eitc, on = ['stfips', 'year', 'numchildren'], how = 'inner')

    return birth_county_eitc

if __name__ == "__main__":
    raise RuntimeError("This script is not intended to be run directly.")