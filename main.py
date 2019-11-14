import namesDictionary as ND
import pandas as pd
import pandas_dataframes_functions as pdFunc
import csv_functionalities as csvFunc
import os


def main():
    path = ND.MAIN_DIRECTORY
    files = os.listdir(path)

    global_data_frame = pd.DataFrame()
    for year in sorted(files):
        year_path = os.path.join(path, year)
        year_months = os.listdir(year_path)
        for month in sorted(year_months):
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
                for arch_file_prefix, var_name in ND.GREEN_FILES_PREFIX.items():
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
                            ["C_Actors_0_Reason"], archive_data_frame,
                        )
                        pdFunc.rename_columns_in_dataframe(
                            archive_data_frame, ["C_Actors_0_Reason"], [var_name],
                        )
                    else:
                        # if file is found in GREEN_FILES_PREFIX_BATCH_2
                        # drop all the columns except for the date, time and C_Actors_1_Reason
                        archive_data_frame = pdFunc.drop_all_columns_except(
                            ["C_Actors_1_Reason"], archive_data_frame,
                        )
                        pdFunc.rename_columns_in_dataframe(
                            archive_data_frame, ["C_Actors_1_Reason"], [var_name],
                        )
                    # Here is where we add the columns that correspond to the discrete data
                    # (i.e. those incidents reported only at specific times)
                    main_data_frame = (
                        pdFunc.merge_dataframes_on_fist_smaller(
                            main_data_frame, archive_data_frame, tol="59s",
                        )
                        .apply(pdFunc.propagate_values_until_next)
                        .apply(pdFunc.fill_NaN_with_default)
                    )  # propagate the values of one occurrence until a new one and fill with "default" the remaining

                # SECTION 3: RhoStruct files
                rho_struct_directory = os.path.join(day_path, ND.STRUCTURE_DIR)
                # RED FILES: Current time
                for rs_current_time_file_prefix in ND.RS_FILES_CURRENT_TIME:
                    rs_current_time_file_name = (
                        rs_current_time_file_prefix
                        + "{}".format(date_format)
                        + ND.XML_FILES_ENDING
                    )
                    rs_current_time_file = os.path.join(
                        rho_struct_directory, rs_current_time_file_name
                    )
                    if not os.path.exists(rs_current_time_file):
                        continue  # if file is not found, continue with next one

                    rs_current_time_reader = csvFunc.create_csv_reader(
                        rs_current_time_file
                    )

                    rs_current_time_table_list = csvFunc.to_table_list_without_empty_values(
                        rs_current_time_reader
                    )

                    rs_current_time_data_frame = pdFunc.create_general_dataframe_from_table(
                        rs_current_time_table_list
                    )

                    rs_current_time_data_frame = pdFunc.drop_all_columns_except(
                        [
                            "C_q_Lkw__wert",
                            "C_q_Pkw_wert",
                            "C_q_Kfz_wert",
                            "C_v_Kfz_wert",
                        ],
                        rs_current_time_data_frame,
                    )

                    pdFunc.rename_columns_in_dataframe(
                        rs_current_time_data_frame,
                        [
                            "C_q_Lkw__wert",
                            "C_q_Pkw_wert",
                            "C_q_Kfz_wert",
                            "C_v_Kfz_wert",
                        ],
                        ND.RS_FILES_CURRENT_TIME[rs_current_time_file_prefix],
                    )

                    main_data_frame = pdFunc.merge_dataframes_on_fist_smaller(
                        main_data_frame, rs_current_time_data_frame,
                    )  # adding data from current time

                # RED FILES: Previous time
                for (
                    rs_previous_time,
                    var_names_min,
                ) in ND.RHO_STRUCT_PREVIOUS_TIME.items():
                    rs_previous_time_file_name = (
                        rs_previous_time
                        + "{}".format(date_format)
                        + ND.XML_FILES_ENDING
                    )
                    rs_previous_time_file = os.path.join(
                        rho_struct_directory, rs_previous_time_file_name
                    )
                    if not os.path.exists(rs_previous_time_file):
                        continue  # if file is not found, continue with next one

                    rs_previous_time_reader = csvFunc.create_csv_reader(
                        rs_previous_time_file
                    )

                    rs_previous_time_table_list = csvFunc.to_table_list_without_empty_values(
                        rs_previous_time_reader
                    )

                    rs_previous_time_data_frame = pdFunc.create_general_dataframe_from_table(
                        rs_previous_time_table_list
                    )

                    rs_previous_time_data_frame = pdFunc.drop_all_columns_except(
                        ["C_q_Kfz_wert", "C_v_Kfz_wert"], rs_previous_time_data_frame,
                    )

                    # HERE WE START DOING STUFF FOR THE HANDLING OF THE MINUTES
                    minutes_pattern = ["_15", "_30", "_45", "_60"]
                    for minute in minutes_pattern:
                        # Copy rs_previous_time_data_frame into a new variable per minute pattern
                        rs_previous_time_df_new = rs_previous_time_data_frame.copy(
                            deep=True
                        )
                        # Get those names that contain the minute pattern
                        new_names_with_minutes = [
                            name for name in var_names_min if minute in name
                        ]
                        pdFunc.rename_columns_in_dataframe(
                            rs_previous_time_df_new,
                            ["C_q_Kfz_wert", "C_v_Kfz_wert"],
                            new_names_with_minutes,
                        )
                        # remove last rows from dataframe based on minutes
                        min_mod = int(minute.replace("_", ""))  # in int
                        if min_mod == 60:
                            min_str_fmt = "01:00:00"
                        else:
                            min_str_fmt = "0:{}:00".format(
                                min_mod
                            )  # in str with format "%H:%M:%S"
                        # Here, the last time in data frame will vary depending on the minute in the loop:
                        # For:
                        #   15 min -> 23:45:00
                        #   30 min -> 23:30:00
                        #   45 min -> 23:15:00
                        #   60 min -> 23:00:00
                        last_time_in_df = pdFunc.subtract_time_str(
                            "23:59:00", min_str_fmt
                        )
                        rs_previous_time_df_new = rs_previous_time_df_new.between_time(
                            "00:00:00", last_time_in_df
                        )
                        # Add the minutes to the timestamp so they match with the current time
                        pdFunc.add_minutes_to_timestamp_idx(
                            rs_previous_time_df_new, min_mod
                        )
                        # And, finally, adding only the values between 01:00:00 and 24:00:00
                        rs_previous_time_df_new = rs_previous_time_df_new.between_time(
                            "01:00:00", "23:59:00"
                        )
                        main_data_frame = pdFunc.merge_dataframes_on_fist_smaller(
                            main_data_frame, rs_previous_time_df_new,
                        )  # adding data from current time

                if global_data_frame.empty:
                    global_data_frame = main_data_frame
                else:
                    # Appending elements to the bottom of the data frame
                    global_data_frame = pd.concat(
                        [global_data_frame, main_data_frame],
                        ignore_index=False,
                        axis=0,
                    )

    # deleting "traffic_load", "fee" and "automatic_fee" from table
    global_data_frame = pdFunc.drop_selected_columns(
        ["traffic_load", "fee", "automatic_fee"], global_data_frame
    )
    # fill empty cells with 0
    global_data_frame = global_data_frame.fillna(0)
    # export dataframe to csv
    pdFunc.convert_to_csv("table_with_data_FINAL.csv", global_data_frame)


if __name__ == "__main__":
    main()
