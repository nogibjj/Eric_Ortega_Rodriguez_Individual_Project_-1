import unittest
import pandas as pd
from io import StringIO
from main import load_data, clean_data, analyze_data

class TestTitanicFunctions(unittest.TestCase):
    
    def setUp(self):
        """
        Sets up the testing environment before each test.
        You can use StringIO to simulate a CSV file.
        """
        self.csv_data = StringIO("""PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
                                   1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
                                   2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
                                   3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S
                                   4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S
                                   5,0,3,"Allen, Mr. William Henry",male,35,0,0,373450,8.05,,S
                                   6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q
                                   """)
        
        # Create a DataFrame using the sample CSV data
        self.test_df = pd.read_csv(self.csv_data)
    
    def test_load_data(self):
        """Test if load_data function loads the CSV correctly."""
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
        df = load_data(url)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('Survived', df.columns)

    def test_clean_data(self):
        """Test if clean_data function cleans the data correctly."""
        df_cleaned = clean_data(self.test_df.copy())
        
        # Check that 'Cabin' is dropped
        self.assertNotIn('Cabin', df_cleaned.columns)
        
        # Check that missing 'Age' is filled with median
        self.assertFalse(df_cleaned['Age'].isnull().any())
        
        # Check that missing 'Embarked' is filled
        self.assertFalse(df_cleaned['Embarked'].isnull().any())

    def test_analyze_data(self):
        """Test analyze_data doesn't raise any exceptions."""
        # This function prints outputs, so we will just check that it runs without errors
        try:
            analyze_data(self.test_df)
        except Exception as e:
            self.fail(f"analyze_data raised an exception {e}")

if __name__ == '__main__':
    unittest.main()
