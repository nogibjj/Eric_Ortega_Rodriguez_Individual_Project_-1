import unittest
import pandas as pd
from main import load_data, calculate_correlation_matrix, survival_rates_by_group

class TestLibFunctions(unittest.TestCase):

    def test_load_data(self):
        url = "https://github.com/datasciencedojo/datasets/raw/master/titanic.csv"
        df = load_data(url)
        self.assertIsNotNone(df)
        self.assertIn('Survived', df.columns)

    def test_calculate_correlation_matrix(self):
        df = load_data("https://github.com/datasciencedojo/datasets/raw/master/titanic.csv")
        corr = calculate_correlation_matrix(df)
        self.assertIsInstance(corr, pd.DataFrame)
        self.assertEqual(corr.shape[0], corr.shape[1])

    def test_survival_rates_by_group(self):
        df = load_data("https://github.com/datasciencedojo/datasets/raw/master/titanic.csv")
        survival_rates = survival_rates_by_group(df, 'Sex')
        self.assertIn('male', survival_rates.index)
        self.assertIn('female', survival_rates.index)
        self.assertTrue((survival_rates >= 0).all() and (survival_rates <= 1).all())

if __name__ == "__main__":
    unittest.main()
