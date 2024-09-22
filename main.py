"""
        library file 
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset = (
    "https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv"
)


def load_dataset():
    df = pd.read_csv(dataset)
    return df

def grab_mean(df, col):
    return df[col].mean()

def grab_median(df,col):
    return df[col].median() 

# def grab STD
def grab_std(df,col):
    return df[col].std()

# def grab max
def grab_max(df,col):
    return df[col].max()

def create_histogram(df , col):
    df[col].plot.hist(bins=10, edgecolor ='black')
    plt.title(col)

df1 = load_dataset()
df1.head()

mean_alc = grab_mean(df1,"alcohol_use")

median_alc = grab_median(df1,"alcohol_use")

std_alc = grab_std(df1,"alcohol_use")

max_alc = grab_max(df1,"alcohol_use")

create_histogram(df1, "alcohol_use")
