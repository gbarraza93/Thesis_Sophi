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

    global_data_frame = pd.DataFrame()
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
                day_path = os.path.join(month_path, day)
                # day_folders = os.listdir(day_path)
                # print(day_folders)
                date_format = day.replace("_", "")  # getting date format as YYYYMMDD
                # Characteristics directory
                characteristics_directory = os.path.join(
                    day_path, ND.CHARACTERISTICS_DIR
                )
                ################################# Still to complete
                characteristics_file = os.path.join(
                    characteristics_directory,
                    ND.FASTLANE_FILE_PREFIX
                    + "{}".format(date_format)
                    + ND.XML_FILES_ENDING,
                )
                if not os.path.exists(characteristics_file):
                    raise FileNotFoundError(characteristics_file)

                # Getting the CDATA content from the XML file
                cdata = xmlFunc.get_xml_CDATA_from_element_tail(
                    characteristics_file, ND.HEADER
                )
                # Ridding out of unnecessary characters in our data
                clean_cdata = csvFunc.remove_characters(cdata, ["'", '"'])
                # Creating a csv reader object out of the clean data
                myreader = csv.reader(clean_cdata.splitlines(), delimiter=";")
                # Converting csv object back to a list
                list_of_values = csvFunc.remove_empty_rows(myreader)
                # Converting list into a Pandas data frame for easier data managing
                data_frame = pdFunc.convert_data_to_pandas_dataframe(list_of_values)
                # Removing unnecessary timestamps
                useles_timestamps = ["DataTimestampUTC", "SaveTimestampLOCAL"]
                data_frame = pdFunc.drop_selected_columns(useles_timestamps, data_frame)

                # Convert DataTimestampLOCAL to date format
                def to_datatime(dt):
                    return datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")

                data_frame["DataTimestampLOCAL"] = data_frame[
                    "DataTimestampLOCAL"
                ].apply(to_datatime)

                # Separate Date and Time into different columns
                date = [d.date() for d in data_frame["DataTimestampLOCAL"]]
                time = [d.time() for d in data_frame["DataTimestampLOCAL"]]

                data_frame.insert(0, "date", date)
                data_frame.insert(1, "time", time)

                # # Take DataTimestampLOCAL as the index of the table
                # data_frame.set_index('DataTimestampLOCAL', inplace = True)

                # Remove DataTimestampLOCAL since we already split it into date and time
                data_frame = pdFunc.drop_selected_columns(
                    ["DataTimestampLOCAL"], data_frame
                )

                print("Old data frame")
                print(global_data_frame)
                if global_data_frame.empty:
                    global_data_frame = data_frame
                else:
                    # Appending elements to the bottom of the data frame
                    global_data_frame = pd.concat(
                        [global_data_frame, data_frame], ignore_index=True, axis=0
                    )
                print("New dataframe")
                print(global_data_frame)
    # export dataframe to csv
    pdFunc.convert_to_csv("table_with_data_3.csv", global_data_frame)


if __name__ == "__main__":
    main()
