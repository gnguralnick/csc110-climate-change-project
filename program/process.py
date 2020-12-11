"""CSC110 Project -- Processing Data"""
import pandas as pd
from typing import List


def intersecting_years(df_list: List[pd.DataFrame]) -> List[pd.DataFrame]:
    """Given a list of DataFrames with a continuous 'Year' column, return a list containing the same
    DataFrames with any years that are not present in the others removed.
    """
    upper_bound = min(max(df['Year']) for df in df_list)
    lower_bound = max(min(df['Year']) for df in df_list)

    return [df.query(str(upper_bound) + ' >= Year >= ' + str(lower_bound)) for df in df_list]
