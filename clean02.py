import numpy as np
import pandas as pd 

from load02 import nat02 

#drop any twins or more
nat02 = nat02.drop(nat02[nat02['number'] > 1].index)

#age
nat02 = np.where(nat02['age'] == 99, np.nan, nat02['age'])

#race
nat02['hispmiss'] = np.where(nat02['hisp'] == 9, 1, 0)
nat02['hisp'] = np.where((nat02['hisp'] == 0) & (nat02['hisp'] == 9), 0, 1)
nat02['black'] = np.where(nat02['race'] == 2, 1, 0)
nat02['namer'] = np.where(nat02['race'] == 3, 1, 0)
nat02['asian'] = np.where(nat02['race'] > 3, 1, 0)

#education
nat02 = nat02.drop(nat02[nat02['educ'] > 3].index)
nat02['hseduc'] = np.where(nat02['educ'] < 3, 1, 0)

#marital status
nat02['marital'] = np.where(nat02['marital'] == 1, 1, np.where(nat02['marital'] == 9, np.nan, 0))

#prior children
nat02 = nat02.drop(nat02[nat02['priorchild'] == 99].index)
nat02['priorchild'] = np.where(nat02['priorchild'] > 3, 4, nat02['priorchild'])

#dummy for prenatal care in 1st trimester
nat02['prenatal'] = np.where(nat02['prenatal'] == 1, 1, np.where(nat02['prenatal'] == 5, np.nan, 0))

#gestation missing values
nat02 = nat02.drop(nat02[nat02['gestation'] == 99].index)

#sex
nat02['female'] = np.where(nat02['sex'] == 2, 1, 0)

#continuous birthweight missing values
nat02['birthweight'] = np.where(nat02['birthweight'] == 9999, np.nan, nat02['birthweight'])

#categorical birthweight
nat02['lbw'] = np.where(nat02['birthcat'] < 3, 1, np.where(nat02['birthcat'] == 4, np.nan, 0))

#tobacco use
nat02['tobacco'] = np.where(nat02['tobacco'] == 9, np.nan, nat02['tobacco'])

#county population indicators
nat02['cp500'] = np.where(nat02['countysize'] == 1, 1, 0)
nat02['cp250'] = np.where(nat02['countysize'] == 2, 1, 0)
nat02['cp100'] = np.where(nat02['countysize'] == 3, 1, 0)
nat02['cpsmall'] = np.where(nat02['countysize'] == 9, 1, 0)

#creating a conception year variable
nat02['conception_month'] = np.round(nat02['month'] - (nat02['gestation']*84/365))
nat02['conception_year'] = np.where(nat02['conception_month'] < 0, (nat02['year'] - 1), nat02['year'])

#renaming columns to make merging easier
nat02 = nat02.rename(columns={'state': 'stfips', 'county': 'cofips', 'year': 'byear', 'conception_year' : 'year', 'priorchild': 'numchildren'})

#dropping children conceived in 2000
nat02 = nat02.drop(nat02[nat02['year'] == 2000].index)

#dropping mothers under age 18
nat02 = nat02.drop(nat02[nat02['age'] < 18].index)

#dropping unneeded columns
nat2 = nat02.drop(columns = ['countysize', 'educ', 'number', 'conception_month', 'race', 'birthcat', 'sex', 'byear'])