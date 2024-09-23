import unittest
import pandas as pd
from lib import (
    load_data,
    calculate_correlation_matrix,
    survival_rates_by_group,
    calculate_descriptive_statistics,
)

class TestLibFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = "https://github.com/datasciencedojo/datasets/raw/master/titanic.csv"
        cls.df = load_data(cls.url)

    def test_load_data(self):
        """Test if the data loads correctly and is a DataFrame."""
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertTrue({'Survived', 'Sex', 'Age', 'Pclass'}.issubset(self.df.columns))

    def test_calculate_correlation_matrix(self):
        """Test if the correlation matrix is calculated correctly."""
        corr = calculate_correlation_matrix(self.df)
        self.assertIsInstance(corr, pd.DataFrame)
        self.assertEqual(corr.shape[0], corr.shape[1])  # Should be square
        self.assertIn('Survived', corr.columns)

    def test_survival_rates_by_group(self):
        """Test survival rates by different groups."""
        for group_by in ['Sex', 'Pclass']:
            rates = survival_rates_by_group(self.df, group_by)
            self.assertTrue((rates >= 0).all() and (rates <= 1).all())

    def test_calculate_descriptive_statistics(self):
        """Test if descriptive statistics are calculated correctly."""
        stats = calculate_descriptive_statistics(self.df)
        self.assertIsInstance(stats, pd.DataFrame)
        self.assertTrue({'Survived', 'Age', 'Pclass'}.issubset(stats.columns))
        self.assertEqual(stats.shape[0], 8)  # Default describe() returns 8 statistics

if __name__ == "__main__":
    unittest.main()
