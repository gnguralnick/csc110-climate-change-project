"""CSC110 Project -- US Snowfall vs. Global Land-Ocean Temperature Index"""

from typing import List
import snowfall_import as si
import temperature_import as ti
import visualize as vis
import process
import pandas as pd


def run_all_default() -> None:
    data = import_datasets()
    snowfall_data, temperature_data = data[0], data[1]
    run_choropleth([0, 10], snowfall_data, temperature_data)
    run_year_comparison_scatterplot([0, 2], snowfall_data, temperature_data)
    run_correlation_scatterplot([0, 3], snowfall_data, temperature_data)


def import_datasets() -> List[pd.DataFrame]:
    original_snowfall_data = si.df_snow(
        './data/snowfall/regional-snowfall-index_c20191218.csv',
        ['Region', 'Year', 'RSI'])
    no_national_snowfall_data = si.remove_national(original_snowfall_data)
    aggregated_snowfall_data = si.agg_years(no_national_snowfall_data,
                                            pd.core.groupby.generic.DataFrameGroupBy.mean)

    temperature_data = ti.df_temp(
        './data/land-ocean_temperature_index/land-ocean_temperature_index.csv')
    return process.common_years([aggregated_snowfall_data, temperature_data])


def run_choropleth(rsi_color_scale_range: List[float], snowfall_data: pd.DataFrame, temp_data: pd.DataFrame) -> None:
    states_snowfall_data = si.regions_to_states(snowfall_data)
    vis.show_animated_choropleth(states_snowfall_data, temp_data, rsi_color_scale_range)


def run_year_comparison_scatterplot(rsi_axis_range: List[float], snowfall_data: pd.DataFrame, temp_data: pd.DataFrame) -> None:
    vis.show_year_comparison_scatterplot(snowfall_data, temp_data, rsi_axis_range)


def run_correlation_scatterplot(rsi_axis_range: List[float], snowfall_data: pd.DataFrame, temp_data: pd.DataFrame) -> None:
    vis.show_correlation_scatterplot(snowfall_data, temp_data, rsi_axis_range)


if __name__ == '__main__':
    # import python_ta
    #
    # python_ta.check_all(config={
    #     'extra-imports': ['csv', 'os', 'dataclasses', 'python_ta.contracts', 'pandas'],
    #     'allowed-io': ['import_as_dict'],
    #     'max-line-length': 100,
    #     'disable': ['R1705', 'C0200']
    # })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)

    run_all_default()
