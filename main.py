"""CSC110 Project -- US Snowfall vs. Global Land-Ocean Temperature Index"""

import program
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
    temp_data = ti.import_as_dataframe(
        'data/land-ocean_temperature_index/land-ocean_temperature_index.csv'
    )
    vis.initialize_heatmap(temp_data, snow_data)
    while True:
        pass


def run_choropleth() -> None:
    original_snowfall_data = si.df_snow(
        './data/snowfall/regional-snowfall-index_c20191218.csv',
        ['Region', 'Year', 'RSI'])
    aggregated_snowfall_data = si.agg_years(original_snowfall_data,
                                            pd.core.groupby.generic.DataFrameGroupBy.sum)
    unnational_snowfall_data = aggregated_snowfall_data.query('Region != "National"')
    stateified_snowfall_data = si.regions_to_states(unnational_snowfall_data)
    temperature_data = ti.import_as_dataframe(
        './data/land-ocean_temperature_index/land-ocean_temperature_index.csv')
    vis.show_animated_choropleth(stateified_snowfall_data, temperature_data)
