import pandas as pd
from typing import List
from datetime import datetime

"""
    Converts a list of lists into a Pandas DataFrame in order to easily access columns of the data.
    Takes the first row of the list and takes it as the Header (or columns name)
    
    :returns pandas DataFrame
"""


def convert_data_to_pandas_dataframe(data: List[List[str]]):
    df = pd.DataFrame.from_records(data)
    new_header = df.iloc[0]  # grab the first row for the header
    df = df[1:]  # take all the data except the header row
    df.columns = new_header  # set the header row as the df header
    return df


def convert_to_csv(file_name: str, pandas_dataframe):
    pandas_dataframe.to_csv(file_name, sep=";", index=True, index_label=None)


def drop_selected_columns(columns_to_delete: List[str], pandas_dataframe):
    return pandas_dataframe.drop(columns_to_delete, axis=1)


def drop_all_columns_except(columns_to_keep: List[str], pandas_dataframe):
    return pandas_dataframe[columns_to_keep]


def rename_columns_in_dataframe(data_frame, old_names: List[str], new_names: List[str]):
    names_dictionary = dict(zip(old_names, new_names))
    data_frame.rename(columns=names_dictionary, inplace=True)


def merge_dataframes_on_nearest(left_df, right_df, timestamp, tol: str = "0"):
    return pd.merge_asof(
        left_df,
        right_df,
        on=timestamp,
        direction="nearest",
        tolerance=pd.Timedelta(tol),
    )


def merge_dataframes_on_fist_smaller(left_df, right_df, tol: str = "0"):
    return pd.merge_asof(
        left_df,
        right_df,
        left_index=True,
        right_index=True,
        direction="backward",
        tolerance=pd.Timedelta(tol),
    )


def propagate_values_until_next(data_frame):
    return data_frame.ffill(axis=0)


def fill_NaN_with_default(data_frame):
    return data_frame.fillna("default")


def create_general_dataframe_from_table(table_list: List[List[str]]):
    # Converting list into a Pandas data frame for easier data managing
    data_frame = convert_data_to_pandas_dataframe(table_list)
    # Removing unnecessary timestamps
    useles_timestamps = ["DataTimestampUTC", "SaveTimestampLOCAL"]
    data_frame = drop_selected_columns(useles_timestamps, data_frame)

    data_frame["DataTimestampLOCAL"] = data_frame["DataTimestampLOCAL"].apply(
        to_datetime
    )

    # Separate Date and Time into different columns
    date = [d.date() for d in data_frame["DataTimestampLOCAL"]]
    time = [d.time() for d in data_frame["DataTimestampLOCAL"]]

    data_frame.insert(0, "date", date)
    data_frame.insert(1, "time", time)

    # Set DataTimestampLOCAL as index
    data_frame.set_index("DataTimestampLOCAL", inplace=True)

    # Adding month_name and day_name to table
    month_name = data_frame.index.month_name()
    day_name = data_frame.index.day_name()

    # insertamos la columna en la posición 3 (a la derecha de "time")
    data_frame.insert(2, "month_name", month_name)
    # insertamos la columna en la posición 4 (a la derecha de "month_name")
    data_frame.insert(3, "day_name", day_name)

    return data_frame


# Convert DataTimestampLOCAL to date and time format and round to minutes
def to_datetime(dt):
    return datetime.strptime(dt, "%Y-%m-%d %H:%M:%S").replace(second=0)


def subtract_time_str(time: str, to_subtract: str):
    original_time = datetime.strptime(time, "%H:%M:%S")
    minus_time = datetime.strptime(to_subtract, "%H:%M:%S")
    return str(original_time - minus_time)


def add_minutes_to_timestamp_idx(data_frame, minutes: int):
    return data_frame.set_index(
        data_frame.index.values + pd.Timedelta(minutes=minutes), inplace=True
    )
