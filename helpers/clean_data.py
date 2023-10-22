import numpy as np
import pandas as pd

def convert_to_fips(state_column):
    FipsDF = pd.read_csv("./data/fips2county.tsv", delimiter = "\t")
    StateFips = FipsDF[['StateAbbr', 'StateFIPS']] 
    output = state_column.merge(StateFips, left_on = 'state', right_on = 'StateAbbr')
    output['state'] = output['StateFIPS']
    output = output.drop(columns=['StateAbbr', 'StateFIPS'])
    return output

def clean_data(input):
    if not isinstance(input, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    output = pd.DataFrame()

    #drop any twins or more
    output = input.drop(input[input['number'] > 1].index)

    #age
    output['age'] = np.where(output['age'] == 99, np.nan, output['age'])

    #race
    output['hispmiss'] = np.where(output['hisp'] == 9, 1, 0)
    output['hisp'] = np.where((output['hisp'] == 0) & (output['hisp'] == 9), 0, 1)
    output['black'] = np.where(output['race'] == 2, 1, 0)
    output['namer'] = np.where(output['race'] == 3, 1, 0)
    output['asian'] = np.where(output['race'] > 3, 1, 0)

    #education
    output = output.drop(output[output['educ'] > 3].index)
    output['hseduc'] = np.where(output['educ'] < 3, 1, 0)

    #marital status
    output['marital'] = np.where(output['marital'] == 1, 1, np.where(output['marital'] == 9, np.nan, 0))

    #prior children
    output = output.drop(output[output['priorchild'] == 99].index)
    output['priorchild'] = np.where(output['priorchild'] > 3, 4, output['priorchild'])

    #dummy for prenatal care in 1st trimester
    output['prenatal'] = np.where(output['prenatal'] == 1, 1, np.where(output['prenatal'] == 5, np.nan, 0))

    #gestation missing values
    output = output.drop(output[output['gestation'] == 99].index)

    #sex
    output['female'] = np.where(output['sex'] == 2, 1, 0)

    #continuous birthweight missing values
    output['birthweight'] = np.where(output['birthweight'] == 9999, np.nan, output['birthweight'])

    #categorical birthweight
    output['lbw'] = np.where(output['birthcat'] < 3, 1, np.where(output['birthcat'] == 4, np.nan, 0))

    #tobacco use
    output['tobacco'] = np.where(output['tobacco'] == 9, np.nan, output['tobacco'])
    output['tobacco'] = np.where(output['tobacco'] == 1, 1, 0)

    #county population indicators
    output['cp500'] = np.where(output['countysize'] == 1, 1, 0)
    output['cp250'] = np.where(output['countysize'] == 2, 1, 0)
    output['cp100'] = np.where(output['countysize'] == 3, 1, 0)
    output['cpsmall'] = np.where(output['countysize'] == 9, 1, 0)

    #creating a conception year variable
    output['conception_month'] = np.round(output['month'] - (output['gestation']*84/365))
    output['conception_year'] = np.where(output['conception_month'] < 0, (output['year'] - 1), output['year'])

    #renaming columns to make merging easier
    output = output.rename(columns={'state': 'stfips', 'county': 'cofips', 'year': 'byear', 'conception_year' : 'year', 'priorchild': 'numchildren'})

    #dropping children conceived in 2000
    output = output.drop(output[output['year'] == 2000].index)

    #dropping mothers under age 18
    output = output.drop(output[output['age'] < 18].index)

    #converting state to fips
    if output['state'].dtype == 'object':
        output['state'] = convert_to_fips(output)

    #dropping unneeded columns
    output = output.drop(columns = ['countysize', 'educ', 'number', 'conception_month', 'race', 'birthcat', 'sex', 'byear'])

if __name__ == "__main__":
    print("[CLEAN_DATA]\t","I've been called directly")
    print("[CLEAN_DATA]\t",__name__)
    raise RuntimeError("This script is not meant to be run directly")
