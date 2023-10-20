import numpy as np
import pandas as pd 

from Minimal import natl2001_s
from Minimal import natl2002_s
from Minimal import natl2003_s

#drop any twins or more
natl2001_s = natl2001_s.drop(natl2001_s[natl2001_s['number'] > 1].index)
natl2002_s = natl2002_s.drop(natl2002_s[natl2002_s['number'] > 1].index)
natl2003_s = natl2003_s.drop(natl2003_s[natl2003_s['number'] > 1].index)

#combine 2001 and 2002 to clean together since they are identical
s_0102 = pd.concat([natl2001_s, natl2002_s])

##### cleaning 2001-2002 #####

#age
s_0102 = np.where(s_0102['age'] == 99, np.nan, s_0102['age'])

#race
s_0102['hispmiss'] = np.where(s_0102['hisp'] == 9, 1, 0)
s_0102['hisp'] = np.where((s_0102['hisp'] == 0) & (s_0102['hisp'] == 9), 0, 1)
s_0102['black'] = np.where(s_0102['race'] == 2, 1, 0)
s_0102['namer'] = np.where(s_0102['race'] == 3, 1, 0)
s_0102['asian'] = np.where(s_0102['race'] > 3, 1, 0)

#education
s_0102 = s_0102.drop(s_0102[s_0102['educ'] > 3].index)
s_0102['hseduc'] = np.where(s_0102['educ'] < 3, 1, 0)

#marital status
s_0102['marital'] = np.where(s_0102['marital'] == 1, 1, np.where(s_0102['marital'] == 9, np.nan, 0))

#prior children
s_0102 = s_0102.drop(s_0102[s_0102['priorchild'] == 99].index)
s_0102['priorchild'] = np.where(s_0102['priorchild'] > 3, 4, s_0102['priorchild'])

#dummy for prenatal care in 1st trimester
s_0102['prenatal'] = np.where(s_0102['prenatal'] == 1, 1, np.where(s_0102['prenatal'] == 5, np.nan, 0))

#gestation missing values
s_0102 = s_0102.drop(s_0102[s_0102['gestation'] == 99].index)

#sex
s_0102['female'] = np.where(s_0102['sex'] == 2, 1, 0)

#continuous birthweight missing values
s_0102['birthweight'] = np.where(s_0102['birthweight'] == 9999, np.nan, s_0102['birthweight'])

#categorical birthweight
s_0102['lbw'] = np.where(s_0102['birthcat'] < 3, 1, np.where(s_0102['birthcat'] == 4, np.nan, 0))

#tobacco use
s_0102['tobacco'] = np.where(s_0102['tobacco'] == 9, np.nan, s_0102['tobacco'])

#county population indicators
s_0102['cp500'] = np.where(s_0102['countysize'] == 1, 1, 0)
s_0102['cp250'] = np.where(s_0102['countysize'] == 2, 1, 0)
s_0102['cp100'] = np.where(s_0102['countysize'] == 3, 1, 0)
s_0102['cpsmall'] = np.where(s_0102['countysize'] == 9, 1, 0)



##### cleaning 2003 #####
#converting state abbreviations to state fips codes
FipsDF = pd.read_csv("C:/Users/micha/OneDrive - Emory University/Second Year/Health Econ I/Replication/Data/fips2county.tsv", delimiter = "\t")
StateFips = FipsDF[['StateAbbr', 'StateFIPS']] 
natl2003_s = natl2003_s.merge(StateFips, left_on = 'state', right_on = 'StateAbbr')
natl2003_s['state'] = natl2003_s['StateFIPS']
s_03 = natl2003_s.drop(columns=['StateAbbr', 'StateFIPS'])

#age
s_03 = np.where(s_03['age'] == 99, np.nan, s_03['age'])

#race
s_03['hispmiss'] = np.where(s_03['hisp'] == 9, 1, 0)
s_03['hisp'] = np.where(s_03['hisp'] == 0, 0, np.where(s_03['hisp'] == 9, np.nan, 1))
s_03['black'] = np.where(s_03['race'] == 2, 1, 0)
s_03['namer'] = np.where(s_03['race'] == 3, 1, 0)
s_03['asian'] = np.where(s_03['race'] == 4, 1, 0)

#education
s_03 = s_03.drop(s_03[s_03['educ'] > 3].index)
s_03['hseduc'] = np.where(s_03['educ'] < 3, 1, 0)

#marital status
s_03['marital'] = np.where(s_03['marital'] == 1, 1, np.where(s_03['marital'] == 9, np.nan, 0))

#prior children
s_03 = s_03.drop(s_03[s_03['priorchild'] == 99].index)
s_03['priorchild'] = np.where(s_03['priorchild'] > 3, 4, s_03['priorchild'])

#dummy for prenatal care in 1st trimester
s_03['prenatal'] = np.where(s_03['prenatal'] == 1, 1, np.where(s_03['prenatal'] == 5, np.nan, 0))

#gestation missing values
s_03['gestation'] = np.where(s_03['gestation'] == 99, np.nan, s_03['gestation'])

#sex
s_03['female'] = np.where(s_03['sex'] == 'F', 1, 0)

#continuous birthweight missing values
s_03['birthweight'] = np.where(s_03['birthweight'] == 9999, np.nan, s_03['birthweight'])

#categorical birthweight
s_03['lbw'] = np.where(s_03['birthcat'] < 3, 1, np.where(s_03['birthcat'] == 4, np.nan, 0))

#tobacco use
s_03['tobacco'] = np.where(s_03['tobacco'] == 9, np.nan, s_03['tobacco'])

#county population indicators
s_03['cp500'] = np.where(s_03['countysize'] == 1, 1, 0)
s_03['cp250'] = np.where(s_03['countysize'] == 2, 1, 0)
s_03['cp100'] = np.where(s_03['countysize'] == 3, 1, 0)
s_03['cpsmall'] = np.where(s_03['countysize'] == 9, 1, 0)

#combine all three years
s_births = pd.concat([s_0102, s_03])

#creating a conception year variable
s_births['conception_month'] = np.round(s_births['month'] - (s_births['gestation']*84/365))
s_births['conception_year'] = np.where(s_births['conception_month'] < 0, (s_births['year'] - 1), s_births['year'])

#renaming columns to make merging easier
s_births = s_births.rename(columns={'state': 'stfips', 'county': 'cofips', 'year': 'byear', 'conception_year' : 'year', 'priorchild': 'numchildren'})

#dropping children conceived in 2000
s_births = s_births.drop(s_births[s_births['year'] == 2000].index)

#dropping mothers under age 18
s_births = s_births.drop(s_births[s_births['age'] < 18].index)

#dropping unneeded columns
s_births = s_births.drop(columns = ['countysize', 'educ', 'number', 'conception_month', 'race', 'birthcat', 'sex', 'byear'])