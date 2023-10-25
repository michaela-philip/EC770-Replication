import numpy as np
import pandas as pd

# def convert_to_fips(state_column):
#     FipsDF = pd.read_csv("./data/fips2county.tsv", delimiter = "\t")
#     StateFips = FipsDF[['StateAbbr', 'StateFIPS']] 
#     output = state_column.merge(StateFips, left_on = 'state', right_on = 'StateAbbr')
#     output['state'] = output['StateFIPS']
#     output = output.drop(columns=['StateAbbr', 'StateFIPS'])
#     return output

def clean_data(input):
    if not isinstance(input, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    output = pd.DataFrame()

    #drop any twins or more
    output = input.drop(input[input['number'] > 1].index)

    #prior children
    output = output.drop(output[output['priorchild'] == 99].index)
    output['priorchild'] = np.where(output['priorchild'] > 3, 4, output['priorchild'])

    #education
    output = output.drop(output[output['educ'] > 3].index)
    output['hseduc'] = np.where(output['educ'] < 3, 1, 0)

    #gestation missing values
    output = output.drop(output[output['gestation'] == 99].index)

    #dropping mothers under age 18
    output = output.drop(output[output['age'] < 18].index)

    #creating a conception year variable
    output['conception_month'] = np.round(output['month'] - (output['gestation']*84/365))
    output['conception_year'] = np.where(output['conception_month'] < 0, (output['year'] - 1), output['year'])

    #renaming columns to make merging easier
    output = output.rename(columns={'state': 'stfips', 'county': 'cofips', 'year': 'byear', 'conception_year' : 'year', 'priorchild': 'numchildren'})

    #dropping children conceived in 2000
    output = output.drop(output[output['year'] == 2000].index)

    #dropping unneeded columns
    output = output.drop(columns = ['conception_month', 'byear'])

    #age
    #output['age'] = np.where(output['age'] == 99, np.nan, output['age'])

    #race
    output['hispmiss'] = np.where(output['hisp'] == 9, 1, 0)
    output['hisp'] = np.where((output['hisp'] == 0) | (output['hisp'] == 9), 0, 1)
    output['black'] = np.where(output['race'] == 2, 1, 0)
    output['namer'] = np.where(output['race'] == 3, 1, 0)
    output['asian'] = np.where(output['race'] > 3, 1, 0)

    #marital status
    output['marital'] = np.where(output['marital'] == 1, 1, np.where(output['marital'] == 9, np.nan, 0))

    #dummy for prenatal care in 1st trimester
    output['prenatal'] = np.where(output['prenatal'] == 1, 1, np.where(output['prenatal'] == 5, np.nan, 0))

    #sex
    if output['sex'].dtype == 'object':
        output['female'] = np.where(output['sex'] == 'F', 1, 0)
    else:
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

    #dropping unneeded columns
    output = output.drop(columns = ['countysize', 'educ', 'number', 'race', 'birthcat', 'sex'])

    return output 

state_abbrev_fips_dict = { 'AL': '01', 'AK': '02', 'AZ': '04', 'AR': '05', 'CA': '06', 'CO': '08', 'CT': '09', 'DE': '10', 'FL': '12', 'GA': '13', 'HI': '15', 'ID': '16', 'IL': '17', 'IN': '18', 'IA': '19', 'KS': '20', 'KY': '21', 'LA': '22', 'ME': '23', 'MD': '24', 'MA': '25', 'MI': '26', 'MN': '27', 'MS': '28', 'MO': '29', 'MT': '30', 'NE': '31', 'NV': '32', 'NH': '33', 'NJ': '34', 'NM': '35', 'NY': '36', 'NC': '37', 'ND': '38', 'OH': '39', 'OK': '40', 'OR': '41', 'PA': '42', 'RI': '44', 'SC': '45', 'SD': '46', 'TN': '47', 'TX': '48', 'UT': '49', 'VT': '50', 'VA': '51', 'WA': '53', 'WV': '54', 'WI': '55', 'WY': '56', 'AS': '60', 'GU': '66', 'MP': '69', 'PR': '72', 'VI': '78'}

if __name__ == "__main__":
    print("[CLEAN_DATA]\t","I've been called directly")
    print("[CLEAN_DATA]\t",__name__)
    raise RuntimeError("This script is not meant to be run directly")
