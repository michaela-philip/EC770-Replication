import numpy as np
import pandas as pd

def clean_eitc(filepath):
    output = pd.read_stata(filepath)
    
    output['eitc'] = np.where(output['eitc_pct'] > 0, 1, 0)

    output['eitcp'] = np.where(output['eitc_pct'] > 0, output['eitc_pct'], np.nan)

    output['refund'] = np.where((output['eitc'] == 1) & (output['refund'] == 1), 1, np.where((output['eitc'] == 1) & (output['refund'] == 0), 0, np.nan))

    return output