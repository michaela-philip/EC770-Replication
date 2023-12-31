import pandas as pd
import numpy as np

#let's read in the data

county_vars = pd.read_stata("./inputs/county_vars.dta")

eitc = pd.read_stata("./inputs/eitc.dta")

ruralcounty_vars = pd.read_stata("./inputs/ruralcounty_vars.dta")

#creating eitc categories
eitc['eitc'] = np.where(eitc['eitc_pct'] > 0, 1, 0)

eitc['eitcp'] = np.where(eitc['eitc_pct'] > 0, eitc['eitc_pct'], np.nan)

eitc['refund'] = np.where((eitc['eitc'] == 1) & (eitc['refund'] == 1), 1, np.where((eitc['eitc'] == 1) & (eitc['refund'] == 0), 0, np.nan))

#we want to use rural county data for any county code 999
ruralcounty_vars['cofips'] = pd.Series([999 for x in range(len(ruralcounty_vars.index))])

#drop indicator of small county in rural county
ruralcounty_vars = ruralcounty_vars.drop(columns = ['pop_lt_100k'])

#combining the rural and urban county data
county = pd.concat([county_vars, ruralcounty_vars])