from helpers.load import load
from helpers.view import view
from helpers.segment import segment_flood, segment_kmeans, segment_gmm, segment_otsu, segment_multiotsu

import numpy as np

# fist scan is saggital plane second scan is coronal plane

# mandarin 1 data
scan00 = load("series2/")
scan01 = load("series3/")

# mandarin 2 data
scan10 = load("series5/")
scan11 = load("series6/")

# mandarin 3 data
scan20 = load("series8/")
scan21 = load("series9/")

# mandarin 4 data
scan30 = load("series11/")
scan31 = load("series12/")

saggital_scans = [scan00, scan10, scan20, scan30]
coronal_scans = [scan01, scan11, scan21, scan31]

for i in range(4):
    volume = 0
    voxel_volume = saggital_scans[i][0][0].PixelSpacing[0] * saggital_scans[i][0][0].PixelSpacing[1] * saggital_scans[i][0][0].SliceThickness
    print("Voxel volume (mm^3):", voxel_volume) 
    for image in saggital_scans[i][0]:
        pixels = image.pixel_array
        mask = segment_flood(pixels, tolerance=0.09)
        volume += np.sum(mask) * voxel_volume

    print(f"Estimated volume of mandarin {i}: {volume} mm^3")