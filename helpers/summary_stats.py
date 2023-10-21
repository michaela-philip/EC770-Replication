import numpy as np
import pandas as pd

def summary_table(input):
    if not isinstance(input, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    output = pd.DataFrame()

    output = input.describe().T

    output = output.drop(columns=['count', '25%', '50%', '75%'])

    output = output.rename(columns={'mean': 'Mean', 'std': 'Std. Dev.', 'min': 'Min', 'max': 'Max'})

    output = output.reindex(['prenatal', 'tobacco', 'birthweight', 'lbw', 'gestation', 'eitc', 'eitcp', 'refund', 'age', 'marital', 'female', 'black', 'namer', 'asian', 'hisp', 'hseduc', 'hispmiss', 'cp500', 'cp250', 'cp100', 'cpsmall', 'unemp', 'rpcinc', 'pctpoverty', 'supplyMD_pc'])

    print(output)

if __name__ == "__main__":
    raise RuntimeError("This script is not intended to be run directly.")