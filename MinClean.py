import numpy as np
import pandas as pd

from Minimal import natl2001_s
from Minimal import natl2002_s
from Minimal import natl2003_s

#drop any twins or more
natl2003_s = natl2003_s.drop(natl2003_s[natl2003_s['number'] > 1].index)

#combine 2001 and 2002 to clean together since they are identical
s_0102 = pd.concat([natl2001_s, natl2002_s])

##### cleaning 2001-2002 #####

#race
s_0102['hispanic'] = np.where(s_0102['hisp'] == 0, 0, np.where(s_0102['hisp'] == 9, 9999, 1))
s_0102['black'] = np.where(s_0102['race'] == 2, 1, 0)
s_0102['namer'] = np.where(s_0102['race'] == 3, 1, 0)
s_0102['asian'] = np.where(s_0102['race'] > 3, 1, 0)

#education
s_0102['eduhs'] = np.where(s_0102['educ'] < 3, 1, np.where(s_0102['educ'] == 6, 9999, 0))

#marital status
s_0102['married'] = np.where(s_0102['marital'] == 1, 1, np.where(s_0102['marital'] == 9, 9999, 0))

#dummy for prenatal care in 1st trimester
s_0102['prenat'] = np.where(s_0102['prenatal'] == 1, 1, np.where(s_0102['prenatal'] == 5, 9999, 0))




##### cleaning 2003 #####
#converting state abbreviations to state fips codes
FipsDF = pd.read_csv("C:/Users/micha/OneDrive - Emory University/Second Year/Health Econ I/Replication/Data/fips2county.tsv")
StateFips = FipsDF[['StateAbbr', 'StateFIPS']] 
natl2003_s = natl2003_s.merge(StateFips, left_on = 'state', right_on = 'StateAbbr')
natl2003_s = natl2003_s.drop(columns=['StateAbbr'])

#recoding race variables
natl2003_s['black'] = np.where(natl2003_s['race'] == 2, 1, 0)
natl2003_s['natamer'] = np.where(natl2003_s['race'] == 3, 1, 0)
natl2003_s['asian'] = np.where(natl2003_s['race'] ==4, 1, 0)

#recoding hispanic variable
natl2003_s['hispanic'] = np.where(natl2003_s['hisp'] == 0, 0, np.where(natl2003_s['hisp'] == 9, 9999, 1))

#recoding marital status
natl2003_s['married'] = np.where(natl2003_s['marital'] == 1, 1, np.where(natl2003_s['marital'] == 6, 9999, 0))

#dummy for less than high school
natl2003_s['eduhs'] = np.where(natl2003_s['educ'] < 3, 1, np.where(natl2003_s['educ'] == 6, 9999, 0))

#dummy for 1st trimester prenatal care
natl2003_s['prenat'] = np.where(natl2003_s['prenatal'] == 1, 1, np.where(natl2003_s['prenatal'] == 5, 9999, 0))

