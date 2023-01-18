from fxtracker.fx_rate_lookup import fx_rate_lookup  # need to change after we combine the .py into one single .py
import pandas as pd
import datetime
import pytest

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
    