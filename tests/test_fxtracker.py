from fxtracker.fx_rate_lookup import fx_rate_lookup  # need to change after we combine the .py into one single .py
import pandas as pd
import datetime
import pytest
from pytest import raises
import altair as alt

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
