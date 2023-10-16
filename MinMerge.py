import numpy as np
import pandas as pd

#we want to merge county characteristics with our birth data

from MinClean import s_births

from Organization import county

birth_county = pd.merge(s_births, county, on = ['cofips', 'stfips', 'year'], how = 'outer')

#now we add eitc

from Organization import eitc

birth_county_eitc = pd.merge(birth_county, eitc, on = ['stfips', 'year', 'numchildren'], how = 'outer')

#changing order of columns for my sanity
birth_county_eitc.set_index(birth_county_eitc.pop('year'), inplace=True)
birth_county_eitc.reset_index(inplace=True)