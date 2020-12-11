"""CSC110 Project -- US Snowfall vs. Global Land-Ocean Temperature Index"""

import program
from typing import List
from program import snowfall_import as si
from program import temperature_import as ti
from program import visualize as vis
import pandas as pd


def run() -> None:
    snow_params = ['Region', 'Start', 'End', 'RSI', 'Category']

    snow_data = si.df_snow(
        'data/snowfall/regional-snowfall-index_c20191218.csv',
        snow_params
        )
    temp_data = ti.df_temp(
        'data/land-ocean_temperature_index/land-ocean_temperature_index.csv'
    )
    vis.initialize_heatmap(temp_data, snow_data)
    while True:
        pass

def run_choropleth(rsi_color_scale_range: List[float]) -> None:
    original_snowfall_data = si.df_snow(
        './data/snowfall/regional-snowfall-index_c20191218.csv',
        ['Region', 'Year', 'RSI'])
    no_national_snowfall_data = si.remove_national(original_snowfall_data)
    aggregated_snowfall_data = si.agg_years(no_national_snowfall_data,
                                            pd.core.groupby.generic.DataFrameGroupBy.mean)
    states_snowfall_data = si.regions_to_states(aggregated_snowfall_data)
    temperature_data = ti.df_temp(
        './data/land-ocean_temperature_index/land-ocean_temperature_index.csv')
    vis.show_animated_choropleth(states_snowfall_data, temperature_data, rsi_color_scale_range)


def run_comparison_scatterplot(rsi_axis_range: List[float]) -> None:
    original_snowfall_data = si.df_snow(
        './data/snowfall/regional-snowfall-index_c20191218.csv',
        ['Region', 'Year', 'RSI'])
    no_national_snowfall_data = si.remove_national(original_snowfall_data)
    aggregated_snowfall_data = si.agg_years(no_national_snowfall_data,
                                            pd.core.groupby.generic.DataFrameGroupBy.mean)
    temperature_data = ti.df_temp(
        './data/land-ocean_temperature_index/land-ocean_temperature_index.csv')
    vis.show_comparison_scatterplot(aggregated_snowfall_data, temperature_data, rsi_axis_range)


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
