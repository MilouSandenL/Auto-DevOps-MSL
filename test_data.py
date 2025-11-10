from unittest.mock import patch
import pandas as pd
from datetime import datetime, timedelta
from app import collect_smhi_data

@patch("app.get_smhi_data")
def test_collect_smhi_data_success(mock_get):
    future_time = (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    mock_smhi_json = {
        "timeSeries": [
            {
                "validTime": future_time,
                "parameters": [
                    {"name": "t", "values": [4.9]},
                    {"name": "pcat", "values": [1]}
                ]
            }
        ]
    }
    mock_get.return_value = (mock_smhi_json, "Success")

    df, status = collect_smhi_data(59.3293, 18.0686)

    assert status == "Success"
    assert isinstance(df, pd.DataFrame)
    assert df["Temperature (°C)"].iloc[0] == 5
    assert df["Rain or Snow"].iloc[0] == True