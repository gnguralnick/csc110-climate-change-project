"""CSC110 Project -- Processing Data"""

import temperature_import
import datetime
import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go

SAMPLE_SNOWFALL_DATAFRAME = pd.DataFrame({'State': ['PA', 'PA', 'PA', 'PA', 'PA', 'NY', 'NY', 'NY',
                                                    'NY', 'NY'],
                                          'RSI': [2, 3, 4, 5, 6, 4, 5, 6, 7, 8],
                                          'Year': [2015, 2016, 2017, 2018, 2019, 2015, 2016, 2017,
                                                   2018, 2019]},
                                         columns=['State', 'RSI', 'Year'])

REGIONS = {'Northeast': ['PA', 'NY', 'ME', 'MA', 'CT', 'RI', 'VT', 'NJ', 'DE', 'MD', 'NH'],
           'Northern Rockies and Plains': ['MT', 'ND', 'SD', 'WY', 'NE'],
           'Ohio Valley': ['MO', 'IL', 'TN', 'WV', 'OH', 'IN', 'KY'],
           'South': ['KS', 'OK', 'MS', 'TX', 'AR', 'LA'],
           'Southeast': ['VA', 'NC', 'SC', 'AL', 'GA', 'FL'],
           'Upper Midwest': ['MN', 'IA', 'WI', 'MI']}


def show_animated_df(snowfall: pd.DataFrame, temperature: pd.DataFrame) -> None:
    """Show animated dataframe of snowfall.
    """
    min_snowfall_year = min(snowfall['Year'])
    max_snowfall_year = max(snowfall['Year'])

    min_temperature_year = min(temperature['Year'])
    max_temperature_year = max(temperature['Year'])

    max_rsi = max(snowfall['RSI'])

    if max_snowfall_year > max_temperature_year:
        snowfall = snowfall.query('Year <= ' + str(max_temperature_year))
        max_year = max_temperature_year
    elif max_snowfall_year < max_temperature_year:
        temperature = temperature.query('Year <= ' + str(max_snowfall_year))
        max_year = max_snowfall_year
    else:
        max_year = max_temperature_year

    if min_snowfall_year < min_temperature_year:
        snowfall = snowfall.query('Year >= ' + str(min_temperature_year))
        min_year = min_temperature_year
    elif min_snowfall_year > min_temperature_year:
        temperature = temperature.query('Year >= ' + str(min_snowfall_year))
        min_year = min_snowfall_year
    else:
        min_year = min_temperature_year

    title = 'US Central and Eastern RSI vs. Global Land-Ocean Temperature Index From ' + \
            str(min_year) + ' to ' + str(max_year)

    fig = px.choropleth(data_frame=snowfall, locations='State', locationmode="USA-states",
                        scope='usa', animation_frame='Year', animation_group='State', color='RSI',
                        range_color=(0, max_rsi), title=title)

    for step in fig['layout']['sliders'][0]['steps']:
        step['label'] = step['label'] + ', '\
                        + str(temperature.query('Year == ' + step['label']).iloc[0]['Raw'])

    fig.show()


if __name__ == '__main__':
    show_animated_df(SAMPLE_SNOWFALL_DATAFRAME, temperature_import.import_as_dataframe('../data/land-ocean_temperature_index/land-ocean_temperature_index.csv'))
