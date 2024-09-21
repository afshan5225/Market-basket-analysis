# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Importing dataset
df = pd.read_csv("https://raw.githubusercontent.com/gitganeshnethi/Datasets/refs/heads/master/store_data.csv", header=None)

# ECLAT Algorithm
from pyECLAT import ECLAT

# Initialize ECLAT with data
ecl = ECLAT(data=df, verbose=True)

# Fitting the ECLAT model with a minimum support threshold
get_ECLAT_indexes, get_ECLAT_supports = ecl.fit(min_support=0.08, separator=' & ', verbose=True)

# Display ECLAT support values
get_ECLAT_supports
