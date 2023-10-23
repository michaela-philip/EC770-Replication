import numpy as np
import pandas as pd
import statsmodels.api as sm

def ols_reg(data, y_var, x_var):
    y = data[y_var]
    X = data[x_var]
    X = C('state') + C('year') - 1
    model = sm.OLS(y, X, missing = 'drop').fit()
    return model