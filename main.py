import numpy as np
import pandas as pd

from helpers.clean_data import clean_data
from helpers.import_data import import_data
from helpers.merge_data import merge_data
from helpers.clean_county import clean_county
from helpers.clean_eitc import clean_eitc
from helpers.summary_stats import summary_table

def main():
    master = pd.DataFrame()

    filepath = "./inputs/Natl2001.dat"
    colspecs = [(0, 4), (4, 41), (41, 43), (43, 46), (46, 57), (57, 58), (58, 69), (69, 71), (71, 76), (76, 77), (77, 79), (79, 81), (81, 84), (84, 85), (85, 86), (86, 87), (87, 95), (95, 96), (96, 108), (108, 109), (109, 171), (171, 173), (173, 182), (182, 184), (184, 187), (187, 189), (189, 192), (192, 196), (196, 198), (198, 199), (199, 200), (200, 201), (201, 241), (241, 242), (242, -1)]
    columns = ['year', 'drop0', 'state', 'county', 'drop1', 'countysize', 'drop2', 'age', 'drop3', 'hisp', 'drop4', 'race', 'drop5', 'educ', 'drop6', 'marital', 'drop7', 'priorchild', 'drop8', 'prenatal', 'drop9', 'month', 'drop10', 'gestation', 'drop11', 'sex', 'drop12', 'birthweight', 'drop13', 'birthcat', 'drop14', 'number', 'drop15', 'tobacco', 'drop16']
    drop_columns = ['drop0', 'drop1', 'drop2', 'drop3', 'drop4', 'drop5', 'drop6', 'drop7', 'drop8', 'drop9', 'drop10', 'drop11', 'drop12', 'drop13', 'drop14', 'drop15', 'drop16']
    nat_01 = import_data(filepath, colspecs, columns, drop_columns)
    print("2001 import complete", nat_01.info())

    filepath = "./inputs/Natl2002.dat"
    nat_02 = import_data(filepath, colspecs, columns, drop_columns)
    print("2002 import complete", nat_02.info())

    filepath = "./inputs/Nat03us.dat"
    colspecs = [(0, 14), (14, 18), (18, 20), (20, 76), (76, 78), (78, 108), (108, 110), (110, 113), (113, 116), (116, 131), (131, 132), (132, 142), (142, 143), (143, 147), (147, 148), (148, 152), (152, 153), (153, 157), (157, 158), (158, 203), (203, 205), (205, 258), (258, 259), (259, 289), (289, 290), (290, 422), (422, 423), (423, 435), (435, 436), (436, 450), (450, 452), (452, 462), (462, 466), (466, 472), (472, 473), (473, -1)]
    columns = ['drop1' ,'year', 'month', 'drop2', 'age', 'drop3', 'state', 'drop4', 'county', 'drop5', 'countysize', 'drop0', 'race', 'drop6', 'hisp', 'drop7', 'marital', 'drop8', 'educ', 'drop9', 'priorchild', 'drop10', 'prenatal', 'drop11', 'tobacco', 'drop12', 'number', 'drop13', 'sex', 'drop14', 'gestation', 'drop15', 'birthweight', 'drop16', 'birthcat', 'drop17']
    drop_columns = ['drop0', 'drop1', 'drop2', 'drop3', 'drop4', 'drop5', 'drop6', 'drop7', 'drop8', 'drop9', 'drop10', 'drop11', 'drop12', 'drop13', 'drop14', 'drop15', 'drop16', 'drop17']
    nat_03 = import_data(filepath, colspecs, columns, drop_columns)
    print("2003 import complete", nat_03.info())

    state_abbrev_fips_dict = { 'AL': '01', 'AK': '02', 'AZ': '04', 'AR': '05', 'CA': '06', 'CO': '08', 'CT': '09', 'DE': '10', 'FL': '12', 'GA': '13', 'HI': '15', 'ID': '16', 'IL': '17', 'IN': '18', 'IA': '19', 'KS': '20', 'KY': '21', 'LA': '22', 'ME': '23', 'MD': '24', 'MA': '25', 'MI': '26', 'MN': '27', 'MS': '28', 'MO': '29', 'MT': '30', 'NE': '31', 'NV': '32', 'NH': '33', 'NJ': '34', 'NM': '35', 'NY': '36', 'NC': '37', 'ND': '38', 'OH': '39', 'OK': '40', 'OR': '41', 'PA': '42', 'RI': '44', 'SC': '45', 'SD': '46', 'TN': '47', 'TX': '48', 'UT': '49', 'VT': '50', 'VA': '51', 'WA': '53', 'WV': '54', 'WI': '55', 'WY': '56', 'AS': '60', 'GU': '66', 'MP': '69', 'PR': '72', 'VI': '78'}
    nat_03['state'] = nat_03['state'].map(state_abbrev_fips_dict)
    print("state conversion complete", nat_03.info())


    cleaned_01 = clean_data(nat_01)
    cleaned_02 = clean_data(nat_02)
    cleaned_03 = clean_data(nat_03)
    print("birth data cleaning complete", cleaned_01.info(), cleaned_02.info(), cleaned_03.info())

    filepath_u = "./inputs/county_vars.dta"
    filepath_r = "./inputs/ruralcounty_vars.dta"
    county = clean_county(filepath_u, filepath_r)
    print("county data cleaning complete", county.info())

    filepath = "./inputs/eitc.dta"
    eitc = clean_eitc(filepath)
    print("eitc data cleaning complete", eitc.info())

    merged = merge_data(cleaned_01, cleaned_02, cleaned_03, county, eitc)

    print("merge complete", merged.head())
    table_1 = summary_table(merged)

    print("summary table complete", table_1)

    #complete_data = pd.to_pickle("./complete_data.pkl")

if __name__ == "__main__":
    print("I'm running!")
    main()