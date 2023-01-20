from fxtracker.fx_rate_lookup import fx_rate_lookup  # need to change after we combine the .py into one single .py
import pandas as pd
import datetime
import pytest
from pytest import raises
import altair as alt
import numpy as np

def test_fx_rate_lookup():
    assert isinstance(pd.to_datetime(fx_rate_lookup('JPYHKD', 0.09)), datetime.datetime), 'Return string should be a valid YYYY-MM-DD format'
        
    with pytest.raises(Exception):
        fx_rate_lookup('AAABBB', 0.09)
    
    with pytest.raises(Exception):
        fx_rate_lookup('JPYHKD', 1)
        
    with pytest.raises(Exception):
        fx_rate_lookup()
        
    with pytest.raises(Exception):
        fx_rate_lookup('JPYHKD')
    
def test_pl_trend_viz():
    
    #Start date invalid
    with raises(ValueError) as start_date_error:
        pl_trend_viz("EURUSD", "20200101", "2022-01-10")

    #End date invalid
    with raises(ValueError) as end_date_error:
        pl_trend_viz("EURUSD", "2020-01-01", "20220110")

    #Start date > end date
    with raises(ValueError) as date_range_error:
        pl_trend_viz("EURUSD", "2022-01-01", "2020-01-10")
        
    with raises(NameError) as error_name:
        pl_trend_viz("ABCD", "2020-01-01", "2022-01-01")
        
    output = pl_trend_viz("EURUSD", "2020-01-01", "2022-01-01")
    assert type(output) == alt.vegalite.v4.api.Chart, "Altair chart object should be returned."
    
    raw = output.to_dict()
    
    assert raw['encoding']['x']['field'] == 'Date', 'Date should be mapped to the x axis'
    
    assert raw['encoding']['y']['field'] == 'Percentage Change', 'Percentage Change should be mapped to the y axis'
    
    assert raw['mark'] == 'line', "Altair mark should be 'line'"

def test_price_trend_viz():
    
    # Check input type of curr
    with pytest.raises(TypeError, match = "curr needs to be of str type."):
        price_trend_viz(1, '2012-02-01', '2014-12-31')
    
    # Check input type of start_date
    with pytest.raises(TypeError, match = "start_date needs to be of str type."):
        price_trend_viz('EURUSD', 2.5, '2014-12-31')
    
    # Check input type of end_date
    with pytest.raises(TypeError, match = "end_date needs to be of str type."):
        price_trend_viz('EURUSD', '2012-02-01', 333)
    
    # Check if the end date entered is later than 2003-12-01
    with pytest.raises(Exception, match = "No data exists before 2003-12-01, please try again."):
        price_trend_viz('EURUSD', '1992-02-01', '1994-12-31')
    
    # Check if the start date entered is earlier than or equal to today 
    with pytest.raises(Exception, match = "You entered a start date later than today, please try again."):
        price_trend_viz('EURUSD', '2023-12-31', '2024-12-31')
    
           
    output_chart = price_trend_viz("EURUSD", "2018-12-01", "2022-12-01")
    
    # Check if an Altair chart is returned
    assert type(output_chart) == alt.vegalite.v4.api.Chart, "Altair chart object should be returned."

def test_fx_conversion():
    
    # Check if a numpy float is returned
    assert isinstance(fx_conversion('EUR', 'USD', 100), np.float64), "Float should be returned."
    
    # Check input type of curr_1
    with pytest.raises(TypeError, match = "Ticker of the current currency needs to be of str type."):
        fx_conversion(1, 'USD', 100)
        
    # Check input type of curr_2
    with pytest.raises(TypeError, match = "Ticker of the desired currency needs to be of str type."):
        fx_conversion('EUR', 1, 100)
        
    # Check input type of amt
    with pytest.raises(TypeError, match = "Amount of money to be converted needs to be a number."):
        fx_conversion('EUR', 'USD', 'a')
    
    # Check if no arguments are passed
    with pytest.raises(TypeError, match=r"^fx_conversion\(\) missing 3 required positional arguments: 'curr1', 'curr2', and 'amt'$"):
        fx_conversion()
        
    # Check if curr_2 and amt arguments are not passed    
    with pytest.raises(TypeError, match=r"^fx_conversion\(\) missing 2 required positional arguments: 'curr2' and 'amt'$"):
        fx_conversion('USD')
        
    # Check if amt argument is not passed
    with pytest.raises(TypeError, match=r"^fx_conversion\(\) missing 1 required positional argument: 'amt'$"):
        fx_conversion('USD', 'EUR')
        
    # Check if wrong ticker(s) is/are passed
    with pytest.raises(NameError, match="You have entered an invalid foreign ticker! Try again."):
        fx_conversion('XXX', 'YYY', 100)
    with pytest.raises(NameError, match="You have entered an invalid foreign ticker! Try again."):
        fx_conversion('USD', 'YYY', 100)
    with pytest.raises(NameError, match="You have entered an invalid foreign ticker! Try again."):
        fx_conversion('XXX', 'EUR', 100)