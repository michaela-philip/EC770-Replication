import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib as plt

from helpers.ols_reg import ols_reg

complete_data = pd.read_pickle("./complete_data.pkl")

def main():

    data = complete_data
    y_var = 'prenatal'
    x_var = ['eitc', 'age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc']

    model_2_1 = ols_reg(data, y_var, x_var)

    print(model_2_1.summary())


if __name__ == "__main__":
    print("I'm running!")
    main()