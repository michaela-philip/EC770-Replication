import numpy as np
import pandas as pd

#create table of summary statistics

from MinMerge import s_birth_county_eitc 

s_sumstats = s_birth_county_eitc.describe().T

s_sumstats = s_sumstats.drop(columns=['count', '25%', '50%', '75%'])

s_sumstats = s_sumstats.rename(columns={'mean': 'Mean', 'std': 'Std. Dev.', 'min': 'Min', 'max': 'Max'})

s_sumstats = s_sumstats.drop(labels = ['year', 'stfips', 'cofips', 'month', 'eitc_pct', 'birthcat'])

print(s_sumstats)

s_sumstats = s_sumstats.reindex(['prenatal', 'tobacco', 'birthweight', 'lbw', 'gestation', 'eitc', 'eitcp', 'refund', 'age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc'])