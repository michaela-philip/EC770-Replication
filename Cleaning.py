import numpy as np
import pandas as pd

from Org2 import natl2003_short

FipsDF = pd.read_csv("C:/Users/micha/OneDrive - Emory University/Second Year/Health Econ I/Replication/Data/fips2county.tsv")

#converting state abbreviations to state fips codes
StateFips = FipsDF[['StateAbbr', 'StateFIPS']] 

natl2003_short = natl2003_short.merge(StateFips, left_on = 'state', right_on = 'StateAbbr')

natl2003_short = natl2003_short.drop(columns=['StateAbbr'])

#recoding race variables
natl2003_short['black'] = np.where(natl2003_short['race'] == 2, 1, 0)

natl2003_short['natamer'] = np.where(natl2003_short['race'] == 3, 1, 0)

natl2003_short['asian'] = np.where(natl2003_short['race'] ==4, 1, 0)

#recoding hispanic variable
natl2003_short['hispanic'] = np.where(natl2003_short['hisp'] == 0, 0, np.where(natl2003_short['hisp'] == 9, 9999, 1))

#recoding marital status
natl2003_short['marital'] = np.where(natl2003_short['marital'] == 1, 1, np.where(natl2003_short['marital'] == 6, 9999, 0))

#dummy for less than high school
natl2003_short['eduhs'] = np.where(natl2003_short['educ'] < 3, 1, np.where(natl2003_short['educ'] == 6, 9999, 0))

#dummy for 1st trimester prenatal care
natl2003_short['prenat'] = np.where(natl2003_short['prenatal'] == 1, 1, np.where(natl2003_short['prenatal'] == 5, 9999, 0))

#drop any twins or more
natl2003_short = natl2003_short.drop(natl2003_short[natl2003_short['number'] > 1].index)



