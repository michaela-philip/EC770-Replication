import numpy as np
import pandas as pd

from Org2 import natl2003_short

FipsDF = pd.read_csv("C:/Users/micha/OneDrive - Emory University/Second Year/Health Econ I/Replication/Data/fips2county.tsv")

#converting state abbreviations to state fips codes
StateFips = FipsDF[['StateAbbr', 'StateFIPS']] 

natl2003 = natl2003.merge(StateFips, left_on = 'state', right_on = 'StateAbbr')

natl2003 = natl2003.drop(columns=['StateAbbr'])

#recoding race variables
natl2003['black'] = np.where(natl2003['race'] == 2, 1, 0)

natl2003['natamer'] = np.where(natl2003['race'] == 3, 1, 0)

natl2003['asian'] = np.where(natl2003['race'] ==4, 1, 0)

#recoding hispanic variable
natl2003['hispanic'] = np.where(natl2003['hisp'] == 0, 0, np.where(natl2003['hisp'] == 9, 9999, 1))

#recoding marital status
natl2003['marital'] = np.where(natl2003['marital'] == 1, 1, np.where(natl2003['marital'] == 6, 9999, 0))

#dummy for less than high school
natl2003['eduhs'] = np.where(natl2003['educ'] < 3, 1, np.where(natl2003['educ'] == 6, 9999, 0))

#dummy for 1st trimester prenatal care
natl2003['prenat'] = np.where(natl2003['prenatal'] == 1, 1, np.where(natl2003['prenatal'] == 5, 9999, 0))

#drop any twins or more
natl2003 = natl2003.drop(natl2003[natl2003['number'] > 1].index)



