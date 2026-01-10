import os
import shutil
from .view import view

def clean(ds: list[list]) -> None:
    """
    Interactively clean and save DICOM series.

    For each series in the input list, this function displays the slices
    using an interactive viewer, allowing the user to remove unwanted
    images. The remaining slices are then saved to a new directory named
    after the series number.

    Parameters
    ----------
    ds : list of list of pydicom.dataset.FileDataset
        List of DICOM series, where each series is a list of slices
        belonging to the same acquisition.

    Behavior
    --------
    - Each series is shown sequentially in an interactive viewer.
    - The user may mark slices for deletion during viewing.
    - A directory named ``series<SeriesNumber>/`` is created for each series.
    - If the directory already exists, it is deleted and recreated.
    - Cleaned slices are saved as ``slice_XXX.dcm`` files in order.

    Returns
    -------
    None
    """

    for data in ds:
        data = view(data)
        out_path = f"series{data[0].SeriesNumber}/"
        if os.path.exists(out_path):
            shutil.rmtree(out_path)
        os.makedirs(out_path, exist_ok=True)

        for i, dcm in enumerate(data):
            filename = f"slice_{i:03d}.dcm"
            filepath = os.path.join(out_path, filename)
            dcm.save_as(filepath)
