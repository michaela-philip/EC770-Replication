import numpy as np
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices 

def ols_reg(data, y_var, x_var):
    formula = y_var + '~' + '+' .join(x_var) + ' + C(year) - 1'
    y, X = dmatrices(formula, data, return_type = 'dataframe')
    model = sm.OLS(y, X).fit(cov_type = 'cluster', cov_kwds = {'groups': data['stfips']})
    return model

