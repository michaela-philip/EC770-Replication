import numpy as np
import pandas as pd
import statsmodels.api as sm

def ols_reg(data, y_var, x_var):
    y = data[y_var]
    X = data[x_var]
    model = sm.OLS(y, X).fit()
    return model
    print(model.summary())