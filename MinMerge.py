import numpy as np
import pandas as pd

#we want to merge county characteristics with our birth data

from MinClean import s_births

from Organization import county

s_birth_county = pd.merge(s_births, county, on = ['cofips', 'stfips', 'year'], how = 'outer')

#now we add eitc

from Organization import eitc

s_birth_county_eitc = pd.merge(s_birth_county, eitc, on = ['stfips', 'year', 'numchildren'], how = 'outer')

#changing order of columns for my sanity
s_birth_county_eitc.set_index(s_birth_county_eitc.pop('year'), inplace=True)
s_birth_county_eitc.reset_index(inplace=True)