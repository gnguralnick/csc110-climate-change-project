"""CSC110 Project -- Visualizing Data"""

from typing import List
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import process


REGIONS = {'Northeast': ['PA', 'NY', 'ME', 'MA', 'CT', 'RI', 'VT', 'NJ', 'DE', 'MD', 'NH'],
           'Northern Rockies and Plains': ['MT', 'ND', 'SD', 'WY', 'NE'],
           'Ohio Valley': ['MO', 'IL', 'TN', 'WV', 'OH', 'IN', 'KY'],
           'South': ['KS', 'OK', 'MS', 'TX', 'AR', 'LA'],
           'Southeast': ['VA', 'NC', 'SC', 'AL', 'GA', 'FL'],
           'Upper Midwest': ['MN', 'IA', 'WI', 'MI']}


def show_animated_choropleth(snowfall: pd.DataFrame, temperature: pd.DataFrame,
                             rsi_color_scale_range: List[float]) -> None:
    """Show an animated choropleth of snowfall vs temperature over time.
    """
    min_year = snowfall['Year'].min()
    max_year = snowfall['Year'].max()

    title = 'US Central and Eastern Yearly Mean RSI by Region vs. Global Land-Ocean Temperature ' \
            'Index From ' + str(int(min_year)) + ' to ' + str(int(max_year))

    fig = px.choropleth(data_frame=snowfall, locations='State', locationmode="USA-states",
                        scope='usa', animation_frame='Year', animation_group='State',
                        color='RSI', range_color=rsi_color_scale_range, title=title,
                        labels={'Region': 'Region'})

    fig['layout']['sliders'][0]['currentvalue']['prefix'] = 'Year, Temp='

    for step in fig['layout']['sliders'][0]['steps']:
        step['label'] = str(int(float(step['label']))) + ', ' + str(
            temperature.query('Year == ' + step['label']).iloc[0]['Raw'])

    fig.show()


def show_year_comparison_scatterplot(snowfall: pd.DataFrame, temperature: pd.DataFrame,
                                     rsi_axis_range: List[float]) -> None:
    """Show a scatterplot with lowess trendlines for each individual region, the average of the
    regions, and the temperature.
    """
    min_year = snowfall['Year'].min()
    max_year = snowfall['Year'].max()

    fig = make_subplots(specs=[[{'secondary_y': True}]])

    swatch_index = 0

    for region in snowfall['Region'].drop_duplicates():
        fig.add_trace(
            go.Scatter(x=snowfall.query('Region == "' + region + '"')['Year'],
                       y=snowfall.query('Region == "' + region + '"')['RSI'],
                       name=region, mode='markers',
                       line={'color': px.colors.qualitative.Plotly[swatch_index % len(px.colors.qualitative.Plotly)]}),
            secondary_y=False
        )
        trendline = process.lowess(snowfall.query('Region == "' + region + '"'), 'Year',
                                          'RSI')
        fig.add_trace(
            go.Scatter(x=trendline['Year'],
                       y=trendline['RSI'],
                       name=region + ' Trendline', mode='lines',
                       line={'color':
                                 px.colors.qualitative.Plotly[swatch_index %
                                                              len(px.colors.qualitative.Plotly)]}),
            secondary_y=False
        )
        swatch_index += 1

    snowfall_mean = snowfall.groupby(['Year'], as_index=False)[['RSI']].mean()
    snowfall_mean_trendline = process.lowess(snowfall_mean, 'Year', 'RSI')

    fig.add_trace(
        go.Scatter(x=snowfall_mean_trendline['Year'],
                   y=snowfall_mean_trendline['RSI'],
                   name='Overall Mean Trendline', mode='lines',
                   line={'color': px.colors.qualitative.Plotly[swatch_index %
                                                               len(px.colors.qualitative.Plotly)]}),
        secondary_y=False
    )

    swatch_index += 1

    fig.add_trace(
        go.Scatter(x=temperature['Year'], y=temperature['Raw'], name='Temperature',
                   mode='markers',
                   line={'color': px.colors.qualitative.Plotly[swatch_index %
                                                               len(px.colors.qualitative.Plotly)]}),
        secondary_y=True
    )
    temperature_trendline = process.lowess(temperature, 'Year', 'Raw')
    fig.add_trace(
        go.Scatter(x=temperature_trendline['Year'],
                   y=temperature_trendline['Raw'],
                   name='Temperature Trendline', mode='lines',
                   line={'color': px.colors.qualitative.Plotly[swatch_index %
                                                               len(px.colors.qualitative.Plotly)]}),
        secondary_y=True
    )

    fig['layout']['yaxis']['range'] = rsi_axis_range

    fig['layout']['xaxis']['title']['text'] = 'Year'
    fig['layout']['yaxis']['title']['text'] = 'RSI'
    fig['layout']['yaxis2']['title']['text'] = 'Degrees Celsius'

    title = 'US Central and Eastern Yearly Mean RSI and Global Land-Ocean Temperature Index From ' \
            + str(int(min_year)) + ' to ' + str(int(max_year))
    fig['layout']['title']['text'] = title

    fig.show()


def show_correlation_scatterplot(snowfall: pd.DataFrame, temperature: pd.DataFrame,
                                 rsi_axis_range: List[float]) -> None:
    min_year = snowfall['Year'].min()
    max_year = snowfall['Year'].max()

    snowfall_with_temps = process.add_year_temps(snowfall, temperature)

    title = 'US Central and Eastern Yearly Mean RSI vs. Global Land-Ocean Temperature Index From ' \
            + str(int(min_year)) + ' to ' + str(int(max_year))

    fig = go.Figure()

    fig.update_layout(title={'text': title})
    fig.update_xaxes({'title': {'text': 'Degrees Celsius'}})
    fig.update_yaxes({'title': {'text': 'RSI'}})
    fig.update_yaxes({'range': rsi_axis_range})

    swatch_index = 0

    for region in snowfall['Region'].drop_duplicates():
        fig.add_trace(
            go.Scatter(x=snowfall_with_temps.query('Region == "' + region + '"')['Temperature'],
                       y=snowfall_with_temps.query('Region == "' + region + '"')['RSI'],
                       name=region, mode='markers',
                       line = {'color': px.colors.qualitative.Plotly[swatch_index %
                                                      len(px.colors.qualitative.Plotly)]}))
        regional_trendline =\
            process.lowess(snowfall_with_temps.query('Region == "'
                                                     + region + '"'), 'Temperature', 'RSI')
        fig.add_trace(
            go.Scatter(x=regional_trendline['Temperature'],
                       y=regional_trendline['RSI'],
                       name=region + ' Trendline', mode='lines',
                       line={'color':
                             px.colors.qualitative.Plotly[swatch_index % len(
                                 px.colors.qualitative.Plotly)]}))

        swatch_index += 1

    snowfall_mean = snowfall.groupby(['Year'], as_index=False)[['RSI']].mean()

    snowfall_mean_with_temps = process.add_year_temps(snowfall_mean, temperature)

    fig.add_trace(
        go.Scatter(x=snowfall_mean_with_temps['Temperature'],
                   y=snowfall_mean_with_temps['RSI'],
                   name='Overall Mean', mode='markers',
                   line = {'color': px.colors.qualitative.Plotly[swatch_index % len(
                               px.colors.qualitative.Plotly)]}))

    snowfall_mean_trendline = process.lowess(snowfall_mean_with_temps, 'Temperature', 'RSI')

    fig.add_trace(
        go.Scatter(x=snowfall_mean_trendline['Temperature'],
                   y=snowfall_mean_trendline['RSI'],
                   name='Overall Mean Trendline', mode='lines',
                   line = {'color': px.colors.qualitative.Plotly[swatch_index % len(
                                   px.colors.qualitative.Plotly)]}))

    fig.show()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'pandas', 'plotly.express', 'process'],
        'allowed-io': ['import_as_dict'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
