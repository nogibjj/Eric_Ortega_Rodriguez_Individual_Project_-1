# My Titanic Project IDS 706: Individual Project 1
![image](titanic.jpeg)

## IDS 706: Individual Project 1
## Continous Integration using Github Actions of Python Data Science Project
### Eric Ortega Rodriguez

The purpose of this assignment was to create a a python script that utilizes pandas to generate summary statistics.


## YouTube Video
[Click Here For Demo]()

## Assignment Requirements
* __`Jupyter Notebook`__ with:
  - Cells that perform __descriptive statistics using Polars or Panda__
  - Tested by using __nbval plugin__ for __pytest__
*	__`Python Script`__ performing the same descriptive statistics using Polars or Pandas
* __`lib.py`__ file that shares the common code between the script and notebook
* __`Makefile`__ with the following:
  - Run all tests __(must test notebook and script and lib)__
  - Formats code with __Python Black__
  - Lints code with __Ruff__
  - Installs code via:  __pip install -r requirements.txt__
*	__`test_script.py`__ to test script
*	__`test_lib.py`__ to test library
*	Pinned __`requirements.txt`__
*	__`GitHub Actions`__ performs all four Makefile commands with __badges__ for each one in the `README.md`



## Data Set Used in this Project
The data set used in this project was pulled from github. The Titanic dataset is a well-known dataset in the field of data science and machine learning, often used for educational purposes. It contains information about the passengers aboard the RMS Titanic, which sank on its maiden voyage in April 1912 after hitting an iceberg. The dataset provides valuable insights into the factors that influenced survival rates during this tragic event.

This dataset includes a range of demographic and socio-economic information about the passengers, such as their age, gender, class, and ticket fare. Analysts and data scientists use this dataset to explore various questions.
The data used can be found here: 
https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv

## Functions
calculator.py contains the following functions: 
1. ```calculate_correlation_matrix``` -- creates correlation matrix
2. ```survival_rates_by_group``` -- calculates survival rates grouped by column
3. ```plot_correlation_matrix``` -- plots the correlation matrix 
4. ```glot_survival_rates``` -- plots survival rates

## Data Visualizations
Histogram of final exam scores and scatter plot of hours studied vs final exam score generated from ```generate_visualization(col, col2)``` in ```main.py```
![image](correlation-matrix.png)
![image](survival_by_class.png)
![image](survival_by_sex.png)

