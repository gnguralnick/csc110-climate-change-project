"""CSC110 Project -- Visualizing Data"""

import pandas as pd
import plotly.express as px
import temperature_import
import snowfall_import
import process


REGIONS = {'Northeast': ['PA', 'NY', 'ME', 'MA', 'CT', 'RI', 'VT', 'NJ', 'DE', 'MD', 'NH'],
           'Northern Rockies and Plains': ['MT', 'ND', 'SD', 'WY', 'NE'],
           'Ohio Valley': ['MO', 'IL', 'TN', 'WV', 'OH', 'IN', 'KY'],
           'South': ['KS', 'OK', 'MS', 'TX', 'AR', 'LA'],
           'Southeast': ['VA', 'NC', 'SC', 'AL', 'GA', 'FL'],
           'Upper Midwest': ['MN', 'IA', 'WI', 'MI']}


def show_animated_choropleth(snowfall: pd.DataFrame, temperature: pd.DataFrame) -> None:
    """Show animated choropleth of snowfall vs temperature over time.
    """
    intersecting_years = process.intersecting_years([snowfall, temperature])
    snowfall, temperature = intersecting_years[0], intersecting_years[1]

    min_year = snowfall['Year'].min()
    max_year = snowfall['Year'].max()
    max_rsi = snowfall['RSI'].max()

    title = 'US Central and Eastern RSI vs. Global Land-Ocean Temperature Index From ' + \
            str(min_year) + ' to ' + str(max_year)

    fig = px.choropleth(data_frame=snowfall, locations='State', locationmode="USA-states",
                        scope='usa', animation_frame='Year', animation_group='State',
                        color='RSI', range_color=(0, max_rsi), title=title)

    for step in fig['layout']['sliders'][0]['steps']:
        step['label'] = step['label'] + ', ' + str(
            temperature.query('Year == ' + step['label']).iloc[0]['Raw'])

    fig.show()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'pandas', 'plotly.express', 'temperature_import',
                          'process'],
        'allowed-io': ['import_as_dict'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)

    original_snowfall_data = snowfall_import.df_snow(
        '../data/snowfall/regional-snowfall-index_c20191218.csv',
        ['Region', 'Year', 'RSI'])
    print(original_snowfall_data)
    aggregated_snowfall_data = snowfall_import.agg_years(original_snowfall_data,
                                                         pd.core.groupby.generic.DataFrameGroupBy.sum)
    # aggregated_snowfall_data = snowfall_import.agg_years_mean(original_snowfall_data)
    # aggregated_snowfall_data = snowfall_import.agg_years_sum(original_snowfall_data)
    print(aggregated_snowfall_data)
    unnational_snowfall_data = aggregated_snowfall_data.query('Region != "National"')
    print(unnational_snowfall_data)
    stateified_snowfall_data = snowfall_import.stateify_data(unnational_snowfall_data)
    print(stateified_snowfall_data)
    temperature_data = temperature_import.import_as_dataframe(
        '../data/land-ocean_temperature_index/land-ocean_temperature_index.csv')
    print(temperature_data)
    show_animated_choropleth(stateified_snowfall_data, temperature_data)
