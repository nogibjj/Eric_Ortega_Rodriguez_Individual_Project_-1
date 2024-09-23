"""
        library file 
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def load_data(url):
    """
    Loads the Titanic dataset from a given URL and returns a pandas DataFrame.
    """
    return pd.read_csv(url)

def clean_data(df):
    """
    Cleans the Titanic dataset by handling missing values.
    """
    # Fill missing 'Age' with the median value
    df['Age'].fillna(df['Age'].median(), inplace=True)
    
    # Fill missing 'Embarked' with the most frequent value
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    
    # Drop 'Cabin' column due to too many missing values
    df.drop('Cabin', axis=1, inplace=True)
    
    return df

def analyze_data(df):
    """
    Analyzes the Titanic dataset and prints basic statistics and insights.
    """
    # Print basic information
    print("Dataset Info:")
    print(df.info())
    print("\nBasic Statistics:")
    print(df.describe())
    
    # Example analysis: survival rate by gender
    survival_by_gender = df.groupby('Sex')['Survived'].mean()
    print("\nSurvival Rate by Gender:")
    print(survival_by_gender)
    
    # Example analysis: survival rate by class
    survival_by_class = df.groupby('Pclass')['Survived'].mean()
    print("\nSurvival Rate by Passenger Class:")
    print(survival_by_class)

def main():
    url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv'
    
    # Load data
    df = load_data(url)
    
    # Clean data
    df = clean_data(df)
    
    # Analyze data
    analyze_data(df)

if __name__ == "__main__":
    main()
