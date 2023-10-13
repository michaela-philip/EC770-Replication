import numpy as np
import pandas as pd

#specifying column breakdowns for 2001 and 2002 data

colspecs = [(0, 4), (4, 41), (41, 43), (43, 46), (46, 69), (69, 71), (71, 76), (76, 77), (77, 79), (79, 81), (81, 84), (84, 85), (85, 86), (86, 87), (87, 95), (95, 96), (96, 108), (108, 109), (109, 171), (171, 173), (173, 182), (182, 184), (184, 187), (187, 189), (189, 192), (192, 196), (196, 198), (198, 199), (199, 200), (200, 201), (201, 241), (241, 242), (242, -1)]

#trying to read in the data using fwf

natl2001_full = pd.read_fwf("C:/Users/micha/OneDrive - Emory University/Second Year/Health Econ I/Replication/Data/Natl2001.dat", colspecs = colspecs, header = None)
                                                    
natl2001_full.columns = ['year', 'drop1', 'state', 'county', 'drop2', 'age', 'drop3', 'hisp', 'drop4', 'race', 'drop5', 'educ', 'drop6', 'marital', 'drop7', 'priorchild', 'drop8', 'prenatal', 'drop9', 'month', 'drop10', 'gestation', 'drop11', 'sex', 'drop12', 'birthweight', 'drop13', 'birthcat', 'drop14', 'number', 'drop15', 'tobacco', 'drop16']

#dropping unneeded columns

natl2001 = natl2001_full.drop(columns=['drop1', 'drop2', 'drop3', 'drop4', 'drop5', 'drop6', 'drop7', 'drop8', 'drop9', 'drop10', 'drop11', 'drop12', 'drop13', 'drop14', 'drop15', 'drop16'])

#doing it again!

natl2002_full = pd.read_fwf("C:/Users/micha/OneDrive - Emory University/Second Year/Health Econ I/Replication/Data/Natl2002.dat", colspecs = colspecs, header = None)

natl2002_full.columns = ['year', 'drop1', 'state', 'county', 'drop2', 'age', 'drop3', 'hisp', 'drop4', 'race', 'drop5', 'educ', 'drop6', 'marital', 'drop7', 'priorchild', 'drop8', 'prenatal', 'drop9', 'month', 'drop10', 'gestation', 'drop11', 'sex', 'drop12', 'birthweight', 'drop13', 'birthcat', 'drop14', 'number', 'drop15', 'tobacco', 'drop16']

natl2002 = natl2002_full.drop(columns=['drop1', 'drop2', 'drop3', 'drop4', 'drop5', 'drop6', 'drop7', 'drop8', 'drop9', 'drop10', 'drop11', 'drop12', 'drop13', 'drop14', 'drop15', 'drop16'])

#data changes slightly for 2003

colspecs2 = [(0, 14), (14, 18), (18, 20), (20, 76), (76, 78), (78, 108), (108, 110), (110, 113), (113, 116), (116, 142), (142, 143), (143, 147), (147, 148), (148, 152), (152, 153), (153, 157), (157, 158), (158, 203), (203, 205), (205, 258), (258, 259), (259, 289), (289, 290), (290, 422), (422, 423), (423, 435), (435, 436), (436, 450), (450, 452), (452, 462), (462, 466), (466, 472), (472, 473), (473, -1)]

natl2003_full = pd.read_fwf("C:/Users/micha/OneDrive - Emory University/Second Year/Health Econ I/Replication/Data/Nat03us.dat", colspecs = colspecs2, header = None)

natl2003_full.columns =  ['drop1' ,'year', 'month', 'drop2', 'age', 'drop3', 'state', 'drop4', 'county', 'drop5', 'race', 'drop6', 'hisp', 'drop7', 'marital', 'drop8', 'educ', 'drop9', 'priorchild', 'drop10', 'prenatal', 'drop11', 'tobacco', 'drop12', 'number', 'drop13', 'sex', 'drop14', 'gestation', 'drop15', 'birthweight', 'drop16', 'birthcat', 'drop17']

natl2003 = natl2003_full.drop(columns=['drop1', 'drop2', 'drop3', 'drop4', 'drop5', 'drop6', 'drop7', 'drop8', 'drop9', 'drop10', 'drop11', 'drop12', 'drop13', 'drop14', 'drop15', 'drop16', 'drop17'])

natl2003_short = natl2003.drop(natl2003.index[100:])

