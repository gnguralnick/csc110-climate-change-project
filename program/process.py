"""CSC110 Project -- Processing Data"""

from snowfall_import import SnowfallData
from temperature_import import TemperatureData, import_as_dict
import datetime
import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go

SAMPLE = {'Northeast': 5,
          'Northern Rockies and Plains': 6,
          'Ohio Valley': 7,
          'South': 8,
          'Southeast': 9,
          'Upper Midwest': 10}


REGIONS = {'Northeast': ['PA', 'NY', 'ME', 'MA', 'CT', 'RI', 'VT', 'NJ', 'DE', 'MD', 'NH'],
           'Northern Rockies and Plains': ['MT', 'ND', 'SD', 'WY', 'NE'],
           'Ohio Valley': ['MO', 'IL', 'TN', 'WV', 'OH', 'IN', 'KY'],
           'South': ['KS', 'OK', 'MS', 'TX', 'AR', 'LA'],
           'Southeast': ['VA', 'NC', 'SC', 'AL', 'GA', 'FL'],
           'Upper Midwest': ['MN', 'IA', 'WI', 'MI']}

# def yearly_regional_rsi_sum(Dict[datetime.date, SnowfallData]) -> :


def show_plot(data: dict) -> None:
    """asdf"""
    states = []
    [states.extend(REGIONS[region]) for region in data]
    colors = []
    [colors.extend([data[region]] * len(REGIONS[region])) for region in data]

    fig = make_subplots(rows=1, cols=2,
                        specs=[[{'type': 'xy'}, {'type': 'xy'}]],
                        subplot_titles=('Title1 1', 'Title 2'))

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