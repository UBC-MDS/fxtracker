# Authors: Sarah Abdelazim, Markus Nam, Crystal Geng, Lennon Au-Yeung
# Date: Jan 13, 2023

import datetime
import pandas as pd
# import pandas_datareader as pdr
import altair as alt
import numpy as np
import yfinance as yf


def fx_rate_lookup(curr, target_px):
    """
    Return the first date (reverse chronological order) on which the target price falling between day high and day low based on the availability of data.
    
    Parameters
    ----------
    curr : string 
        Ticker of the currency pair such as 'EURUSD'.
    target_px : float
        Target price for the lookup.
    
    Returns
    --------
    date: string
        The closest date in YYYY-MM-DD on which the target price falling between day high and day low.

    
    Examples
    --------
    >>> fx_rate_lookup('EURUSD', 1.072)
        '2023-01-10'
    """
    
    df = yf.download(curr + '=X', progress=False, show_errors=False)
    if len(df) == 0:
        raise Exception('No data found from data source. Check your ticker.')
    
    # A query to check if the input price is within the High and Low of any previous days.
    myquery = 'High >= ' + str(target_px) + 'and Low <= ' + str(target_px)
    mydates = df.query(myquery).index.format()
    
    # Found, return the latest one (closest to the query date)
    if len(mydates) > 0:
        return mydates[-1]
    else:
        raise Exception('Target price not found. Adjust your target price.')