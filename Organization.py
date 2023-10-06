import pandas as pd
import numpy as np

#let's read in the data

county_vars = pd.read_stata("C:/EITC Replication/Replication/Data/county_vars.dta")

eitc = pd.read_stata("C:/EITC Replication/Replication/Data/eitc.dta")

ruralcounty_vars = pd.read_stata("C:/EITC Replication/Replication/Data/ruralcounty_vars.dta")

natl2001 = pd.read_stata('C:/EITC Replication/Replication/Data/natl2001.dta')

natl2002 = pd.read_stata('C:/EITC Replication/Replication/Data/natl2002.dta')

natl2003 = pd.read_stata('C:/EITC Replication/Replication/Data/natl2003.dta')
