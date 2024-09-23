import unittest
import pandas as pd
from io import StringIO
from main import load_data, clean_data, analyze_data

class TestTitanicFunctions(unittest.TestCase):
    
    def setUp(self):
        """Set up the testing environment."""
        self.csv_data = StringIO(
            """PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
            1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
            2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
            3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S
            4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S
            5,0,3,"Allen, Mr. William Henry",male,35,0,0,373450,8.05,,S
            6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q
            """
        )
        self.test_df = pd.read_csv(self.csv_data)
    
    def test_load_data(self):
        """Test load_data function."""
        df = load_data("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('Survived', df.columns)

    def test_clean_data(self):
        """Test clean_data function."""
        df_cleaned = clean_data(self.test_df.copy())
        self.assertNotIn('Cabin', df_cleaned.columns)
        self.assertFalse(df_cleaned['Age'].isnull().any())
        self.assertFalse(df_cleaned['Embarked'].isnull().any())

    def test_analyze_data(self):
        """Test analyze_data doesn't raise exceptions."""
        self.assertIsNone(analyze_data(self.test_df))

if __name__ == '__main__':
    unittest.main()
