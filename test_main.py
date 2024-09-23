import unittest
import pandas as pd
from main import load_data, calculate_correlation_matrix, survival_rates_by_group

class TestTitanicDataAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = load_data("https://github.com/datasciencedojo/datasets/raw/master/titanic.csv")

    def test_load_data(self):
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertTrue({'Survived', 'Sex', 'Age', 'Pclass'}.issubset(self.df.columns))

    def test_calculate_correlation_matrix(self):
        corr = calculate_correlation_matrix(self.df)
        self.assertIsInstance(corr, pd.DataFrame)
        self.assertEqual(corr.shape[0], corr.shape[1])
        self.assertIn('Survived', corr.columns)

    def test_survival_rates(self):
        for group_by in ['Sex', 'Pclass']:
            rates = survival_rates_by_group(self.df, group_by)
            self.assertTrue(rates.index.isin(['male', 'female']).any() or rates.index.isin([1, 2, 3]).any())
            self.assertTrue((rates >= 0).all() and (rates <= 1).all())

if __name__ == "__main__":
    unittest.main()
