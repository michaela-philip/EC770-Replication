import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib as plt

from helpers.ols_reg import ols_reg
from helpers.summary_stats import summary_table
from helpers.summary_stats import summary_stats

complete_data = pd.read_pickle("./complete_data.pkl")
rows = ['1st Trimester Prenatal Care', 'Smoked During Pregnancy', 'Birth Weight', 'Birth Weight<2500 grams', 'Gestation Weeks', 'State has an EITC', 'EITC percent of federal (among states with EITC)', 'State has a refund (among states with EITC)', 'Maternal age', 'Married', 'Female baby', 'Black', 'Native American', 'Asian', 'Hispanic', 'Less than high school', 'Hispanic ethnicity missing', 'County pop 500,000-1,000,000', 'County pop 250,000-500,000', 'County pop 100,000-250,000', 'County pop<100,000', 'Unemployment', 'Real income per capital (in $1000s)', 'Percent poverty', 'Primary care physicians per 1000 females age 15-44']

def main():

    table_1 = summary_stats(complete_data)
    print(table_1)

    table_2 = pd.DataFrame(index = rows)

    data = complete_data

    y_var = 'prenatal'
    x_var = ['eitc', 'age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc']
    model_2_1 = ols_reg(data, y_var, x_var)
    # print(model_2_1.summary())
    table_2['1st Trimester Prenatal Care'] = model_2_1.params
    print(table_2)

    # y_var = 'tobacco'
    # model_2_2 = ols_reg(data, y_var, x_var)
    # print(model_2_2.summary())

    # y_var = 'birthweight'
    # model_2_2 = ols_reg(data, y_var, x_var)
    # print(model_2_2.summary())

    # y_var = 'lbw'
    # model_2_3 = ols_reg(data, y_var, x_var)
    # print(model_2_3.summary())

    # y_var = 'gestation'
    # model_2_4 = ols_reg(data, y_var, x_var)
    # print(model_2_4.summary())


if __name__ == "__main__":
    print("I'm running!")
    main()