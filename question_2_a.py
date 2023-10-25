import numpy as np
import pandas as pd

from ols_reg import ols_reg 

def main():

    #table 4
    data = pd.read_pickle("./complete_data.pkl")

    y_var = 'prenatal'
    x_var = ['eitcp', 'refund', 'age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc']
    model_4_1 = ols_reg(data, y_var, x_var)
    print(model_4_1.summary())
    data_4_1 = {'prenatal' : model_4_1.params, 'prenatal se' : model_4_1.bse}
    table_4 = pd.DataFrame(data_4_1, index = x_var)

    y_var = 'tobacco'
    model_4_2 = ols_reg(data, y_var, x_var)
    print(model_4_2.summary())
    data_4_2 = {'tobacco' : model_4_2.params, 'tobacco se' : model_4_2.bse}
    table_4 = pd.concat([table_4, pd.DataFrame(data_4_2, index = x_var)], axis = 1)

    y_var = 'birthweight'
    model_4_3 = ols_reg(data, y_var, x_var)
    print(model_3_3.summary())
    data_4_3 = {'birthweight' : model_4_3.params, 'birthweight se' : model_4_3.bse}
    table_4 = pd.concat([table_4, pd.DataFrame(data_4_3, index = x_var)], axis = 1)

    y_var = 'lbw'
    model_4_4 = ols_reg(data, y_var, x_var)
    print(model_4_4.summary())
    data_4_4 = {'lbw' : model_4_4.params, 'lbw se' : model_4_4.bse}
    table_4 = pd.concat([table_4, pd.DataFrame(data_4_4, index = x_var)], axis = 1)

    y_var = 'gestation'
    model_4_5 = ols_reg(data, y_var, x_var)
    print(model_4_5.summary())
    data_4_5 = {'gestation' : model_4_5.params, 'gestation se' : model_4_5.bse}
    table_4 = pd.concat([table_4, pd.DataFrame(data_4_5, index = x_var)], axis = 1)

    table_4.rename(columns = {'prenatal' : '1st Trimester Prenatal Care', 'tobacco' : 'Smoked During Pregnancy', 'birthweight' : 'Birthweight', 'lbw' : 'Birth Weight<2500 grams', 'gestation' : 'Gestation Weeks'}, index = {'eitcp': 'EITC percent of federal (among states with EITC)', 'refund' : 'Refund', 'age': 'Maternal age', 'marital': 'Married', 'female': 'Female baby', 'black': 'Black', 'namer': 'Native American', 'asian': 'Asian', 'hisp': 'Hispanic', 'hseduc': 'Less than high school', 'hispmiss': 'Hispanic ethnicity missing', 'cp500': 'County pop 500,000-1,000,000', 'cp250': 'County pop 250,000-500,000', 'cp100': 'County pop 100,000-250,000', 'cpsmall': 'County pop<100,000', 'unemp': 'Unemployment', 'rpcinc': 'Real income per capital (in $1000s)', 'pctpoverty': 'Percent poverty', 'supplyMD_pc': 'Primary care physicians per 1000 females age 15-44'}, inplace = True)
    # print(table_4)
    table_4.to_csv("table_4.csv")
    print("table 4 complete")

if __name__ == "__main__":
    print("I'm running!")
    main()