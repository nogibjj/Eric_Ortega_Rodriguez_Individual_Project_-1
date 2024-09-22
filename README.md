
[![CI](https://github.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_2/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_2/actions/workflows/hello.yml)

# Eric Ortega Rodriguez's Pandas Descriptive Statistics Script

## ☑️ Requirements (Mini Project 2):
1. Python script using Pandas for descriptive statistics
2. Read a dataset (CSV or Excel)
3. Generate summary statistics (mean, median, standard deviation)
4. Create at least one data visualization

## ☑️ Deliverables:
1. Python script 
2. CI/CD with badge
3. Generated summary report (PDF or markdown) via CI/CD for extra credit or make your own PDF or MD file and push it 

## ☑️ The Data Being Used
The data being utilized is coming from a GitHub database which can be found [here](https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv) 

The data found here give the frequency breakdown of substance abuse among different age groups. 

## ☑️ Analysis and Calculations
Summary statistics included are Mean, Median, Standard Deviation, and Max. 


## ☑️ Explanation and Breakdown of Repo Components: 

[main.py](main.py)

Function: Main entry point of a project containing program. 

[requirements.txt](requirements.txt)

Function: This file lists all the Python dependencies required for the project. It specifies the exact versions of packages needed, making it easy to install all dependencies with a single command. For this project specifically, we will be using pandas and matplotlib. 

[hello.yml](.github/workflows/hello.yml)

Function: This file is typically used for workflows in CI/CD (Continuous Integration/Continuous Deployment) systems, like GitHub Actions. It defines automated processes, such as running tests, building the project, or deploying it when certain events occur.

[Makefile](Makefile)

Function: A Makefile is used to automate tasks in software development, especially compiling and building projects. It contains a set of rules defining how to execute commands for tasks like building, testing, or cleaning up files. This helps streamline repetitive commands.

[test.py](test.py)

Function: test.py is a script typically used to contain test cases for a project and data set. It includes functions or classes designed to verify that the code works as expected. 

## ☑️ Visualization: 
Highlights the frequency of alcohol use among different age groups.

![Visualization](Chart.png)
