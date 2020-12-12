# Todo

## Programming

### Importing Data

- [x] `land-ocean_temperature_index.csv`
    - All columns
    - Import as a dict of TemperatureData and as a DataFrame.
- [x] `regional-snowfall-index_c20170317.csv`
    - Region
    - Year
    - ~~Start~~
    - ~~End~~
    - RSI
    - ~~Category~~
    - Pandas maybe, if it works for us, otherwise something with dataclasses.

### Visualization

- [x] Figure out how to use https://plotly.com/python/mapbox-density-heatmaps/
    - ~~We want to go through the years showing snowfall RSI, with a heat bar/value on the side.~~
    - Determined that the goal above was infeasible and instead showed temperature on the slider values.
    - [ ] ~~Figure out how to add fade and duration to transitions, if possible.~~
        - Wasn't able to figure out if it was possible.
- [x] Line graph of average totals over time, if we have time after?
- [x] Add regression function for Overall Mean RSI and Temperature.
    - [ ] Fix titles
    - [ ] Separate by region
