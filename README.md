[![ci-cd](https://github.com/UBC-MDS/fxtracker/actions/workflows/ci-cd.yml/badge.svg?branch=main)](https://github.com/UBC-MDS/fxtracker/actions/workflows/ci-cd.yml) [![codecov](https://codecov.io/gh/UBC-MDS/fxtracker/branch/main/graph/badge.svg?token=N4sBOXKB87)](https://codecov.io/gh/UBC-MDS/fxtracker) [![Documentation Status](https://readthedocs.org/projects/fxtracker/badge/?version=latest)](https://fxtracker.readthedocs.io/en/latest/?badge=latest)

# fxtracker

This is a package created as a group project for DSCI_524 Collaborative Software Development of UBC Master of Data Science (MDS) program 2022-2023. Based on the foreign exchange data in Yahoo Finance, this package allows user to perform currency conversion based on the latest available exchange rate, lookup a target exchange rate from historical data as well plotting exchange rate history and profit/loss percentage history by specifying a currency pair (and other input parameters).

The full documentation of this package can also be found on <https://fxtracker.readthedocs.io/en/latest/>

## Function Description

-   `fx_conversion` <br> Convert the input amount of currency 1 to currency 2 based on the latest available exchange rate.
-   `fx_rate_lookup` <br> Lookup for the date of the first occurence (in reverse chronological order) on which the input target rate of a currency pair is within the day's high/low.
-   `price_trend_viz` <br> Plot the historical exchange rate of the input currency pair for a specific period of time.
-   `pl_trend_viz` <br> Plot the historical profit/loss percentage of the input currency pair for a specific period of time.

There is a python package ([`forex-python`](https://pypi.org/project/forex-python/)) relevant to foreign exchange. That package is basically for retrieving exchange rates and bitcoin prices in plain text as well as performing conversion. It does not provide visualizations and lookup function like `fxtracker` does. `fxtracker` allows user to visualize the trends and understand if a target price of a currency pair of interest is within a reasonable range.

## Installation

``` bash
$ pip install fxtracker
```

## Usage

If the package is installed successfully, users then need the following nine input parameters:

`curr`, `target_px`, `start_date`, `end_date`, `chart_type`, `option`, `curr1`, `curr2`, `amt`. The output of the functions will be in forms of a datetime string, a float and interactive plots from the "altair" package.

`fxtracker` can be used to convert a specific amount of money from one currency to another, find the the first date on which the target price falling between day high and day low, visualize the trend of the exchange rate of a currency pair and the trend of the profit and loss of a currency pair between the selected start date and end date.

The functions can be imported from the package as follows:

``` python
from fxtracker.fxtracker import fx_conversion
from fxtracker.fxtracker import fx_rate_lookup
from fxtracker.fxtracker import price_trend_viz
from fxtracker.fxtracker import pl_trend_viz
```

### To convert a specific amount of money from current currency (curr1) to desired currency (curr2):

    fx_conversion('EUR', 'USD', 150.75)

163.68

### To look up the first date (reverse chronological order) on which the target price falling between day high and day low based on the availability of data:

    fx_rate_lookup('EURUSD', 1.072)

'2023-01-10'

### To visualize the trend of the exchange rate of a currency pair between the selected start date and end date:

    price_trend_viz('EURUSD', '2018-12-01', '2022-12-01', 'High').show()

![](https://user-images.githubusercontent.com/112665905/215251534-3d452198-23bc-4b42-885c-d76a5ca68f25.png)

### To visualize the trend of the profit and loss of a currency pair between the selected start date and end date:

**If a line chart is specified in the input:**

    pl_trend_viz("EURUSD", "2020-01-01", "2022-01-01", 'line').show()

![](https://user-images.githubusercontent.com/112665905/215251530-8a3cf86f-6854-47b5-b7b4-2ff214e88217.png)

**If an area chart is specified in the input:**

    pl_trend_viz("EURUSD", "2020-01-01", "2022-01-01", 'area').show()

![](https://user-images.githubusercontent.com/112665905/215251527-3381d5de-c776-4b5f-9777-c687b287f089.png)

## Dependencies

-   python = "\^3.9"
-   pandas = "\^1.5.2"
-   altair = "\^4.2.0"
-   numpy = "\^1.24.1"
-   plotly = "\^5.12.0"
-   yfinance = "\^0.2.3"
-   ipykernel = "\^6.20.2"
-   altair-viewer = "\^0.4.0"

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`fxtracker` was created by Sarah Abdelazim, Markus Nam, Crystal Geng and Lennon Au-Yeung. It is licensed under the terms of the MIT license.

## Credits

`fxtracker` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
