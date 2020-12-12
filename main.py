"""CSC110 Project -- US Snowfall vs. Global Land-Ocean Temperature Index"""

from typing import List
import snowfall_import as si
import temperature_import as ti
import visualize as vis
import process as ps
import pandas as pd


def run_all_default() -> None:
    """Run all graphs with recommended default arguments.
    """
    data = import_datasets()
    snowfall_data, temperature_data = data[0], data[1]
    run_choropleth([0, 10], snowfall_data, temperature_data)
    run_year_comparison_scatter_plot([0, 2], snowfall_data, temperature_data)
    run_correlation_scatter_plot([0, 3], snowfall_data, temperature_data)


def import_datasets() -> List[pd.DataFrame]:
    """Import all datasets and filter them so they are ready to be passed to the graph functions.
    """
    original_snowfall_data = si.df_snow(
        './data/snowfall/regional-snowfall-index_c20191218.csv',
        ['Region', 'Year', 'RSI'])
    no_national_snowfall_data = si.remove_national(original_snowfall_data)
    aggregated_snowfall_data = si.agg_years(no_national_snowfall_data)

    temperature_data = ti.df_temp(
        './data/land-ocean_temperature_index/land-ocean_temperature_index.csv')
    return ps.common_years([aggregated_snowfall_data, temperature_data])


def run_choropleth(rsi_color_scale_range: List[float], snowfall_data: pd.DataFrame, temp_data: pd.DataFrame) -> None:
    """Show the choropleth graph.
    """
    states_snowfall_data = si.regions_to_states(snowfall_data)
    vis.show_animated_choropleth(states_snowfall_data, temp_data, rsi_color_scale_range)


def run_year_comparison_scatter_plot(rsi_axis_range: List[float], snowfall_data: pd.DataFrame, temp_data: pd.DataFrame) -> None:
    """Show the year comparison scatter_plot.
    """
    vis.show_year_comparison_scatter_plot(snowfall_data, temp_data, rsi_axis_range)


def run_correlation_scatter_plot(rsi_axis_range: List[float], snowfall_data: pd.DataFrame, temp_data: pd.DataFrame) -> None:
    """Show the correlation scatter_plot.
    """
    vis.show_correlation_scatter_plot(snowfall_data, temp_data, rsi_axis_range)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['csv', 'os', 'dataclasses', 'python_ta.contracts', 'pandas'],
        'allowed-io': ['import_as_dict'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)

    run_all_default()
