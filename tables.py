import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib as plt

from helpers.ols_reg import ols_reg
from helpers.summary_stats import summary_table
from helpers.summary_stats import summary_stats

complete_data = pd.read_pickle("./complete_data.pkl")
# rows = ['State has an EITC', 'Maternal age', 'Married', 'Female baby', 'Black', 'Native American', 'Asian', 'Hispanic', 'Less than high school', 'Hispanic ethnicity missing', 'County pop 500,000-1,000,000', 'County pop 250,000-500,000', 'County pop 100,000-250,000', 'County pop<100,000', 'Unemployment', 'Real income per capital (in $1000s)', 'Percent poverty', 'Primary care physicians per 1000 females age 15-44']

def main():

    table_1 = summary_stats(complete_data)
    print(table_1)
    table_1.to_csv("table_1.csv")
    print("table 1 complete")

    data = complete_data

    #table2
    y_var = 'prenatal'
    x_var = ['eitc', 'age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc']
    model_2_1 = ols_reg(data, y_var, x_var)
    data_2_1 = {'prenatal' : model_2_1.params, 'prenatal se' : model_2_1.bse}
    print(model_2_1.summary())
    table_2 = pd.DataFrame(data_2_1, index = x_var)

    y_var = 'tobacco'
    model_2_2 = ols_reg(data, y_var, x_var)
    data_2_2 = {'tobacco' : model_2_2.params, 'tobacco se' : model_2_2.bse}
    print(model_2_2.summary())
    table_2 = pd.concat([table_2, pd.DataFrame(data_2_2, index = x_var)], axis = 1)

    y_var = 'birthweight'
    model_2_3 = ols_reg(data, y_var, x_var)
    data_2_3 = {'birthweight' : model_2_3.params, 'birthweight se' : model_2_3.bse}
    print(model_2_3.summary())
    table_2 = pd.concat([table_2, pd.DataFrame(data_2_3, index = x_var)], axis = 1)

    y_var = 'lbw'
    model_2_4 = ols_reg(data, y_var, x_var)
    data_2_4 = {'lbw' : model_2_4.params, 'lbw se' : model_2_4.bse}
    print(model_2_4.summary())
    table_2 = pd.concat([table_2, pd.DataFrame(data_2_4, index = x_var)], axis = 1)

    y_var = 'gestation'
    model_2_5 = ols_reg(data, y_var, x_var)
    print(model_2_5.summary())
    data_2_5 = {'gestation' : model_2_5.params, 'gestation se' : model_2_5.bse}
    table_2 = pd.concat([table_2, pd.DataFrame(data_2_5, index = x_var)], axis = 1)

    table_2.rename(columns = {'prenatal' : '1st Trimester Prenatal Care', 'tobacco' : 'Smoked During Pregnancy', 'birthweight' : 'Birthweight', 'lbw' : 'Birth Weight<2500 grams', 'gestation' : 'Gestation Weeks'}, index = {'eitc': 'State has an EITC', 'age': 'Maternal age', 'marital': 'Married', 'female': 'Female baby', 'black': 'Black', 'namer': 'Native American', 'asian': 'Asian', 'hisp': 'Hispanic', 'hseduc': 'Less than high school', 'hispmiss': 'Hispanic ethnicity missing', 'cp500': 'County pop 500,000-1,000,000', 'cp250': 'County pop 250,000-500,000', 'cp100': 'County pop 100,000-250,000', 'cpsmall': 'County pop<100,000', 'unemp': 'Unemployment', 'rpcinc': 'Real income per capital (in $1000s)', 'pctpoverty': 'Percent poverty', 'supplyMD_pc': 'Primary care physicians per 1000 females age 15-44'}, inplace = True)
    # print(table_2)
    table_2.to_csv("table_2.csv")
    print("table 2 complete")

    #table 3
    y_var = 'prenatal'
    x_var = ['eitcp', 'age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc']
    model_3_1 = ols_reg(data, y_var, x_var)
    print(model_3_1.summary())
    data_3_1 = {'prenatal' : model_3_1.params, 'prenatal se' : model_3_1.bse}
    table_3 = pd.DataFrame(data_3_1, index = x_var)

    y_var = 'tobacco'
    model_3_2 = ols_reg(data, y_var, x_var)
    print(model_3_2.summary())
    data_3_2 = {'tobacco' : model_3_2.params, 'tobacco se' : model_3_2.bse}
    table_3 = pd.concat([table_3, pd.DataFrame(data_3_2, index = x_var)], axis = 1)

    y_var = 'birthweight'
    model_3_3 = ols_reg(data, y_var, x_var)
    print(model_3_3.summary())
    data_3_3 = {'birthweight' : model_3_3.params, 'birthweight se' : model_3_3.bse}
    table_3 = pd.concat([table_3, pd.DataFrame(data_3_3, index = x_var)], axis = 1)

    y_var = 'lbw'
    model_3_4 = ols_reg(data, y_var, x_var)
    print(model_3_4.summary())
    data_3_4 = {'lbw' : model_3_4.params, 'lbw se' : model_3_4.bse}
    table_3 = pd.concat([table_3, pd.DataFrame(data_3_4, index = x_var)], axis = 1)

    y_var = 'gestation'
    model_3_5 = ols_reg(data, y_var, x_var)
    print(model_3_5.summary())
    data_3_5 = {'gestation' : model_3_5.params, 'gestation se' : model_3_5.bse}
    table_3 = pd.concat([table_3, pd.DataFrame(data_3_5, index = x_var)], axis = 1)

    table_3.rename(columns = {'prenatal' : '1st Trimester Prenatal Care', 'tobacco' : 'Smoked During Pregnancy', 'birthweight' : 'Birthweight', 'lbw' : 'Birth Weight<2500 grams', 'gestation' : 'Gestation Weeks'}, index = {'eitcp': 'EITC percent of federal (among states with EITC)', 'age': 'Maternal age', 'marital': 'Married', 'female': 'Female baby', 'black': 'Black', 'namer': 'Native American', 'asian': 'Asian', 'hisp': 'Hispanic', 'hseduc': 'Less than high school', 'hispmiss': 'Hispanic ethnicity missing', 'cp500': 'County pop 500,000-1,000,000', 'cp250': 'County pop 250,000-500,000', 'cp100': 'County pop 100,000-250,000', 'cpsmall': 'County pop<100,000', 'unemp': 'Unemployment', 'rpcinc': 'Real income per capital (in $1000s)', 'pctpoverty': 'Percent poverty', 'supplyMD_pc': 'Primary care physicians per 1000 females age 15-44'}, inplace = True)
    # print(table_3)
    table_3.to_csv("table_3.csv")
    print("table 3 complete")

if __name__ == "__main__":
    print("I'm running!")
    main()