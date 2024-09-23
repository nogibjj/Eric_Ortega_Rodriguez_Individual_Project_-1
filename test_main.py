import unittest
import pandas as pd
from main import load_data, calculate_correlation_matrix, survival_rates_by_group

class TestTitanicDataAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up test data for all tests."""
        cls.url = "https://github.com/datasciencedojo/datasets/raw/master/titanic.csv"
        cls.df = load_data(cls.url)

    def test_load_data(self):
        """Test if the data loads correctly and has the expected columns."""
        expected_columns = ['Survived', 'Sex', 'Age', 'Pclass']
        self.assertIsInstance(self.df, pd.DataFrame)
        for column in expected_columns:
            self.assertIn(column, self.df.columns)

    def test_calculate_correlation_matrix(self):
        """Test if the correlation matrix is calculated correctly."""
        corr = calculate_correlation_matrix(self.df)
        self.assertIsInstance(corr, pd.DataFrame)
        self.assertEqual(corr.shape[0], corr.shape[1])  # Should be square
        self.assertIn('Survived', corr.columns)

    def test_survival_rates(self):
        """Test survival rates by sex and class."""
        for group_by in ['Sex', 'Pclass']:
            survival_rates = survival_rates_by_group(self.df, group_by)
            self.assertTrue(survival_rates.index.isin(['male', 'female']).any() or
                            survival_rates.index.isin([1, 2, 3]).any())
            self.assertTrue((survival_rates >= 0).all() and (survival_rates <= 1).all())

if __name__ == "__main__":
    unittest.main()
