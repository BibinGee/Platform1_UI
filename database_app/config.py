database_headers = [
    "Market high byte", "Market low byte", "Serial Enable high byte", "Serial Enable low byte",
    "Force Mode Toggle","Calibration Status high byte", "Calibration Status low byte",
    "Manufacturing Product Traceability Data 1",
    "Manufacturing Product Traceability Data 2", "Manufacturing Product Traceability Data 3",
    "Manufacturing Product Traceability Data 4",
    "Manufacturing Product Traceability Data 5", "Manufacturing Product Traceability Data 6",
    "Manufacturing Product Traceability Data 7",
    "Manufacturing Product Traceability Data 8", "Manufacturing Product Traceability Data 9",
    "Manufacturing Product Traceability Data 10",
    "Manufacturing Product Traceability Data 11", "Manufacturing Product Traceability Data 12",
    "Manufacturing Product Traceability Data 13", "Manufacturing Product Traceability Data 14",
    "Manufacturing Product Traceability Data 15", "Manufacturing Product Traceability Data 16",
    "Manufacturing Product Traceability Data 17", "Manufacturing Product Traceability Data 18",
    "Manufacturing Product Traceability Data 19", "Manufacturing Product Traceability Data 20",
    "Manufacturing Product Traceability Data 21", "IR Forward Drive Current",
    "IR Back Drive Current", "Blue Forward Drive Current", "Photo Reading Initialization Time",
    "IR Forward PTT Drive Current", "IR Back PTT Drive Current", "Blue Forward PTT Drive Current",
    "Photo Alarm Equation Threshold",
    "Photo Alarm Hush Threshold", "Alarm Equation Fail Safe Level", "IR Forward Factory Value",
    "IR Back Factory Value", "Blue Forward Factory Value", "Photo Cal IR Forward Min Value",
    "Photo Cal IR Forward Max Value", "Photo Cal IR Back Min Value", "Photo Cal IR Back Max Value",
    "Photo Cal Blue Forward Min Value", "Photo Cal Blue Forward Max Value",
    "IR Forward Quiescent Value", "IR Back Quiescent Value", "Blue Forward Quiescent Value",
    "Photo Cal Blue Back Supervision", "CO Circuit Calibration Raw Counts",
    "CO Offset high byte", "CO Offset low byte", "CO PPM Scale high byte", "CO PPM Scale low byte",
    "Low Battery Voltage Threshold", "AFE TIA Manual Calibration Status",
    "Hush Multiplier high byte", "Hush Multiplier low byte",
    "Reserved Database Addresses (Unused)1",
    "Reserved Database Addresses (Unused)2",
    "Reserved Database Addresses (Unused)3",
    "Reserved Database Addresses (Unused)4",
    "Reserved Database Addresses (Unused)5",
    "Reserved Database Addresses (Unused)6",
    "Reserved Database Addresses (Unused)7",
    "Reserved Database Addresses (Unused)8",
    "Reserved Database Addresses (Unused)9",
    "Reserved Database Addresses (Unused)10", "Flaming Fire IR_F to IR_B Ratio high byte",
    "Flaming Fire IR_F to IR_B Ratio low byte",
    "Flaming Fire BL_F to IR_B Ratio high byte", "Flaming Fire BL_F to IR_B Ratio low byte",
    "Multiwave/Photo IR_F to IR_B Ratio high byte", "Multiwave/Photo IR_F to IR_B Ratio low byte",
    "Multiwave/Photo BL_F to IR_B Ratio high byte",
    "Multiwave/Photo BL_F to IR_B Ratio low byte", "Multi-Wave Flaming Fire Ratio",
    "Photo IR Forward Delta", "Photo IR Back Delta",
    "Photo Blue Forward Delta", "Light IR Forward Validation Threshold",
    "Light IR Back Validation Threshold", "Dark IR Forward Validation Threshold",
    "Dark IR Back Validation Threshold", "Alarm Equation Fail Safe Count Threshold",
    "Reserved Database Address (Unused)", "Normal Mode Period",
    "Reserved Database Addresses (Unused) 1",
    "Reserved Database Addresses (Unused) 2",
    "Reserved Database Addresses (Unused) 3",
    "Reserved Database Addresses (Unused) 4",
    "Reserved Database Addresses (Unused) 5",
    "Reserved Database Addresses (Unused) 6",
    "Reserved Database Addresses (Unused) 7",
    "Reserved Database Addresses (Unused) 8",
    "Reserved Database Addresses (Unused) 9",
    "Reserved Database Addresses (Unused) 10",
    "Reserved Database Addresses (Unused) 11",
    "Reserved Database Addresses (Unused) 12",
    "Reserved Database Addresses (Unused) 13",
    "Reserved Database Addresses (Unused) 14",
    "Reserved Database Addresses (Unused) 15",
    "Reserved Database Addresses (Unused) 16",
    "Reserved Database Addresses (Unused) 17",
    "Reserved Database Addresses (Unused) 18",
    "Reserved Database Addresses (Unused) 19",
    "Reserved Database Addresses (Unused) 20",
    "Day Count high byte", "Day Count low byte",
    "CO Sensor Health Error Count high byte", "CO Sensor Health Error Count low byte",
    "CO Sensor Short Count high byte", "CO Sensor Short Count low byte",
    "Smoke Chamber Error Count high byte", "Smoke Chamber Error Count low byte",
    "Push to Test Count high byte", "Push to Test Count low byte",
    "Flash Memory Error Count high byte", "Flash Memory Error Count low byte",
    "Database Erase Count high byte", "Database Erase Count low byte",
    "Database Page Number", "CRC high byte", "CRC low byte",
]

major_event_headers = {
    "81": "Major Events 1st Entry",
    "82": "CO Sensor Health Fault",
    "83": "CO Sensor Short Fault",
    "84": "Drift Compensation Fault",
    "85": "Hardwired Interconnect Supervision Fault",
    "86": "Push To Test Fault",
    "87": "Fatal Memory Fault",
    "88": "End of Life",
    "8A": "CO Fault Cleared",
    "8B": "RAM Database Memory Fault",
    "8C": "Flash Primary Database Memory Fault",
    "8D": "Flash Back Up Database Memory Fault",
    "8E": "CO Sensor Test Fault (PTT)",
    "8F": "Button Stuck Fault",
    "90": "32KHz Crystal Startup Error",
    "91": "Smoke Alarm Start",
    "92": "Smoke Alarm Interconnect Start",
    "93": "CO Alarm",
    "94": "CO Alarm Interconnect",
    "95": "Smoke Alarm End",
    "96": "Smoke Alarm Interconnect End",
    "97": "Fatal AFE Fault",
    "A0": "Photo Clean Air Value Fault Set",
    "A1": "Photo Forward Ambient Fault Set",
    "A2": "Photo Back Ambient Fault Set",
    "A3": "Photo Forward IR LED Fault Set",
    "A4": "Photo Back IR LED Fault Set",
    "A5": "Photo Blue LED Supervision Fault Set",
    "A6": "Photo Clean Air Value Fault Cleared",
    "A7": "Photo Forward Ambient Fault Cleared",
    "A8": "Photo Back Ambient Fault Cleared",
    "A9": "Photo Forward IR LED Fault Cleared",
    "AA": "Photo Back IR LED Fault Cleared",
    "AB": "Photo Blue LED Supervision Fault Cleared",
    "AC": "All Photo Faults Cleared",
}

minor_event_headers = {
    "01": "Minor Events 1st Entry",
    "02": "AC Power Off",
    "03": "AC Power On",
    "04": "Push To Test Activated",
    "05": "Low Battery",
    "06": "Low Battery Fatal",
    "07": "No Battery / Abnormally Low Battery",
    "10": "Power On",
    "11": "Power Reset Execution of Illegal Instruction",
    "12": "Power Reset Watchdog Timer",
    "13": "Power Reset RAM Parity Error",
    "14": "Power Reset Illegal Memory Access",
    "15": "Power Reset Low Voltage Detection",
    "16": "Power Reset Debugger Interface",
    "17": "Power Reset Software Reset",
    "18": "Power Reset External Reset",
    "19": "Power Reset Brown Out Detection",
}
