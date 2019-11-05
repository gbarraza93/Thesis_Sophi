import os


### Keys and values useful for providing translations and paths to files

CHARACTERISTICS_DIR = "FastLaneCharacteristics"
STRUCTURE_DIR = "RohStruct"
TYP_ARCHIVE_DIR = "Typ_AQZustandArchiv"

FASTLANE_FILE_PREFIX = (
    "FastLaneTLV.FastLane.FastLaneCharacteristics.FastLaneCharacteristics."
)

HEADER = "Header"

MAIN_DIRECTORY = "/home/memo/Desktop/Sample_Data/Sample_Data/"
XML_FILES_ENDING = ".01.xml"


TYP_ARCHIVE_FILE_VPS_0062_0001_W = (
    "FastLaneTLV.VPS_0062_0001_W.AQZustandArchiv.Typ_AQZustandArchiv."
)
TYP_ARCHIVE_FILE_VPS_0435_FL01_W = (
    "FastLaneTLV.VPS_0435_FL01_W.AQZustandArchiv.Typ_AQZustandArchiv."
)
TYP_ARCHIVE_FILE_VMS_0070_0001_W = (
    "FastLaneTLV.VMS_0070_0001_W.AQZustandArchiv.Typ_AQZustandArchiv."
)
TYP_ARCHIVE_FILE_VMS_0603_PRAR_W = (
    "FastLaneTLV.VMS_0603_PRAR_W.AQZustandArchiv.Typ_AQZustandArchiv."
)

GREEN_FILES_PREFIX = [
    TYP_ARCHIVE_FILE_VPS_0062_0001_W,
    TYP_ARCHIVE_FILE_VPS_0435_FL01_W,
    TYP_ARCHIVE_FILE_VMS_0070_0001_W,
    TYP_ARCHIVE_FILE_VMS_0603_PRAR_W,
]

GREEN_FILES_PREFIX_BATCH_1 = [
    TYP_ARCHIVE_FILE_VPS_0062_0001_W,
    TYP_ARCHIVE_FILE_VPS_0435_FL01_W,
]


GREEN_FILES_PREFIX_BATCH_2 = [
    TYP_ARCHIVE_FILE_VMS_0070_0001_W,
    TYP_ARCHIVE_FILE_VMS_0603_PRAR_W,
]
