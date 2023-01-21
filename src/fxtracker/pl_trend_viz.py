# Authors: Sarah Abdelazim, Markus Nam, Crystal Geng, Lennon Au-Yeung
# Date: Jan 13, 2023

import datetime
import pandas as pd
import altair as alt
import numpy as np
import yfinance as yf
from yfinance import shared
import altair_viewer
alt.renderers.enable('mimetype')

def pl_trend_viz(curr, start_date, end_date, chart_type):
    """
    Visualizes trend of the profit and loss of a currency pair between the selected start date and end date.
    
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
    Line plot that shows the trend of the profit and loss of a currency pair over the selected period of time
    
    Examples
    --------
    >>> pl_trend_viz('EURUSD', '2018-12-31', '2022-12-31','line')
    """
    shared._ERRORS = {}
    curr_X = curr +'=X'
    
    #check input type of curr
    if not isinstance(curr, str):
        raise TypeError("curr needs to be of str type.")
        
    # Check input type of start_date     
    if not isinstance(start_date, str):
        raise TypeError("start_date needs to be of str type.")
        
    # Check input type of end_date  
    if not isinstance(end_date, str):
        raise TypeError("end_date needs to be of str type.")
    
    #Check type of visulization
    if chart_type not in ['line', 'area']:
        raise ValueError("Your option of plotting should be from 'line' or 'area'")

    # Assert end date is later than start date
    format = "%Y-%m-%d"
    if(datetime.datetime.strptime(end_date, format) < datetime.datetime.strptime(start_date, format)):
        raise ValueError("You have entered an end date which is earlier than the start date! Try again.")
    
    data = yf.download(curr_X, start_date, end_date)
    
    if curr_X in shared._ERRORS and 'symbol may be delisted' in shared._ERRORS[curr_X] :
        raise NameError("You have entered an invalid foreign ticker! Try again.")
    
    drop = {'Open', 'High', 'Low', 'Adj Close', 'Volume'}
    data = data.drop(columns = drop)
    
    for i in range(1,len(data)):
        data.iloc[i,:] = round((data.iloc[i,:] - data.iloc[0,:])/data.iloc[0,:], 3)
    
    data.iloc[0,:] = round((data.iloc[0,:] - data.iloc[0,:])/data.iloc[0,:], 3)
    
    data = data.rename(columns={"Close": "Percentage Change"})
    
    title = 'Price trend over time for currency ' + curr
    
    if chart_type == 'line':
        chart = alt.Chart(data.reset_index(),title = title).mark_line().encode(
            x = alt.X('Date'),
            y = alt.Y('Percentage Change',axis=alt.Axis(format='%')),
            tooltip = alt.Tooltip('Percentage Change',format = '.2%')
        )
    else:
        chart = alt.Chart(data.reset_index(),title = title).mark_area().encode(
            x = alt.X('Date'),
            y = alt.Y('Percentage Change',axis=alt.Axis(format='%')),
            tooltip = alt.Tooltip('Percentage Change',format = '.2%')
        )
    
    chart.show()
    
    return chart