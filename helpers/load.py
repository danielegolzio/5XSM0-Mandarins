import os
import pydicom as pd

def load(path: str) -> list[list]:
    """
    Load, filter, group, and sort DICOM slices from path.

    The function performs the following steps:
    1. Load all DICOM files in the specified folder.
    2. Removes slices belonging to a "Scout" series.
    3. Sorts slices by SeriesNumber and groups them into separate series.
    4. For each series, sorts the slices in anatomical order based on scan orientation,
       

    Parameters
    ----------
    path : str
        Path to the folder containing DICOM files.

    Returns
    -------
    list of list of pydicom.dataset.FileDataset
        A list of series, where each series is a list of DICOM slices sorted in anatomical order.
        Each inner list corresponds to a single series.
    """

    # Get all slices
    ds = [pd.dcmread(path + f) for f in os.listdir(path)]
    
    # Remove "Scout"
    ds = [f for f in ds if f.SeriesDescription != "Scout"]

    # Sort slices
    ds = sorted(
        ds, 
        key=lambda f: f.SeriesNumber
    )

    # Group by series
    curr_series = ds[0].SeriesNumber
    group = []
    grouped = []

    for f in ds:
        if f.SeriesNumber == curr_series:
            group.append(f)
            
        else:
            grouped.append(group)
            curr_series = f.SeriesNumber
            group = [f]
    grouped.append(group)

    # Sort each series
    ds = []
    for group in grouped:
        # Saggital
        if group[0].ImageOrientationPatient == [0, 1, 0, 0, 0, -1]:
            ds.append(
                sorted(
                    group,
                    key=lambda f: f.ImagePositionPatient[0]
                )
            ) 
        # Coronal    
        elif group[0].ImageOrientationPatient == [1, 0, 0, 0, 0, -1]:
            ds.append(
                sorted(
                    group,
                    key=lambda f: f.ImagePositionPatient[1]
                )
            )
        # Axial    
        elif group[0].ImageOrientationPatient == [1, 0, 0, 0, 1, 0]:
            ds.append(
                sorted(
                    group,
                    key=lambda f: f.ImagePositionPatient[2]
                )
            )
    return ds
