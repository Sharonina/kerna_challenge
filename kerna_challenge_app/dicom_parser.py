import pydicom
import numpy as np
import pandas as pd

def parse_dicom(file_path):
    ds = pydicom.dcmread(file_path)

    # Extract structure names
    structures = [s.StructureSetROISequence[0].ROIName for s in ds.RTROIObservationsSequence]

    # Extract dose data
    dose_data = ds.pixel_array.astype(float)
    dose_max = np.max(dose_data)

    return structures, dose_max