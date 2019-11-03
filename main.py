import namesDictionary as ND
import pandas as pd
from datetime import datetime
import pandas_dataframes_functions as pdFunc
import XML_parsing_functions as xmlFunc
import csv_functionalities as csvFunc
import csv
import os, sys


def main():
    path = ND.MAIN_DIRECTORY
    files = os.listdir(path)
    # print(sorted(files))
    for year in sorted(files):
        # print(year)
        year_path = os.path.join(path, year)
        year_months = os.listdir(year_path)
        for month in sorted(year_months):
            # print(month)
            month_path = os.path.join(year_path, month)
            month_days = os.listdir(month_path)
            for day in sorted(month_days):
                print(day)
################################# Still to fix
                doc = os.path.join(path, '2018/2018_09/2018_09_18/Typ_AQZustandArchiv/FastLaneTLV.VMS_0603_PRAR_W.AQZustandArchiv.Typ_AQZustandArchiv.20180918.01.xml')
                if not os.path.exists(doc):
                    raise FileNotFoundError(doc)

                # Getting the CDATA content from the XML file
                cdata = xmlFunc.get_xml_CDATA_from_element_tail(doc, ND.HEADER)
                # Ridding out of unnecessary characters in our data
                clean_cdata = csvFunc.remove_characters(cdata, ['\'', '\"'])
                # Creating a csv reader object out of the clean data
                myreader = csv.reader(clean_cdata.splitlines(), delimiter=';')
                # Converting csv object back to a list
                list_of_values = csvFunc.remove_empty_rows(myreader)
                # Converting list into a Pandas data frame for easier data managing
                data_frame = pdFunc.convert_data_to_pandas_dataframe(list_of_values)
                # Removing unnecessary timestamps
                useles_timestamps = ["DataTimestampUTC", "SaveTimestampLOCAL"]
                data_frame = pdFunc.drop_selected_columns(useles_timestamps, data_frame)
                data_frame = data_frame.drop(["DataTimestampUTC", "SaveTimestampLOCAL"], axis=1)


                # Convert DataTimestampLOCAL to date format
                def to_datatime(dt):
                    return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')


                data_frame['DataTimestampLOCAL'] = data_frame['DataTimestampLOCAL'].apply(to_datatime)

                # Separate Date and Time into different columns
                date = [d.date() for d in data_frame['DataTimestampLOCAL']]
                time = [d.time() for d in data_frame['DataTimestampLOCAL']]

                data_frame.insert(0, 'date', date)
                data_frame.insert(1, 'time', time)

                # # Take DataTimestampLOCAL as the index of the table
                # data_frame.set_index('DataTimestampLOCAL', inplace = True)

                # Remove DataTimestampLOCAL since we already split it into date and time
                data_frame = data_frame.drop(['DataTimestampLOCAL'], axis=1)

                # print(data_frame)

                # export dataframe to csv
                pdFunc.convert_to_csv('table_with_data_2.csv', data_frame)


if __name__ == '__main__':
    main()