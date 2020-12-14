"""CSC110 Project -- US Snowfall vs. Global Land-Ocean Temperature Index"""

from typing import List
import pandas as pd
import snowfall_import as si
import temperature_import as ti
import visualize as vis
import process as pc


def run_all_default() -> None:
    """Run all graphs with recommended default arguments.
    """
    data = import_datasets()
    snowfall, temperature = data[0], data[1]
    run_choropleth(snowfall, temperature, [0, 10])
    run_yearly_scatter_plot(snowfall, temperature, [0, 2])
    run_correlation_scatter_plot(snowfall, temperature, [0, 3])


def import_datasets() -> List[pd.DataFrame]:
    """Import all datasets and filter them so they are ready to be passed to the graph functions.
    """
    original_snowfall = si.df_snow('./data/snowfall/regional-snowfall-index_c20191218.csv',
                                   ['Region', 'Year', 'RSI'])
    no_national_snowfall = si.remove_national(original_snowfall)
    aggregated_snowfall = si.agg_years(no_national_snowfall)

    temperature = ti.df_temp(
        './data/land-ocean_temperature_index/land-ocean_temperature_index.csv')
    return pc.common_years([aggregated_snowfall, temperature])


def run_choropleth(snowfall: pd.DataFrame, temperature: pd.DataFrame,
                   rsi_color_scale_range: List[float]) -> None:
    """Show the choropleth graph.

    Preconditions:
        - 'Year' in snowfall.columns
        - 'Region' in snowfall.columns
        - 'RSI' in snowfall.columns
        - 'Year' in temperature.columns
        - 'Raw' in temperature.columns
        - len(rsi_color_scale_range) == 2
        - rsi_color_scale_range[0] < rsi_color_scale_range[1]
    """
    states_snowfall_data = si.regions_to_states(snowfall)
    vis.show_animated_choropleth(states_snowfall_data, temperature, rsi_color_scale_range)


def run_yearly_scatter_plot(snowfall: pd.DataFrame, temperature: pd.DataFrame,
                            rsi_axis_range: List[float]) -> None:
    """Show the year comparison scatter_plot.

    Preconditions:
        - 'Year' in snowfall.columns
        - 'Region' in snowfall.columns
        - 'RSI' in snowfall.columns
        - 'Year' in temperature.columns
        - 'Raw' in temperature.columns
        - len(rsi_axis_range) == 2
        - rsi_axis_range[0] < rsi_axis_range[1]
    """
    vis.show_yearly_scatter_plot(snowfall, temperature, rsi_axis_range)


def run_correlation_scatter_plot(snowfall: pd.DataFrame, temperature: pd.DataFrame,
                                 rsi_axis_range: List[float]) -> None:
    """Show the correlation scatter_plot.

    Preconditions:
        - 'Year' in snowfall.columns
        - 'Region' in snowfall.columns
        - 'RSI' in snowfall.columns
        - 'Year' in temperature.columns
        - 'Raw' in temperature.columns
        - len(rsi_axis_range) == 2
        - rsi_axis_range[0] < rsi_axis_range[1]
    """
    vis.show_correlation_scatter_plot(snowfall, temperature, rsi_axis_range)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'snowfall_import', 'temperature_import',
                          'visualize', 'process', 'pandas'],
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
