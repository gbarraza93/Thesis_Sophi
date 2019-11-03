import csv
import re
from XML_parsing_functions import get_xml_CDATA_from_element_tail
import namesDictionary as ND
from typing import List, Any


def remove_characters(string_to_clean: str, list_of_characters: List[str]) -> str:
    are_white_spaces = False
    if ' ' in list_of_characters:
        are_white_spaces = True

    if are_white_spaces:
        formated_data = string_to_clean.replace(' ', '_')  # we will replace white spaces with an underscore
        return re.sub("|".join(list_of_characters), "", formated_data)
    else:
        # when no white spaces found, then only rid out of the passed characters
        return re.sub("|".join(list_of_characters), "", string_to_clean)


def remove_empty_rows(csv_reader) -> List[List[str]]:
    lines = list()
    for row in csv_reader:
        if row:  # if row is not empty, get the row
            lines.append(list(filter(None, row)))  # remove any empty element in the list
    return lines


