"""CSC110 Project -- Processing Data"""
from typing import List
import pandas as pd


def intersecting_years(df_list: List[pd.DataFrame]) -> List[pd.DataFrame]:
    """Given a list of DataFrames with a continuous 'Year' column, return a list containing the same
    DataFrames with any years that are not present in the others removed.
    """
    upper_bound = min(max(df['Year']) for df in df_list)
    lower_bound = max(min(df['Year']) for df in df_list)

    return [df.query(str(upper_bound) + ' >= Year >= ' + str(lower_bound)) for df in df_list]


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'pandas'],
        'allowed-io': ['import_as_dict'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
