import numpy as np
import pandas as pd

from load03 import nat03

#dropping any twins or more
nat03 = nat03.drop(nat03[nat03['number'] > 1].index)

#converting state abbreviations to state fips codes
FipsDF = pd.read_csv("C:/Users/micha/OneDrive - Emory University/Second Year/Health Econ I/Replication/Data/fips2county.tsv", delimiter = "\t")
StateFips = FipsDF[['StateAbbr', 'StateFIPS']] 
nat03 = nat03.merge(StateFips, left_on = 'state', right_on = 'StateAbbr')
nat03['state'] = nat03['StateFIPS']
nat03 = nat03.drop(columns=['StateAbbr', 'StateFIPS'])

#age
nat03['age'] = np.where(nat03['age'] == 99, np.nan, nat03['age'])

#race
nat03['hispmiss'] = np.where(nat03['hisp'] == 9, 1, 0)
nat03['hisp'] = np.where((nat03['hisp'] == 0) & (nat03['hisp'] == 9), 0, 1)
nat03['black'] = np.where(nat03['race'] == 2, 1, 0)
nat03['namer'] = np.where(nat03['race'] == 3, 1, 0)
nat03['asian'] = np.where(nat03['race'] == 4, 1, 0)

#education
nat03 = nat03.drop(nat03[nat03['educ'] > 3].index)
nat03['hseduc'] = np.where(nat03['educ'] < 3, 1, 0)

#marital status
nat03['marital'] = np.where(nat03['marital'] == 1, 1, np.where(nat03['marital'] == 9, np.nan, 0))

#prior children
nat03 = nat03.drop(nat03[nat03['priorchild'] == 99].index)
nat03['priorchild'] = np.where(nat03['priorchild'] > 3, 4, nat03['priorchild'])

#dummy for prenatal care in 1st trimester
nat03['prenatal'] = np.where(nat03['prenatal'] == 1, 1, np.where(nat03['prenatal'] == 5, np.nan, 0))

#gestation missing values
nat03['gestation'] = np.where(nat03['gestation'] == 99, np.nan, nat03['gestation'])

#sex
nat03['female'] = np.where(nat03['sex'] == 'F', 1, 0)

#continuous birthweight missing values
nat03['birthweight'] = np.where(nat03['birthweight'] == 9999, np.nan, nat03['birthweight'])

#categorical birthweight
nat03['lbw'] = np.where(nat03['birthcat'] < 3, 1, np.where(nat03['birthcat'] == 4, np.nan, 0))

#tobacco use
nat03['tobacco'] = np.where(nat03['tobacco'] == 9, np.nan, nat03['tobacco'])

#county population indicators
nat03['cp500'] = np.where(nat03['countysize'] == 1, 1, 0)
nat03['cp250'] = np.where(nat03['countysize'] == 2, 1, 0)
nat03['cp100'] = np.where(nat03['countysize'] == 3, 1, 0)
nat03['cpsmall'] = np.where(nat03['countysize'] == 9, 1, 0)

#creating a conception year variable
nat03['conception_month'] = np.round(nat03['month'] - (nat03['gestation']*84/365))
nat03['conception_year'] = np.where(nat03['conception_month'] < 0, (nat03['year'] - 1), nat03['year'])

#renaming columns to make merging easier
nat03 = nat03.rename(columns={'state': 'stfips', 'county': 'cofips', 'year': 'byear', 'conception_year' : 'year', 'priorchild': 'numchildren'})

#dropping children conceived in 2000
nat03 = nat03.drop(nat03[nat03['year'] == 2000].index)

#dropping mothers under age 18
nat03 = nat03.drop(nat03[nat03['age'] < 18].index)

#dropping unneeded columns
nat3 = nat03.drop(columns = ['countysize', 'educ', 'number', 'conception_month', 'race', 'birthcat', 'sex', 'byear'])