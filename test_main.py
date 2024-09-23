import unittest
import pandas as pd
from main import (
    load_data,
    calculate_correlation_matrix,
    survival_rates_by_group,
    calculate_descriptive_statistics
)

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
            has_sex = rates.index.isin(['male', 'female']).any()
            has_class = rates.index.isin([1, 2, 3]).any()
            self.assertTrue(has_sex or has_class)
            self.assertTrue((rates >= 0).all() and (rates <= 1).all())

    def test_descriptive_statistics(self):
        stats = calculate_descriptive_statistics(self.df)
        self.assertIsInstance(stats, pd.DataFrame)
        self.assertTrue({'Survived', 'Age', 'Pclass'}.issubset(stats.columns))
        self.assertEqual(stats.shape[0], 8)  # Default describe() returns 8 statistics


if __name__ == "__main__":
    unittest.main()
