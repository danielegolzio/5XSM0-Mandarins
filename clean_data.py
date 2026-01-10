from helpers.view import view
from helpers.load import load
from helpers.clean import clean

# path of stored data
path = "data/"

# sort data
ds = load(path)

# remove unwanted slices with viewer
clean(ds)