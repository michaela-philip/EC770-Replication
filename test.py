import numpy as np
import pandas as pd

from helpers.clean_data import clean_data
from helpers.import_data import import_data 
from helpers.clean_data import convert_to_fips 

def test_1():
    filepath = "./inputs/Natl2001.dat"
    colspecs = [(0, 4), (4, 41), (41, 43), (43, 46), (46, 57), (57, 58), (58, 69), (69, 71), (71, 76), (76, 77), (77, 79), (79, 81), (81, 84), (84, 85), (85, 86), (86, 87), (87, 95), (95, 96), (96, 108), (108, 109), (109, 171), (171, 173), (173, 182), (182, 184), (184, 187), (187, 189), (189, 192), (192, 196), (196, 198), (198, 199), (199, 200), (200, 201), (201, 241), (241, 242), (242, -1)]
    columns = ['year', 'drop0', 'state', 'county', 'drop1', 'countysize', 'drop2', 'age', 'drop3', 'hisp', 'drop4', 'race', 'drop5', 'educ', 'drop6', 'marital', 'drop7', 'priorchild', 'drop8', 'prenatal', 'drop9', 'month', 'drop10', 'gestation', 'drop11', 'sex', 'drop12', 'birthweight', 'drop13', 'birthcat', 'drop14', 'number', 'drop15', 'tobacco', 'drop16']
    drop_columns = ['drop0', 'drop1', 'drop2', 'drop3', 'drop4', 'drop5', 'drop6', 'drop7', 'drop8', 'drop9', 'drop10', 'drop11', 'drop12', 'drop13', 'drop14', 'drop15', 'drop16']
    nat_01 = import_data(filepath, colspecs, columns, drop_columns)

    print(nat_01.head())

    cleaned_01 = clean_data(nat_01)

    print(cleaned_01.head())

def test_2():
    filepath = "./inputs/Nat03us.dat"
    colspecs = [(0, 14), (14, 18), (18, 20), (20, 76), (76, 78), (78, 108), (108, 110), (110, 113), (113, 116), (116, 131), (131, 132), (132, 142), (142, 143), (143, 147), (147, 148), (148, 152), (152, 153), (153, 157), (157, 158), (158, 203), (203, 205), (205, 258), (258, 259), (259, 289), (289, 290), (290, 422), (422, 423), (423, 435), (435, 436), (436, 450), (450, 452), (452, 462), (462, 466), (466, 472), (472, 473), (473, -1)]
    columns = ['drop1' ,'year', 'month', 'drop2', 'age', 'drop3', 'state', 'drop4', 'county', 'drop5', 'countysize', 'drop0', 'race', 'drop6', 'hisp', 'drop7', 'marital', 'drop8', 'educ', 'drop9', 'priorchild', 'drop10', 'prenatal', 'drop11', 'tobacco', 'drop12', 'number', 'drop13', 'sex', 'drop14', 'gestation', 'drop15', 'birthweight', 'drop16', 'birthcat', 'drop17']
    drop_columns = ['drop0', 'drop1', 'drop2', 'drop3', 'drop4', 'drop5', 'drop6', 'drop7', 'drop8', 'drop9', 'drop10', 'drop11', 'drop12', 'drop13', 'drop14', 'drop15', 'drop16', 'drop17']
    limit = 1000
    nat_03_s = import_data(filepath, colspecs, columns, drop_columns)

    print(nat_03_s.head())
    #nat_03 = convert_to_fips(nat_03_s)

    cleaned_03 = clean_data(nat_03_s)

    print(cleaned_03.head())


if __name__ == "__main__":
    print("I'm running!")
    test_2()


filepath = "./inputs/Nat03us.dat"
colspecs = [(0, 14), (14, 18), (18, 20), (20, 76), (76, 78), (78, 108), (108, 110), (110, 113), (113, 116), (116, 131), (131, 132), (132, 142), (142, 143), (143, 147), (147, 148), (148, 152), (152, 153), (153, 157), (157, 158), (158, 203), (203, 205), (205, 258), (258, 259), (259, 289), (289, 290), (290, 422), (422, 423), (423, 435), (435, 436), (436, 450), (450, 452), (452, 462), (462, 466), (466, 472), (472, 473), (473, -1)]
columns = ['drop1' ,'year', 'month', 'drop2', 'age', 'drop3', 'state', 'drop4', 'county', 'drop5', 'countysize', 'drop0', 'race', 'drop6', 'hisp', 'drop7', 'marital', 'drop8', 'educ', 'drop9', 'priorchild', 'drop10', 'prenatal', 'drop11', 'tobacco', 'drop12', 'number', 'drop13', 'sex', 'drop14', 'gestation', 'drop15', 'birthweight', 'drop16', 'birthcat', 'drop17']
drop_columns = ['drop0', 'drop1', 'drop2', 'drop3', 'drop4', 'drop5', 'drop6', 'drop7', 'drop8', 'drop9', 'drop10', 'drop11', 'drop12', 'drop13', 'drop14', 'drop15', 'drop16', 'drop17']
limit = 1000
nat_03_s = import_data(filepath, colspecs, columns, drop_columns, limit)

print(nat_03_s.head())

nat_03 = convert_to_fips(nat_03_s)

cleaned_03 = clean_data(nat_03)

print(cleaned_03.head())
