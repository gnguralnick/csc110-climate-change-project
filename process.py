"""CSC110 Project -- Processing Data"""

from typing import List
import pandas as pd
import statsmodels.api as sm


def common_years(df_list: List[pd.DataFrame]) -> List[pd.DataFrame]:
    """Given a list of DataFrames with a continuous or discontinuous 'Year' columns, return a list
    containing the same DataFrames with any years that are not present in the others removed.

    Preconditions:
        - df.empty == False
        - 'Year' in df.columns

    >>> data1 = {'Region': ['National', 'South'], 'Year': [2001, 2001], 'RSI': [3.0, 2.15]}
    >>> data2 = {'Year': [2001, 2002], 'Raw': [0.5, 0.8], 'Smoothed': [0.5, 0.7]}
    >>> df1 = pd.DataFrame(data1)
    >>> df2 = pd.DataFrame(data2)
    >>> common_years([df1, df2])
    [     Region  Year   RSI
    0  National  2001  3.00
    1     South  2001  2.15,    Year  Raw  Smoothed
    0  2001  0.5       0.5]
    """
    years_so_far = set(df_list[0]['Year'])
    for i in range(1, len(df_list)):
        years_so_far = years_so_far.intersection(set(df_list[i]['Year']))

    query_so_far = ''
    for year in years_so_far:
        query_so_far += 'Year == ' + str(year) + ' or '

    return [df.query(query_so_far[0:-4]) for df in df_list]


def lowess(df: pd.DataFrame, x: str, y: str) -> pd.DataFrame:
    """Given a DataFrame containing both x and y column names, return a lowess smoothed DataFrame
    with only the x and y data.

    Preconditions:
        - df.empty == False
        - x in df.columns
        - y in df.columns
    """
    return pd.DataFrame(sm.nonparametric.lowess(
        endog=df[y],
        exog=df[x]
    ), columns=[x, y])


def add_year_temps(snowfall: pd.DataFrame, temperature: pd.DataFrame) -> pd.DataFrame:
    """Given both snowfall and temperature dataframes, return the snowfall dataframe with an
    added temperature column that corresponds to the raw temperature in the year of that
    row in the temperature dataframe.
    """
    conversion_dict = dict(zip(temperature['Year'], temperature['Raw']))
    return snowfall.assign(temperature=[
        conversion_dict[row['Year']]
        for row in snowfall.iloc]).rename(columns={'temperature': 'Temperature'})


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'pandas', 'statsmodels.api'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
