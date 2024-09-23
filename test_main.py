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
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertIn('Survived', self.df.columns)
        self.assertIn('Sex', self.df.columns)
        self.assertIn('Age', self.df.columns)
        self.assertIn('Pclass', self.df.columns)

    def test_calculate_correlation_matrix(self):
        """Test if the correlation matrix is calculated correctly."""
        corr = calculate_correlation_matrix(self.df)
        self.assertIsInstance(corr, pd.DataFrame)
        self.assertEqual(corr.shape[0], corr.shape[1])  # Should be square
        self.assertIn('Survived', corr.columns)

    def test_survival_rates_by_sex(self):
        """Test survival rates by sex."""
        survival_by_sex = survival_rates_by_group(self.df, 'Sex')
        self.assertIn('male', survival_by_sex.index)
        self.assertIn('female', survival_by_sex.index)
        self.assertTrue((survival_by_sex >= 0).all())  # Rates should be >= 0
        self.assertTrue((survival_by_sex <= 1).all())  # Rates should be <= 1

    def test_survival_rates_by_class(self):
        """Test survival rates by class."""
        survival_by_class = survival_rates_by_group(self.df, 'Pclass')
        self.assertIn(1, survival_by_class.index)
        self.assertIn(2, survival_by_class.index)
        self.assertIn(3, survival_by_class.index)
        self.assertTrue((survival_by_class >= 0).all())  # Rates should be >= 0
        self.assertTrue((survival_by_class <= 1).all())  # Rates should be <= 1

if __name__ == "__main__":
    unittest.main()
