# -*- coding: utf-8 -*-
"""Market basket analysis.ipynb"""

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from apyori import apriori

# Loading dataset
df = pd.read_csv("/content/drive/MyDrive/dataset/Groceries_dataset.csv")

# Basic data overview
df.head()
df.info()
df.size
df.shape
df.ndim
df.isna().sum()

# Top selling item
df['itemDescription'].value_counts().nlargest(1)

# Least selling item
df['itemDescription'].value_counts().nsmallest(1)

# Top 10 selling items
df['itemDescription'].value_counts().head(10).plot(kind='bar')

# Top 10 least selling items
df['itemDescription'].value_counts().tail(10).plot(kind='bar')

# Least selling item sorted
df['itemDescription'].value_counts().tail(10).sort_values()

# Top 10 customers
df['Member_number'].value_counts().head(10)

# Extracting year, month, and day from date
df['year'] = df['Date'].str.extract(r'(\d{4})')
df['Month'] = df['Date'].str.extract(r'-(\d{2})-')
df['day'] = df['Date'].str.extract(r'(\d{2})')

# Majority transactions by year
df['year'].value_counts()

# Majority transactions by month
df['Month'].value_counts()

# Transactions in August 2015
df[df['year'] == '2015']['Month'].value_counts()
df[(df['year'] == '2015') & (df['Month'] == '08')]['day'].value_counts()

# Label encoding items
data = pd.get_dummies(df['itemDescription'])
data1 = df.join(data)

# Grouping data by Member_number and Date
products = df['itemDescription'].unique()
data2 = data1.groupby(['Member_number', 'Date'])[products].sum()

# Resetting index
data2 = data2.reset_index()

# Function to map 1 occurrences to product names
def fun(data):
    for i in products:
        if data[i] > 0:
            data[i] = i
    return data

# Apply function
data2 = data2.apply(fun, axis=1)

# Creating a new dataset with non-zero values
newdata1 = [i[i != 0].tolist() for i in data2.values if i[i != 0].tolist()]

# Apriori algorithm
association = apriori(newdata1, min_support=0.0003, min_confidence=0.05, min_lift=3, max_length=2)

# Display results
result = list(association)
result
