from helpers.load import load
from helpers.volume import volume

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
    tot_volume = (volume(saggital_scans[i]) + volume(coronal_scans[i])) / 2
    print(f"Estimated volume of mandarin {i}: {tot_volume} mm^3")