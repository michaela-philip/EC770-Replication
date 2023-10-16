import numpy as np
import pandas as pd

from clean01 import nat1
from clean02 import nat2
from clean03 import nat3

#first we combine all the birth data
births = pd.concat([nat1, nat2, nat3])

from Organization import county

birth_county = pd.merge(births, county, on = ['cofips', 'stfips', 'year'], how = 'outer')

#now we add eitc

from Organization import eitc

birth_county_eitc = pd.merge(birth_county, eitc, on = ['stfips', 'year', 'numchildren'], how = 'outer')

#changing order of columns for my sanity
birth_county_eitc.set_index(birth_county_eitc.pop('year'), inplace=True)
birth_county_eitc.reset_index(inplace=True)