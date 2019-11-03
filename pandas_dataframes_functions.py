import pandas as pd
from typing import List

'''
    Converts a list of lists into a Pandas DataFrame in order to easily access columns of the data.
    Takes the first row of the list and takes it as the Header (or columns name)
    
    :returns pandas DataFrame
'''
def convert_data_to_pandas_dataframe(data: List[List[str]]):
    df = pd.DataFrame.from_records(data)
    new_header = df.iloc[0]  # grab the first row for the header
    df = df[1:]  # take all the data except the header row
    df.columns = new_header  # set the header row as the df header
    return df


def convert_to_csv(file_name: str, pandas_dataframe):
    pandas_dataframe.to_csv(file_name, sep=';', index=False)


def drop_selected_columns(columns_to_delete: List[str], pandas_dataframe):
    pandas_dataframe.drop(columns_to_delete, axis=1)


def drop_all_columns_except(columns_to_keep: List[str], pandas_dataframe):
    return pandas_dataframe[columns_to_keep]