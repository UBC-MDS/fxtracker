# Authors: Sarah Abdelazim, Markus Nam, Crystal Geng, Lennon Au-Yeung
# Date: Jan 13, 2023

import datetime
import pandas as pd
import pandas_datareader as pdr
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
    date
        The closest date on which the target price falling between day high and day low.

    
    Examples
    --------
    >>> fx_rate_lookup('EURUSD', 1.072)
        datetime.date(2023, 1, 10)
    """
    pass