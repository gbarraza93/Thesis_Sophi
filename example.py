from datetime import datetime
import pandas as pd
import pandas_dataframes_functions as pdFunc

date_time_str = "2018-06-29 08:15:27"
date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")

print("Date:", date_time_obj.date())
print("Time:", date_time_obj.time())
print("Date-time:", date_time_obj)

dictionary = {
    "A": ["1", "2", "3"],
    "B": ["4", "5", "6"],
    "C": ["10", "20", "30"],
    "D": ["40", "50", "60"],
}

data_frame = pd.DataFrame(dictionary)
data_frame = data_frame[["A", "D"]]

print(data_frame)

trades = pd.DataFrame(
    {
        "time": pd.to_datetime(
            [
                "20160525 13:30:00.023",
                "20160525 13:30:00.038",
                "20160525 13:30:00.048",
                "20160525 13:30:00.048",
                "20160525 13:30:00.048",
            ]
        ),
        "price": [51.95, 51.95, 720.77, 720.92, 98.00],
        "quantity": [75, 155, 100, 100, 100],
    },
    columns=["time", "price", "quantity"],
)

quotes = pd.DataFrame(
    {
        "time": pd.to_datetime(
            [
                "20160525 13:30:00.023",
                "20160525 13:30:00.023",
                "20160525 13:30:00.030",
                "20160525 13:30:00.041",
                "20160525 13:30:00.048",
                "20160525 13:30:00.049",
                "20160525 13:30:00.072",
                "20160525 13:30:00.075",
            ]
        ),
        "bid": [720.50, 51.95, 51.97, 51.99, 720.50, 97.99, 720.50, 52.01],
        "ask": [720.93, 51.96, 51.98, 52.00, 720.93, 98.01, 720.88, 52.03],
    },
    columns=["time", "bid", "ask"],
)

df_merge_asof_tolerance = pdFunc.merge_dataframes_on_fist_smaller(
    trades, quotes, "time", tol="1ms"
)

print(df_merge_asof_tolerance)
