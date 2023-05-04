import numpy as np
import pandas as pd

def parse_dynalog(file_path):
    df = pd.read_csv(file_path, header=None, delimiter='\t', skiprows=15, usecols=[0, 1, 3, 4])

    # Calculate actual fluence and planned fluence
    actual_fluence = np.sqrt(df[1]**2 + df[2]**2)
    planned_fluence = np.sqrt(df[3]**2 + df[4]**2)

    # Calculate error
    error = (actual_fluence - planned_fluence) / planned_fluence

    return actual_fluence, planned_flu