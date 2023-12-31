from helpers.import_data import import_data

#specifying column breakdowns for 2001 data

def main():
    filepath = "./inputs/Natl2001.dat"
    colspecs = [(0, 4), (4, 41), (41, 43), (43, 46), (46, 57), (57, 58), (58, 69), (69, 71), (71, 76), (76, 77), (77, 79), (79, 81), (81, 84), (84, 85), (85, 86), (86, 87), (87, 95), (95, 96), (96, 108), (108, 109), (109, 171), (171, 173), (173, 182), (182, 184), (184, 187), (187, 189), (189, 192), (192, 196), (196, 198), (198, 199), (199, 200), (200, 201), (201, 241), (241, 242), (242, -1)]
    columns = ['year', 'drop0', 'state', 'county', 'drop1', 'countysize', 'drop2', 'age', 'drop3', 'hisp', 'drop4', 'race', 'drop5', 'educ', 'drop6', 'marital', 'drop7', 'priorchild', 'drop8', 'prenatal', 'drop9', 'month', 'drop10', 'gestation', 'drop11', 'sex', 'drop12', 'birthweight', 'drop13', 'birthcat', 'drop14', 'number', 'drop15', 'tobacco', 'drop16']
    drop_columns = ['drop0', 'drop1', 'drop2', 'drop3', 'drop4', 'drop5', 'drop6', 'drop7', 'drop8', 'drop9', 'drop10', 'drop11', 'drop12', 'drop13', 'drop14', 'drop15', 'drop16']

    nat01 = import_data(filepath, colspecs, columns, drop_columns)
    print(nat01.head())

if __name__ == "__main__":
    main()