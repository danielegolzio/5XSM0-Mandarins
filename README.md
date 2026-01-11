# Installation
Clone repository
```
git clone https://github.com/danielegolzio/5XSM0-Mandarins
cd 5XSM0-Mandarins
```
Install packages
```
pip install -r requirements.txt
```
# Usage
### 1. Clean MRI data
Run: `clean_data.py`
- Navigate through slices using the arrow keys
- Press 'd' to delete slices that are not required
- This step removes empty or irrelevant slices before processing

### 2. Compute edible volume
Run: `edible_volume.py` 
- Manually place seed points inside the pulp regions
- The pulp is segmented from the rest of the mandarin
- Outputs the edible volume of the mandarin

### 3. Compute total volume
Run: `total_volume.py`
- Segments the outer boundary of the mandarin
- Outputs the total external volume of the mandarin

# Notes
The helpers/ directory contains supporting functions used throughout the project:
- load.py: sorts DICOM data by series number and slice position
- clean.py: iterates through slices and allows deletion of unwanted images
- view.py: displays MRI slice series
- segment.py: segmentation functions implemented using scikit-learn and scikit-image
- volume.py: computes the total volume of a scan series
