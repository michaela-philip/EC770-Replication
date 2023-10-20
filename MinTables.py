import numpy as np
import pandas as pd

#create table of summary statistics

from MinMerge import s_birth_county_eitc 

s_birth_county_eitc.describe()

s_sumstats = pd.DataFrame()

s_sumstats.columns = ['Variables', 'Mean', 'Std. Dev', 'Min', 'Max']

