import numpy as np
import pandas as pd 

from load01 import nat01 

#drop any twins or more
nat01 = nat01.drop(nat01[nat01['number'] > 1].index)

#race
nat01['hispmiss'] = np.where(nat01['hisp'] == 9, 1, 0)
nat01['hisp'] = np.where((nat01['hisp'] == 0) & (nat01['hisp'] == 9), 0, 1)
nat01['black'] = np.where(nat01['race'] == 2, 1, 0)
nat01['namer'] = np.where(nat01['race'] == 3, 1, 0)
nat01['asian'] = np.where(nat01['race'] > 3, 1, 0)

#education
nat01['educ'] = nat01.drop(nat01[nat01['educ'] > 3].index)
nat01['hseduc'] = np.where(nat01['educ'] < 3, 1, 0)

#marital status
nat01['marital'] = np.where(nat01['marital'] == 1, 1, np.where(nat01['marital'] == 9, np.nan, 0))

#prior children
nat01 = nat01.drop(nat01[nat01['priorchild'] == 99].index)
nat01['priorchild'] = np.where(nat01['priorchild'] > 3, 4, nat01['priorchild'])

#dummy for prenatal care in 1st trimester
nat01['prenatal'] = np.where(nat01['prenatal'] == 1, 1, np.where(nat01['[prenatal'] == 5, np.nan, 0))

#gestation missing values
nat01 = nat01.drop(nat01[nat01['gestation'] == 99].index)

#sex
nat01['female'] = np.where(nat01['sex'] == 2, 1, 0)

#continuous birthweight missing values
nat01['birthweight'] = np.where(nat01['birthweight'] == 9999, np.nan, nat01['birthweight'])

#categorical birthweight
nat01['lbw'] = np.where(nat01['birthcat'] < 3, 1, np.where(nat01['birthcat'] == 4, np.nan, 0))

#tobacco use
nat01['tobacco'] = np.where(nat01['tobacco'] == 9, np.nan, nat01['tobacco'])

#county population indicators
nat01['cp500'] = np.where(nat01['countysize'] == 1, 1, 0)
nat01['cp250'] = np.where(nat01['countysize'] == 2, 1, 0)
nat01['cp100'] = np.where(nat01['countysize'] == 3, 1, 0)
nat01['cpsmall'] = np.where(nat01['countysize'] == 9, 1, 0)

#creating a conception year variable
nat01['conception_month'] = np.round(nat01['month'] - (nat01['gestation']*84/365))
nat01['conception_year'] = np.where(nat01['conception_month'] < 0, (nat01['year'] - 1), nat01['year'])

#renaming columns to make merging easier
nat01 = nat01.rename(columns={'state': 'stfips', 'county': 'cofips', 'year': 'byear', 'conception_year' : 'year', 'priorchild': 'numchildren'})

#dropping children conceived in 2000
nat01 = nat01.drop(nat01[nat01['year'] == 2000].index)

#dropping mothers under age 18
nat01 = nat01.drop(nat01[nat01['age'] < 18].index)

#dropping unneeded columns
nat1 = nat01.drop(columns = ['countysize', 'educ', 'number', 'conception_month', 'race', 'birthcat', 'sex', 'byear'])