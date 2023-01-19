# Authors: Sarah Abdelazim, Markus Nam, Crystal Geng, Lennon Au-Yeung
# Date: Jan 18, 2023

import datetime
import pandas as pd
import altair as alt
import numpy as np
import yfinance as yf
from yfinance import shared
import altair_viewer
alt.renderers.enable('mimetype')

def price_trend_viz(curr, start_date, end_date):
    """
    Visualizes trend of the exchange rate of a currency pair between the selected start date and end date.
    
    Parameters
    ----------
    curr : string 
        Ticker of the currency pair such as 'EURUSD'
    start_date : string 
        Start date of the selected period of time
    end_date : string
        End date of the selected period of time

    
    Returns
    --------
    Line plot that shows the trend of the exchange rate of a currency pair over the selected period of time
    
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
     
    # Check if the end date entered is later than 2003-12-01
    if(datetime.datetime.strptime(end_date, "%Y-%m-%d") < datetime.datetime.strptime('2003-12-01', "%Y-%m-%d")):
        raise Exception("No data exists before 2003-12-01, please try again.")
        
    # Check if the start date entered is earlier than or equal to today 
    if(datetime.datetime.strptime(start_date, "%Y-%m-%d") > datetime.datetime.today()):
        raise Exception("You entered a start date later than today, please try again.") 
    
    curr_X = curr +'=X'   
        
    data = yf.download(curr_X, start_date, end_date, progress=False) 
    
    # Raise an exception if the data downloaded has emtpy content
    if len(data) == 0:
        raise Exception('No data found from data source. Check your ticker and date.') 

    
    trend_plot = alt.Chart(
        data.reset_index(), 
        title = f"Trend of Exchange Rate of {curr} from {start_date} to {end_date}"
    ).mark_line(
    ).encode(
        x = alt.X('Date', axis = alt.Axis(format = ("%Y-%m-%d"))),
        y = alt.Y('Close', title = 'Exchange Rate', scale = alt.Scale(zero=False)),
        tooltip = alt.Tooltip('Close',format = '.2%')
    ).properties(height=400, width=800
    ).configure_axis(
        labelFontSize=14,                                       
        titleFontSize=15     
    ).configure_title(
        fontSize=16)

    
    trend_plot.show()
    
    return trend_plot
    