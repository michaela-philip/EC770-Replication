import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def summary_stats(input):
    if not isinstance(input, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    output = pd.DataFrame()

    output = input.describe().T

    output = output.drop(columns=['25%', '50%', '75%'])
    output = output.rename(columns={'count' : 'Count', 'mean': 'Mean', 'std': 'Std. Dev.', 'min': 'Min', 'max': 'Max'})
    output = output.reindex(['prenatal', 'tobacco', 'birthweight', 'lbw', 'gestation', 'eitc', 'eitcp', 'refund', 'age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc'])
    labels = {'prenatal': '1st Trimester Prenatal Care', 'tobacco': 'Smoked During Pregnancy', 'birthweight': 'Birth Weight', 'lbw': 'Birth Weight<2500 grams', 'gestation': 'Gestation Weeks', 'eitc': 'State has an EITC', 'eitcp': 'EITC percent of federal (among states with EITC)', 'refund': 'State has a refund (among states with EITC)', 'age': 'Maternal age', 'marital': 'Married', 'female': 'Female baby', 'black': 'Black', 'namer': 'Native American', 'asian': 'Asian', 'hisp': 'Hispanic', 'hseduc': 'Less than high school', 'hispmiss': 'Hispanic ethnicity missing', 'cp500': 'County pop 500,000-1,000,000', 'cp250': 'County pop 250,000-500,000', 'cp100': 'County pop 100,000-250,000', 'cpsmall': 'County pop<100,000', 'unemp': 'Unemployment', 'rpcinc': 'Real income per capital (in $1000s)', 'pctpoverty': 'Percent poverty', 'supplyMD_pc': 'Primary care physicians per 1000 females age 15-44'}
    output = output.rename(index = labels)

    return output 

def summary_table(input):
    if not isinstance(input, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    output = pd.DataFrame()

    output = input.describe().T

    output = output.drop(columns=['count', '25%', '50%', '75%'])
    output = output.rename(columns={'mean': 'Mean', 'std': 'Std. Dev.', 'min': 'Min', 'max': 'Max'})
    output = output.reindex(['prenatal', 'tobacco', 'birthweight', 'lbw', 'gestation', 'eitc', 'eitcp', 'refund', 'age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc'])

    rows_1 = ['1st Trimester Prenatal Care', 'Smoked During Pregnancy', 'Birth Weight', 'Birth Weight<2500 grams', 'Gestation Weeks', 'State has an EITC', 'EITC percent of federal (among states with EITC)', 'State has a refund (among states with EITC)', 'Maternal age', 'Married', 'Female baby', 'Black', 'Native American', 'Asian', 'Hispanic', 'Less than high school', 'Hispanic ethnicity missing', 'County pop 500,000-1,000,000', 'County pop 250,000-500,000', 'County pop 100,000-250,000', 'County pop<100,000', 'Unemployment', 'Real income per capital (in $1000s)', 'Percent poverty', 'Primary care physicians per 1000 females age 15-44']
    labels_swapped = {'1st Trimester Prenatal Care' : 'prenatal', 'Smoked During Pregnancy' : 'tobacco', 'Birth Weight' : 'birthweight', 'Birth Weight<2500 grams' : 'lbw', 'Gestation Weeks' : 'gestation', 'State has an EITC' : 'eitc', 'EITC percent of federal (among states with EITC)' : 'eitcp', 'State has a refund (among states with EITC)' : 'refund', 'Maternal age' : 'age', 'Married' : 'marital', 'Female baby' : 'female', 'Black' : 'black', 'Native American' : 'namer', 'Asian' : 'asian', 'Hispanic' : 'hisp', 'Less than high school' : 'hseduc', 'Hispanic ethnicity missing' : 'hispmiss', 'County pop 500,000-1,000,000' : 'cp500', 'County pop 250,000-500,000' : 'cp250', 'County pop 100,000-250,000' : 'cp100', 'County pop<100,000' : 'cpsmall', 'Unemployment' : 'unemp', 'Real income per capital (in $1000s)' : 'rpcinc', 'Percent poverty' : 'pctpoverty', 'Primary care physicians per 1000 females age 15-44' : 'supplyMD_pc'}
    labels = {'prenatal': '1st Trimester Prenatal Care', 'tobacco': 'Smoked During Pregnancy', 'birthweight': 'Birth Weight', 'lbw': 'Birth Weight<2500 grams', 'gestation': 'Gestation Weeks', 'eitc': 'State has an EITC', 'eitcp': 'EITC percent of federal (among states with EITC)', 'refund': 'State has a refund (among states with EITC)', 'age': 'Maternal age', 'marital': 'Married', 'female': 'Female baby', 'black': 'Black', 'namer': 'Native American', 'asian': 'Asian', 'hisp': 'Hispanic', 'hseduc': 'Less than high school', 'hispmiss': 'Hispanic ethnicity missing', 'cp500': 'County pop 500,000-1,000,000', 'cp250': 'County pop 250,000-500,000', 'cp100': 'County pop 100,000-250,000', 'cpsmall': 'County pop<100,000', 'unemp': 'Unemployment', 'rpcinc': 'Real income per capital (in $1000s)', 'pctpoverty': 'Percent poverty', 'supplyMD_pc': 'Primary care physicians per 1000 females age 15-44'}

    output = output.rename(index = labels)
    return output

if __name__ == "__main__":
    raise RuntimeError("This script is not intended to be run directly.")