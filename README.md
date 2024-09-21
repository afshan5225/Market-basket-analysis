# Market Basket Analysis

## Problem Statement
The project aims to perform market basket analysis using transaction data from a grocery store. The goal is to identify frequent item sets and generate association rules using the Apriori algorithm.

## Libraries Used
- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations.
- **matplotlib**: For data visualization.
- **seaborn**: For advanced data visualization.
- **apyori**: For implementing the Apriori algorithm.

## Execution Methodology
1. **Data Loading**: Load the dataset containing transactions and items.
2. **Data Exploration**: Basic exploration of the dataset including data size, shape, and missing values.
3. **Item Frequency Analysis**: Identify top and least selling items.
4. **Date Analysis**: Extract and analyze the year, month, and day of transactions.
5. **Apriori Algorithm**: Apply the Apriori algorithm to discover frequent item sets and association rules.

The final step includes generating and interpreting the results of the Apriori algorithm.










# ECLAT Algorithm for Market Basket Analysis

This project demonstrates the use of the **ECLAT (Equivalence Class Clustering and bottom-up Lattice Traversal)** algorithm to perform market basket analysis on a store's transaction data.

## Dataset

The dataset contains store transaction records, where each row represents a customer's purchase basket.

- Dataset source: [store_data.csv](https://raw.githubusercontent.com/gitganeshnethi/Datasets/refs/heads/master/store_data.csv)

## Libraries Used

- **Pandas**: Data manipulation
- **Seaborn**: Data visualization
- **pyECLAT**: ECLAT algorithm for frequent itemset mining

## Methodology

1. Load and preprocess the dataset.
2. Apply the ECLAT algorithm with a minimum support threshold.
3. Retrieve frequent itemsets and their support values.
