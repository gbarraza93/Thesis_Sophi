import namesDictionary as ND
import pandas as pd
import pandas_dataframes_functions as pdFunc
import csv_functionalities as csvFunc
import os


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
                date_format = day.replace("_", "")  # getting date format as YYYYMMDD

                # SECTION 1: Fast Lane Characteristics files
                # Characteristics directory
                characteristics_directory = os.path.join(
                    day_path, ND.CHARACTERISTICS_DIR
                )
                # FastlaneCharacteristics file
                characteristics_file = os.path.join(
                    characteristics_directory,
                    ND.FASTLANE_FILE_PREFIX
                    + "{}".format(date_format)
                    + ND.XML_FILES_ENDING,
                )
                if not os.path.exists(characteristics_file):
                    raise FileNotFoundError(characteristics_file)

                characteristics_reader = csvFunc.create_csv_reader(characteristics_file)

                characteristics_table_list = csvFunc.to_table_list_without_empty_values(
                    characteristics_reader
                )

                characteristics_data_frame = pdFunc.create_general_dataframe_from_table(
                    characteristics_table_list
                )

                main_data_frame = (
                    characteristics_data_frame  # This is the main dataframe per day
                )
                # SECTION 2: Typ_AQZustandArchiv files

                # Typ_Archiv directory
                typ_archive_directory = os.path.join(day_path, ND.TYP_ARCHIVE_DIR)
                for arch_file_prefix in ND.GREEN_FILES_PREFIX:
                    arch_file_name = (
                        arch_file_prefix
                        + "{}".format(date_format)
                        + ND.XML_FILES_ENDING
                    )
                    archive_file = os.path.join(typ_archive_directory, arch_file_name)
                    if not os.path.exists(archive_file):
                        continue  # if file is not found, continue with next one

                    archive_reader = csvFunc.create_csv_reader(archive_file)

                    archive_table_list = csvFunc.to_table_list_without_empty_values(
                        archive_reader
                    )

                    archive_data_frame = pdFunc.create_general_dataframe_from_table(
                        archive_table_list
                    )

                    if any(
                        arch_file_prefix in file_pfx
                        for file_pfx in ND.GREEN_FILES_PREFIX_BATCH_1
                    ):
                        # drop all the columns except for the date, time and C_Actors_0_Reason
                        archive_data_frame = pdFunc.drop_all_columns_except(
                            ["DataTimestampLOCAL", "C_Actors_0_Reason"],
                            archive_data_frame,
                        )
                    else:
                        # if file is found in GREEN_FILES_PREFIX_BATCH_2
                        # drop all the columns except for the date, time and C_Actors_1_Reason
                        archive_data_frame = pdFunc.drop_all_columns_except(
                            ["DataTimestampLOCAL", "C_Actors_1_Reason"],
                            archive_data_frame,
                        )
                    # Here is where we add the columns that correspond to the discrete data
                    # (i.e. those incidents reported only at specific times)
                    main_data_frame = (
                        pdFunc.merge_dataframes_on_fist_smaller(
                            main_data_frame,
                            archive_data_frame,
                            "DataTimestampLOCAL",
                            tol="60s",
                        )
                        .apply(pdFunc.propagate_values_until_next)
                        .apply(pdFunc.fill_NaN_with_default)
                    )  # propagate the values of one occurrence until a new one and fill with "default" the remaining

                # SECTION 3: RhoStruct files

                if global_data_frame.empty:
                    global_data_frame = main_data_frame
                else:
                    # Appending elements to the bottom of the data frame
                    global_data_frame = pd.concat(
                        [global_data_frame, main_data_frame], ignore_index=True, axis=0,
                    )
    # export dataframe to csv
    pdFunc.convert_to_csv("table_with_data_4.csv", global_data_frame)


if __name__ == "__main__":
    main()
