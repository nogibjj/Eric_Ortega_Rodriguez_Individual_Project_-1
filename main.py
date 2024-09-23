import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(url):
    """Load the Titanic dataset from the provided URL."""
    return pd.read_csv(url)

def calculate_correlation_matrix(df):
    """Calculate and return the correlation matrix of the DataFrame."""
    numeric_df = df.select_dtypes(include='number')  # Select only numeric columns
    return numeric_df.corr()

def survival_rates_by_group(df, group_by):
    """Calculate survival rates grouped by a specific column."""
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

def main():
    # Load the dataset
    url = "https://github.com/datasciencedojo/datasets/raw/master/titanic.csv"
    df = load_data(url)

    # Calculate and plot the correlation matrix
    corr = calculate_correlation_matrix(df)
    plot_correlation_matrix(corr)

    # Calculate survival rates by sex
    survival_by_sex = survival_rates_by_group(df, 'Sex')
    plot_survival_rates(survival_by_sex, 'Survival Rates by Sex')

    # Calculate survival rates by age group
    age_bins = [0, 12, 18, 30, 50, 100]
    age_labels = ['Child', 'Teenager', 'Young Adult', 'Adult', 'Senior']
    df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)


    # Calculate survival rates by class
    survival_by_class = survival_rates_by_group(df, 'Pclass')
    plot_survival_rates(survival_by_class, 'Survival Rates by Class Level')

if __name__ == "__main__":
    main()
