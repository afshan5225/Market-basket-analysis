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
