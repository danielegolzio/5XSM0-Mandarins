# Installation
install repo
```
git clone https://github.com/danielegolzio/5XSM0-Mandarins
cd 5XSM0-Mandarins
```
install packages
```
pip install -r requirements.txt
```
# Usage
### 1. clean data
run `clean_data.py`
-> go through sluices wiuth arrow keys and delete slices that you dont need with 'd' key

### 2. get edible volume
run `edible_volume.py` 
-> manually place seeds in pulp regions to segment them from mandarin
-> outputs edible volume of mandarin

### 3. get total volume
run `total_volume.py`
-> outputs total volume of the mandarin
