# fxtracker

This is a package created as a group project for DSCI_524 Collaborative Software Development of UBC Master of Data Science (MDS) program 2022-2023. Based on the foreign exchange data in Yahoo Finance, this package allows user to perform currency conversion based on the latest available exchange rate, lookup a target exchange rate from historical data as well plotting exchange rate history and profit/loss percentage history by specifying a currency pair (and other input parameters).

## Function Description
- `fx_conversion` <br>
  Convert the input amount of currency 1 to currency 2 based on the latest available exchange rate.
- `fx_rate_lookup` <br>
  Lookup for the date of the first occurence (in reverse chronological order) on which the input target rate of a currency pair is within the day's high/low.
- `price_trend_viz` <br>
  Plot the historical exchange rate of the input currency pair for a specific period of time.
- `pl_trend_viz` <br>
  Plot the historical profit/loss percentage of the input currency pair for a specific period of time.

There is a python package ([`forex-python`](https://pypi.org/project/forex-python/)) relevant to foreign exchange. That package is basically for retrieving exchange rates and bitcoin prices in plain text as well as performing conversion. It does not provide visualizations and lookup function like `fxtracker` does. `fxtracker` allows user to visualize the trends and understand if a target price of a currency pair of interest is within a reasonable range.

## Installation

```bash
$ pip install fxtracker
```

## Usage

- This section will be updated in later milestones.

## Dependencies

  - pandas
  - pandas-datareader
  - altair
  - numpy
  - plotly
  - yfinance
## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`fxtracker` was created by Sarah Abdelazim, Markus Nam, Crystal Geng and Lennon Au-Yeung. It is licensed under the terms of the MIT license.

## Credits

`fxtracker` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
