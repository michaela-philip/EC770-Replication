import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib as plt

from helpers.ols_reg import ols_reg
from helpers.summary_stats import summary_table

complete_data = pd.read_pickle("./complete_data.pkl")

def main():

    table_1 = summary_table(complete_data)
    print(table_1)

    data = complete_data

    # y_var = 'prenatal'
    x_var = ['eitc', 'age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc']
    # model_2_1 = ols_reg(data, y_var, x_var)
    # print(model_2_1.summary())

    y_var = 'tobacco'
    model_2_2 = ols_reg(data, y_var, x_var)
    print(model_2_2.summary())


if __name__ == "__main__":
    print("I'm running!")
    main()