from fxtracker.pl_trend_viz import *

import altair as alt
import pytest
from pytest import raises
import pandas as pd

def test_pl_trend_viz():
    
    # Invalid input for start date
    with raises(ValueError) as error_start_date:
        pl_trend_viz("EURUSD", "20200101", "2022-01-10")

    # Invalid input for end date
    with raises(ValueError) as error_end_date:
        pl_trend_viz("EURUSD", "2020-01-01", "20220110")

    # End date is ealier than start date
    with raises(ValueError) as error_end_date:
        pl_trend_viz("EURUSD", "2022-01-01", "2020-01-10")
        
    output = pl_trend_viz("EURUSD", "2020-01-01", "2022-01-01")
    assert type(output) == alt.vegalite.v4.api.Chart, "Altair chart object should be returned."