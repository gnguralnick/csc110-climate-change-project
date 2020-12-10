"""CSC110 Project -- US Snowfall vs. Global Land-Ocean Temperature Index"""
import program
from program import snowfall_import as si
from program import temperature_import as ti
from program import visualization as vis



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
