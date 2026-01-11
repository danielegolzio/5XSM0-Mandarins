from .segment import segment_otsu, segment_multiotsu
from skimage.morphology import reconstruction
import numpy as np
import matplotlib.pyplot as plt

def volume(scan: list) -> float:
    """
    Compute the total external volume of a mandarin from an MRI scan.

    This function estimates the *geometric (outer) volume* of the mandarin,
    including peel, pulp, membranes, and any internal air cavities. It does
    this by segmenting the mandarin from the background in each slice,
    filling all enclosed holes to recover the outer boundary, and summing
    voxel volumes across the 3D stack.

    Parameters
    ----------
    scan : list
        MRI scan data as loaded by the dataset loader. The first element
        (scan[0]) must be an iterable of DICOM slices with attributes
        `pixel_array`, `PixelSpacing`, and `SliceThickness`.

    Returns
    -------
    float
        Estimated total mandarin volume in cubic millimetres (mm^3).
    """

    total_volume = 0
    voxel_volume = scan[0][0].PixelSpacing[0] * scan[0][0].PixelSpacing[1] * scan[0][0].SliceThickness

    for image in scan[0]:
        pixels = image.pixel_array

        # create seed for erosion
        seed = np.copy(pixels)
        seed[1:-1, 1:-1] = pixels.max()

        # threshold with multiotsu (better than otsu)
        mask = segment_multiotsu(pixels, 3)
        # create binary mask
        thresholded = mask > 0
        # fill holes with erosion
        filled = reconstruction(seed, thresholded, method='erosion')

        plt.title("Filled Slice")
        plt.imshow(filled, cmap='gray')
        plt.show()

        # volume calculation
        total_volume += np.sum(filled) * voxel_volume

    return total_volume