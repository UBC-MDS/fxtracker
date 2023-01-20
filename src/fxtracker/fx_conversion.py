import pandas as pd
import numpy as np
import yfinance as yf
from yfinance import shared

def fx_conversion(curr1, curr2, amt):
    """
    Converts a specific amount of money from current currency (curr1) to desired currency (curr2)
    
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
    ##Tests
    # Check input type of curr1
    if not isinstance(curr1, str):
        raise TypeError("Ticker of the current currency needs to be of str type.")
        
    # Check input type of curr1   
    if not isinstance(curr2, str):
        raise TypeError("Ticker of the desired currency needs to be of str type.")
        
    # Check input type of amt     
    if not isinstance(amt, (int, float)):
        raise TypeError("Amount of money to be converted needs to be a number.")
    
    curr_pair = curr1+curr2+'=X'
    
    data = yf.download(curr_pair, interval='1m', progress=False, show_errors=False)
    
    # Check for invalid ticker name
    if curr_pair in shared._ERRORS and 'symbol may be delisted' in shared._ERRORS[curr_pair] :
        raise NameError("You have entered an invalid foreign ticker! Try again.")
        
    conversion_rate = data['Close'].iloc[-1]
    converted_value = amt * conversion_rate
    
    return converted_value