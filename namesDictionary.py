### Keys and values useful for providing translations and paths to files

CHARACTERISTICS_DIR = "FastLaneCharacteristics"
STRUCTURE_DIR = "RohStruct"
TYP_ARCHIVE_DIR = "Typ_AQZustandArchiv"

FASTLANE_FILE_PREFIX = (
    "FastLaneTLV.FastLane.FastLaneCharacteristics.FastLaneCharacteristics."
)

HEADER = "Header"

MAIN_DIRECTORY = "/home/memo/Desktop//Data/"
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

GREEN_FILES_PREFIX = {
    TYP_ARCHIVE_FILE_VPS_0062_0001_W: "min_occ_1",
    TYP_ARCHIVE_FILE_VPS_0435_FL01_W: "min_occ_2",
    TYP_ARCHIVE_FILE_VMS_0070_0001_W: "cong_mess_1",
    TYP_ARCHIVE_FILE_VMS_0603_PRAR_W: "cong_mess_2",
}

GREEN_FILES_PREFIX_BATCH_1 = [
    TYP_ARCHIVE_FILE_VPS_0062_0001_W,
    TYP_ARCHIVE_FILE_VPS_0435_FL01_W,
]


GREEN_FILES_PREFIX_BATCH_2 = [
    TYP_ARCHIVE_FILE_VMS_0070_0001_W,
    TYP_ARCHIVE_FILE_VMS_0603_PRAR_W,
]


RHOSTRUCT_FILE_LD_0142_FL01_W = "FastLaneTLV.LD_0142_FL01_W.RohGeglaettet.RohStruct."
RHOSTRUCT_FILE_LD_0142_0001_W = "FastLaneTLV.LD_0142_0001_W.RohGeglaettet.RohStruct."
RHOSTRUCT_FILE_LD_0621_FLR1_W = "FastLaneTLV.LD_0621_FLR1_W.RohGeglaettet.RohStruct."
RHOSTRUCT_FILE_LD_0523_001R_W = "FastLaneTLV.LD_0523_001R_W.RohGeglaettet.RohStruct."


RS_FILES_CURRENT_TIME = {
    RHOSTRUCT_FILE_LD_0142_FL01_W: [
        "q_trucks_fl_d1",
        "q_veh_fl_d1",
        "q_fl_d1",
        "v_fl_d1",
    ],
    RHOSTRUCT_FILE_LD_0142_0001_W: [
        "q_trucks_hw_d1",
        "q_veh_hw_d1",
        "q_hw_d1",
        "v_hw_d1",
    ],
    RHOSTRUCT_FILE_LD_0621_FLR1_W: [
        "q_trucks_fl_d2",
        "q_veh_fl_d2",
        "q_fl_d2",
        "v_fl_d2",
    ],
    RHOSTRUCT_FILE_LD_0523_001R_W: [
        "q_trucks_hw_d2",
        "q_veh_hw_d2",
        "q_hw_d2",
        "v_hw_d2",
    ],
}

RHO_STRUCT_PREVIOUS_TIME_H_1400 = "FastLaneTLV.LD_0070_0001_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_H_2000 = (
    "FastLaneTLV.LD_0100_0001_W.RohGeglaettetStau.RohStruct."
)
RHO_STRUCT_PREVIOUS_TIME_2000 = "FastLaneTLV.LD_0100_FL01_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_H_2600 = "FastLaneTLV.LD_0130_0001_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_2600 = "FastLaneTLV.LD_0130_FL01_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_H_3860 = "FastLaneTLV.LD_0193_0001_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_3860 = "FastLaneTLV.LD_0193_FL01_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_H_6700 = "FastLaneTLV.LD_0439_0001_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_6700 = "FastLaneTLV.LD_0439_FL01_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_7000 = "FastLaneTLV.LD_0454_FL01_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_PR_7300 = "FastLaneTLV.LD_0705_FL1R_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_7300 = "FastLaneTLV.LD_0469_FL01_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_7680 = "FastLaneTLV.LD_0488_FL01_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_H_7920 = "FastLaneTLV.LD_0500_0001_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_7920 = "FastLaneTLV.LD_0500_FL01_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_H_9760 = "FastLaneTLV.LD_0592_0001_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_9760 = "FastLaneTLV.LD_0592_FL01_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_H_10820 = "FastLaneTLV.LD_0645_0001_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_10820 = "FastLaneTLV.LD_0645_FL01_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_H_12820 = "FastLaneTLV.LD_1216_0001_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_12820 = "FastLaneTLV.LD_1216_FL01_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_H_14060 = "FastLaneTLV.LD_1278_0020_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_14060 = "FastLaneTLV.LD_1278_FL20_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_H_14200 = "FastLaneTLV.LD_1285_0020_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_14200 = "FastLaneTLV.LD_1285_FL20_W.RohGeglaettet.RohStruct."
RHO_STRUCT_PREVIOUS_TIME_H_14500 = "FastLaneTLV.LD_A300_0020_W.RohGeglaettet.RohStruct."


RHO_STRUCT_PREVIOUS_TIME = {
    RHO_STRUCT_PREVIOUS_TIME_H_1400: [
        "q_hw_1400_15",
        "v_hw_1400_15",
        "q_hw_1400_30",
        "v_hw_1400_30",
        "q_hw_1400_45",
        "v_hw_1400_45",
        "q_hw_1400_60",
        "v_hw_1400_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_H_2000: [
        "q_hw_2000_15",
        "v_hw_2000_15",
        "q_hw_2000_30",
        "v_hw_2000_30",
        "q_hw_2000_45",
        "v_hw_2000_45",
        "q_hw_2000_60",
        "v_hw_2000_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_2000: [
        "q_fl_2000_15",
        "v_fl_2000_15",
        "q_fl_2000_30",
        "v_fl_2000_30",
        "q_fl_2000_45",
        "v_fl_2000_45",
        "q_fl_2000_60",
        "v_fl_2000_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_H_2600: [
        "q_hw_2600_15",
        "v_hw_2600_15",
        "q_hw_2600_30",
        "v_hw_2600_30",
        "q_hw_2600_45",
        "v_hw_2600_45",
        "q_hw_2600_60",
        "v_hw_2600_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_2600: [
        "q_fl_2600_15",
        "v_fl_2600_15",
        "q_fl_2600_30",
        "v_fl_2600_30",
        "q_fl_2600_45",
        "v_fl_2600_45",
        "q_fl_2600_60",
        "v_fl_2600_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_H_3860: [
        "q_hw_3860_15",
        "v_hw_3860_15",
        "q_hw_3860_30",
        "v_hw_3860_30",
        "q_hw_3860_45",
        "v_hw_3860_45",
        "q_hw_3860_60",
        "v_hw_3860_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_3860: [
        "q_fl_3860_15",
        "v_fl_3860_15",
        "q_fl_3860_30",
        "v_fl_3860_30",
        "q_fl_3860_45",
        "v_fl_3860_45",
        "q_fl_3860_60",
        "v_fl_3860_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_H_6700: [
        "q_hw_6700_15",
        "v_hw_6700_15",
        "q_hw_6700_30",
        "v_hw_6700_30",
        "q_hw_6700_45",
        "v_hw_6700_45",
        "q_hw_6700_60",
        "v_hw_6700_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_6700: [
        "q_fl_6700_15",
        "v_fl_6700_15",
        "q_fl_6700_30",
        "v_fl_6700_30",
        "q_fl_6700_45",
        "v_fl_6700_45",
        "q_fl_6700_60",
        "v_fl_6700_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_7000: [
        "q_fl_7000_15",
        "v_fl_7000_15",
        "q_fl_7000_30",
        "v_fl_7000_30",
        "q_fl_7000_45",
        "v_fl_7000_45",
        "q_fl_7000_60",
        "v_fl_7000_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_PR_7300: [
        "q_fl_7300_pr_15",
        "v_fl_7300_pr_15",
        "q_fl_7300_pr_30",
        "v_fl_7300_pr_30",
        "q_fl_7300_pr_45",
        "v_fl_7300_pr_45",
        "q_fl_7300_pr_60",
        "v_fl_7300_pr_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_7300: [
        "q_fl_7300_15",
        "v_fl_7300_15",
        "q_fl_7300_30",
        "v_fl_7300_30",
        "q_fl_7300_45",
        "v_fl_7300_45",
        "q_fl_7300_60",
        "v_fl_7300_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_7680: [
        "q_fl_7680_15",
        "v_fl_7680_15",
        "q_fl_7680_30",
        "v_fl_7680_30",
        "q_fl_7680_45",
        "v_fl_7680_45",
        "q_fl_7680_60",
        "v_fl_7680_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_H_7920: [
        "q_hw_7920_15",
        "v_hw_7920_15",
        "q_hw_7920_30",
        "v_hw_7920_30",
        "q_hw_7920_45",
        "v_hw_7920_45",
        "q_hw_7920_60",
        "v_hw_7920_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_7920: [
        "q_fl_7920_15",
        "v_fl_7920_15",
        "q_fl_7920_30",
        "v_fl_7920_30",
        "q_fl_7920_45",
        "v_fl_7920_45",
        "q_fl_7920_60",
        "v_fl_7920_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_H_9760: [
        "q_hw_9760_15",
        "v_hw_9760_15",
        "q_hw_9760_30",
        "v_hw_9760_30",
        "q_hw_9760_45",
        "v_hw_9760_45",
        "q_hw_9760_60",
        "v_hw_9760_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_9760: [
        "q_fl_9760_15",
        "v_fl_9760_15",
        "q_fl_9760_30",
        "v_fl_9760_30",
        "q_fl_9760_45",
        "v_fl_9760_45",
        "q_fl_9760_60",
        "v_fl_9760_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_H_10820: [
        "q_hw_10820_15",
        "v_hw_10820_15",
        "q_hw_10820_30",
        "v_hw_10820_30",
        "q_hw_10820_45",
        "v_hw_10820_45",
        "q_hw_10820_60",
        "v_hw_10820_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_10820: [
        "q_fl_10820_15",
        "v_fl_10820_15",
        "q_fl_10820_30",
        "v_fl_10820_30",
        "q_fl_10820_45",
        "v_fl_10820_45",
        "q_fl_10820_60",
        "v_fl_10820_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_H_12820: [
        "q_hw_12820_15",
        "v_hw_12820_15",
        "q_hw_12820_30",
        "v_hw_12820_30",
        "q_hw_12820_45",
        "v_hw_12820_45",
        "q_hw_12820_60",
        "v_hw_12820_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_12820: [
        "q_fl_12820_15",
        "v_fl_12820_15",
        "q_fl_12820_30",
        "v_fl_12820_30",
        "q_fl_12820_45",
        "v_fl_12820_45",
        "q_fl_12820_60",
        "v_fl_12820_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_H_14060: [
        "q_hw_14060_15",
        "v_hw_14060_15",
        "q_hw_14060_30",
        "v_hw_14060_30",
        "q_hw_14060_45",
        "v_hw_14060_45",
        "q_hw_14060_60",
        "v_hw_14060_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_14060: [
        "q_fl_14060_15",
        "v_fl_14060_15",
        "q_fl_14060_30",
        "v_fl_14060_30",
        "q_fl_14060_45",
        "v_fl_14060_45",
        "q_fl_14060_60",
        "v_fl_14060_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_H_14200: [
        "q_hw_14200_15",
        "v_hw_14200_15",
        "q_hw_14200_30",
        "v_hw_14200_30",
        "q_hw_14200_45",
        "v_hw_14200_45",
        "q_hw_14200_60",
        "v_hw_14200_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_14200: [
        "q_fl_14200_15",
        "v_fl_14200_15",
        "q_fl_14200_30",
        "v_fl_14200_30",
        "q_fl_14200_45",
        "v_fl_14200_45",
        "q_fl_14200_60",
        "v_fl_14200_60",
    ],
    RHO_STRUCT_PREVIOUS_TIME_H_14500: [
        "q_hw_14500_15",
        "v_hw_14500_15",
        "q_hw_14500_30",
        "v_hw_14500_30",
        "q_hw_14500_45",
        "v_hw_14500_45",
        "q_hw_14500_60",
        "v_hw_14500_60",
    ],
}
