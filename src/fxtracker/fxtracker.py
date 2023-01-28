# Authors: Sarah Abdelazim, Markus Nam, Crystal Geng, Lennon Au-Yeung
# Date: January, 2023

# import pandas_datareader as pdr
import yfinance as yf
import altair as alt
from yfinance import shared
import datetime
alt.renderers.enable('mimetype')


def fx_rate_lookup(curr, target_px):
    """
    Return the first date (reverse chronological order) on which
    the target price falling between day high and
    day low based on the availability of data.

    Parameters
    ----------
    curr : string
        Ticker of the currency pair such as 'EURUSD'.
    target_px : float
        Target price for the lookup.

    Returns
    --------
    date: string
        The closest date in YYYY-MM-DD on which the target
        price falling between day high and day low.

    Examples
    --------
    >>> fx_rate_lookup('EURUSD', 1.072)
        '2023-01-10'
    """

    # check input type of curr
    if not isinstance(curr, str):
        raise TypeError("curr needs to be of str type.")

    # Check input type of target_px
    if not isinstance(target_px, (int, float)):
        raise TypeError("target_px needs to be a number.")

    df = yf.download(curr + '=X', progress=False, show_errors=False)
    if len(df) == 0:
        raise Exception('No data found from data source. Check your ticker.')

    # To check if the input price is within the High and Low of any previous
    # days.
    myquery = 'High >= ' + str(target_px) + 'and Low <= ' + str(target_px)
    mydates = df.query(myquery).index.format(
        formatter=lambda x: x.strftime('%Y-%m-%d'))

    # Found, return the latest one (closest to the query date)
    if len(mydates) > 0:
        return mydates[-1]
    else:
        raise Exception('Target price not found. Adjust your target price.')


def pl_trend_viz(curr, start_date, end_date, chart_type):
    """
    Visualizes trend of the profit and loss of a
    currency pair between the selected start date and end date.

    Parameters
    ----------
    curr : string
        Ticker of the currency pair such as 'EURUSD'
    start_date : string
        Start date of the selected period of time
    end_date : string
        End date of the selected period of time
    chart_type: string
        Type of visulization

    Returns
    --------
    Line plot that shows the trend of the profit and
    loss of a currency pair over the selected period of time

    Examples
    --------
    >>> pl_trend_viz('EURUSD', '2018-12-31', '2022-12-31','line')
    """
    shared._ERRORS = {}

    # check input type of curr
    if not isinstance(curr, str):
        raise TypeError("curr needs to be of str type.")

    curr_X = curr + '=X'

    # Check input type of start_date
    if not isinstance(start_date, str):
        raise TypeError("start_date needs to be of str type.")

    # Check input type of end_date
    if not isinstance(end_date, str):
        raise TypeError("end_date needs to be of str type.")

    # Check type of visulization
    if chart_type not in ['line', 'area']:
        raise ValueError(
            "Your option of plotting should be from 'line' or 'area'")

    # Assert end date is later than start date
    format = "%Y-%m-%d"
    if (datetime.datetime.strptime(end_date, format)
       < datetime.datetime.strptime(start_date, format)):
        raise ValueError(
            "The end date is earlier than the start date! Try again.")

    data = yf.download(curr_X, start_date, end_date)

    if (curr_X in shared._ERRORS and
            'symbol may be delisted' in shared._ERRORS[curr_X]):
        raise NameError(
            "You have entered an invalid foreign ticker! Try again.")

    drop = {'Open', 'High', 'Low', 'Adj Close', 'Volume'}
    data = data.drop(columns=drop)

    for i in range(1, len(data)):
        data.iloc[i, :] = round(
            (data.iloc[i, :] - data.iloc[0, :]) / data.iloc[0, :], 3)

    data.iloc[0, :] = round(
        (data.iloc[0, :] - data.iloc[0, :]) / data.iloc[0, :], 3)

    data = data.rename(columns={"Close": "Percentage Change"})

    title = 'Profit and loss trend over time for currency ' + curr

    if chart_type == 'line':
        chart = alt.Chart(data.reset_index(), title=title).mark_line().encode(
            x=alt.X('Date'),
            y=alt.Y('Percentage Change', axis=alt.Axis(format='%')),
            tooltip=alt.Tooltip('Percentage Change', format='.2%')
        )
    else:
        chart = alt.Chart(data.reset_index(), title=title).mark_area().encode(
            x=alt.X('Date'),
            y=alt.Y('Percentage Change', axis=alt.Axis(format='%')),
            tooltip=alt.Tooltip('Percentage Change', format='.2%')
        )

    # chart.show()

    return chart


def price_trend_viz(curr, start_date, end_date, option):
    """
    Visualizes trend of the exchange rate of a
    currency pair between the selected start date and end date.

    Parameters
    ----------
    curr : string
        Ticker of the currency pair such as 'EURUSD'
    start_date : string
        Start date of the selected period of time
    end_date : string
        End date of the selected period of time
    option: string
        A choice of option from ['Open', 'High', 'Low', 'Close']

    Returns
    --------
    Line plot that shows the trend of the exchange rate of
    a currency pair over the selected period of time

    Examples
    --------
    >>> price_trend_viz('EURUSD', '2018-12-31', '2022-12-31')
    """

    # Check input type of curr
    if not isinstance(curr, str):
        raise TypeError("curr needs to be of str type.")

    # Check input type of start_date
    if not isinstance(start_date, str):
        raise TypeError("start_date needs to be of str type.")

    # Check input type of end_date
    if not isinstance(end_date, str):
        raise TypeError("end_date needs to be of str type.")

    if option not in ['Open', 'High', 'Low', 'Close']:
        raise Exception(
            "Your option of plotting should be "
            "from 'Open', 'High', 'Low' or 'Close'")

    # Check if the end date entered is later than 2003-12-01
    if (datetime.datetime.strptime(end_date, "%Y-%m-%d")
            < datetime.datetime.strptime('2003-12-01', "%Y-%m-%d")):
        raise Exception("No data exists before 2003-12-01, please try again.")

    # Check if the start date entered is earlier than or equal to today
    if (datetime.datetime.strptime(start_date, "%Y-%m-%d")
            > datetime.datetime.today()):
        raise Exception(
            "You entered a start date later than today, please try again.")

    curr_X = curr + '=X'

    data = yf.download(curr_X, start_date, end_date, progress=False)

    # Raise an exception if the data downloaded has emtpy content
    if len(data) == 0:
        raise Exception(
            'No data found from data source. Check your ticker and date.')

    line_1 = f"Trend of Exchange Rate (Daily {option})"
    line_2 = f" of {curr} from {start_date} to {end_date}"

    trend_plot = alt.Chart(
        data.reset_index(),
        title=line_1+line_2
    ).mark_line(
    ).encode(
        x=alt.X('Date', axis=alt.Axis(format=("%Y-%m-%d"))),
        y=alt.Y(option, title='Exchange Rate', scale=alt.Scale(zero=False)),
        tooltip=alt.Tooltip(option, format='.2%')
    ).properties(height=400, width=600
                 ).configure_axis(
        labelFontSize=14,
        titleFontSize=15
    ).configure_title(
        fontSize=16)

    # trend_plot.show()

    return trend_plot


def fx_conversion(curr1, curr2, amt):
    """
    Converts a specific amount of money from current
    currency (curr1) to desired currency (curr2)

    Parameters
    ----------
    curr1 : string
        Ticker of the current currency such as 'EUR'
    curr2 : string
        Ticker of the desired currency to convert to such as 'USD'
    amt : int or float
        amount of money to be converted

    Returns
    --------
    Amount of value converted from currency 1 to currency 2

    Examples
    --------
    >>> fx_conversion('EUR', 'USD', 150.75)
    """
    shared._ERRORS = {}
    # Tests
    # Check input type of curr1
    if not isinstance(curr1, str):
        raise TypeError(
            "Ticker of the current currency needs to be of str type.")

    # Check input type of curr1
    if not isinstance(curr2, str):
        raise TypeError(
            "Ticker of the desired currency needs to be of str type.")

    # Check input type of amt
    if not isinstance(amt, (int, float)):
        raise TypeError(
            "Amount of money to be converted needs to be a number.")

    curr_pair = curr1 + curr2 + '=X'

    data = yf.download(
        curr_pair,
        interval='1m',
        progress=False,
        show_errors=False)

    # Check for invalid ticker name
    if (curr_pair in shared._ERRORS and
            'symbol may be delisted' in shared._ERRORS[curr_pair]):
        raise NameError(
            "You have entered an invalid foreign ticker! Try again.")

    conversion_rate = data['Close'].iloc[-1]
    converted_value = amt * conversion_rate

    return converted_value
