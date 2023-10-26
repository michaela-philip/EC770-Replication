import numpy as np
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices

data = pd.read_pickle("./complete_data.pkl").dropna()

y_var = 'prenatal'
x_var = ['age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc', 'eitc']
formula = y_var + '~' + '+' .join(x_var) + '+ C(stfips) + C(year) - 1'
y, X = dmatrices(formula, data, return_type = 'dataframe')
model_5_1 = sm.Probit(y, X).fit(cov_type = 'cluster', cov_kwds = {'groups': data['stfips']})
print(model_5_1.summary())

y_var = 'lbw'
model_5_2 = sm.Probit(y, X).fit(cov_type = 'cluster', cov_kwds = {'groups': data['stfips']})
print(model_5_2.summary())


prenatal_me = model_5_1.get_margeff(at='mean', method='dydx', count=True)
lbw_me = model_5_2.get_margeff(at='mean', method='dydx', count=True)

print(prenatal_me.summary())
print(lbw_me.summary())

data={'prenatal' : model_5_1.params, 'prenatal se' : model_5_1.bse, 'low birth weight' : model_5_2.params, 'low birth weight se' : model_5_2.bse}

# table_5 = pd.DataFrame(data, index = x_var)
# table_6 = pd.DataFrame(prenatal_me.summary_frame(), index = x_var)
# table_7 = pd.DataFrame(lbw_me.summary_frame(), index = x_var)
# table_5.to_csv("table_5.csv")
# table_6.to_csv("table_6.csv")
# table_7.to_csv("table_7.csv")
# table_5 = pd.DataFrame(data, index = x_var)
# print(table_5)
# table_5.to_csv("table_5.csv")