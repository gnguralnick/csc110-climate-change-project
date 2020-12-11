"""CSC110 Project -- Processing Data"""

import temperature_import
import datetime
import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go

SAMPLE_DICT = {'Northeast': 5,
          'Northern Rockies and Plains': 6,
          'Ohio Valley': 7,
          'South': 8,
          'Southeast': 9,
          'Upper Midwest': 10}


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


def show_plotted_dict(data: dict) -> None:
    """asdf"""
    states = []
    [states.extend(REGIONS[region]) for region in data]
    colors = []
    [colors.extend([data[region]] * len(REGIONS[region])) for region in data]

    # fig = make_subplots(rows=1, cols=2,
    #                     specs=[[{'type': 'xy'}, {'type': 'xy'}]],
    #                     subplot_titles=('Title1 1', 'Title 2'))

    fig = px.choropleth(locations=states, locationmode="USA-states", scope='usa', color=colors)
    # fig.add_scatter(x=[20, 30, 40], y=[50, 60, 70])

    # temps = import_as_dict('../data/land-ocean_temperature_index/land-ocean_temperature_index.csv')
    #
    # fig.add_trace(
    #     go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
    #     row=1, col=1
    # )
    #
    # fig.add_trace(
    #     go.Scatter(x=list(temps.keys()), y=[temps[year].raw for year in temps]),
    #     row=1, col=2
    # )
    # fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")

    steps = []
    for i in range(len(fig.data)):
        step = dict(
            method="update",
            args=[{"title": "Slider switched to step: " + str(i)}],  # layout attribute
        )
        steps.append(step)

    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Frequency: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(title_text='test', sliders=sliders)
    fig.show()


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


show_animated_df(SAMPLE_SNOWFALL_DATAFRAME, temperature_import.import_as_dataframe('../data/land-ocean_temperature_index/land-ocean_temperature_index.csv'))
