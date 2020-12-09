
import pandas as ps
import python_ta


def snowfall_csv_import(filepath: str) -> ps.DataFrame:
    """
    This function returns a dataframe from the given csv file.
    Preconditions:

    Doctest:

    """
    return ps.read_csv(filepath)


# python_ta.check_all(config={
#     'extra-imports': [],  # the names (strs) of imported modules
#     'allowed-io': [],     # the names (strs) of functions that call print/open/input
#     'max-line-length': 100,
#     'disable': ['R1705', 'C0200']
# })
