

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(url):
    """Load the Titanic dataset from the specified URL."""
    return pd.read_csv(url)

def calculate_correlation_matrix(df):
    """Calculate and return the correlation matrix of the DataFrame."""
    numeric_df = df.select_dtypes(include='number')  # Select only numeric columns
    return numeric_df.corr()

def survival_rates_by_group(df, group_by):
    """Calculate survival rates grouped by a specified column."""
    return df.groupby(group_by)['Survived'].mean()

def plot_correlation_matrix(corr):
    """Plot the correlation matrix using a heatmap."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

def plot_survival_rates(survival_rates, title):
    """Plot survival rates using a bar plot."""
    plt.figure(figsize=(8, 5))
    survival_rates.plot(kind='bar', color='skyblue')
    plt.title(title)
    plt.xlabel('Group')
    plt.ylabel('Survival Rate')
    plt.xticks(rotation=0)
    plt.ylim(0, 1)
    plt.show()

def calculate_descriptive_statistics(df):
    """Calculate and return descriptive statistics for specific columns."""
    return df[['Survived', 'Age', 'Pclass']].describe()
