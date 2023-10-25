import numpy as np
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices

data = pd.read_pickle("./complete_data.pkl").dropna()

y_var = 'prenatal'
x_var = ['eitc', 'age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc']
formula = y_var + '~' + '+' .join(x_var) + '+ C(stfips) + C(year) - 1'
y, X = dmatrices(formula, data, return_type = 'dataframe')
model_5_1 = sm.Probit(y, X).fit(cov_type = 'cluster', cov_kwds = {'groups': data['stfips']})
print(model_5_1.summary())

y_var = 'lbw'
model_5_2 = sm.Probit(y, X).fit(cov_type = 'cluster', cov_kwds = {'groups': data['stfips']})
print(model_5_2.summary())

prenatal_me = model_5_1.get_margeff(at='mean', method='dydx')
lbw_me = model_5_2.get_margeff(at='mean', method='dydx')

print("prenatal params",  model_5_1.params)
print("prenatal me",  prenatal_me)
print("lbw params",  model_5_2.params)
print("lbw me",  lbw_me)