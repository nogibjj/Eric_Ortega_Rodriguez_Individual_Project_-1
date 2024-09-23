import unittest
import pandas as pd
from main import load_data, clean_data, analyze_data

class TestTitanicFunctions(unittest.TestCase):

    def load_test_data(self):
        """Load the test data from the CSV file."""
        return pd.read_csv('titanic_data.csv')

    def test_load_data(self):
        """Test load_data function."""
        df = load_data("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('Survived', df.columns)

    def test_clean_data(self):
        """Test clean_data function."""
        test_df = self.load_test_data()
        df_cleaned = clean_data(test_df)
        self.assertNotIn('Cabin', df_cleaned.columns)
        self.assertFalse(df_cleaned['Age'].isnull().any())
        self.assertFalse(df_cleaned['Embarked'].isnull().any())

    def test_analyze_data(self):
        """Test analyze_data doesn't raise exceptions."""
        test_df = self.load_test_data()
        self.assertIsNone(analyze_data(test_df))

if __name__ == '__main__':
    unittest.main()
