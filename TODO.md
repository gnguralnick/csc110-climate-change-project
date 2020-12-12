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

### Cleanup

- [ ] Create `requirements.txt` files with all required modules.
- [ ] Make sure module titles and descriptions are in a similar format to the code we were given by the profs, and adapt it to claim copyright on our work?
- [ ] Finish docstrings, preconditions, and representation invariants for **all functions**.
	- Make doctests where appropriate, bough they are not required.
- [ ] Make sure all files have been checked by python_ta by running them as main, and that no doctests are failing, also see if we can figure out that recursion error with python_ta in the main module.
