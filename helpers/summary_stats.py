import numpy as np
import pandas as pd
import matplotlib as plt

def summary_table(input):
    if not isinstance(input, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    output = pd.DataFrame()

    output = input.describe().T

    output = output.drop(columns=['25%', '50%', '75%'])
    output = output.rename(columns={'count' : 'Count', 'mean': 'Mean', 'std': 'Std. Dev.', 'min': 'Min', 'max': 'Max'})
    output = output.reindex(['prenatal', 'tobacco', 'birthweight', 'lbw', 'gestation', 'eitc', 'eitcp', 'refund', 'age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc'])

    return output 

    # rows = ['1st Trimester Prenatal Care', 'Smoked During Pregnancy', 'Birth Weight', 'Birth Weight<2500 grams', 'Gestation Weeks', 'State has an EITC', 'EITC percent of federal (among states with EITC)', 'State has a refund (among states with EITC)', 'Maternal age', 'Married', 'Female baby', 'Black', 'Native American', 'Asian', 'Hispanic', 'Less than high school', 'Hispanic ethnicity missing', 'County pop 500,000-1,000,000', 'County pop 250,000-500,000', 'County pop 100,000-250,000', 'County pop<100,000', 'Unemployment', 'Real income per capital (in $1000s)', 'Percent poverty', 'Primary care physicians per 1000 females age 15-44']
    # columns = ['Mean', 'Std. Dev.', 'Min', 'Max']

    # table_1 = plt.pyplot.table(cellText = output, rowLabels = rows, colLabels = columns, loc='center')

    # print(output)



if __name__ == "__main__":
    raise RuntimeError("This script is not intended to be run directly.")