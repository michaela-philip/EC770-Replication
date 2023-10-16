import numpy as np
import pandas as pd

#we want to merge county characteristics with our birth data

from MinClean import s_births

from Organization import county

birth_county = pd.merge(s_births, county, on = ['cofips', 'stfips', 'year'], how = 'left')