import data_analyzer as da

#### Analysing data about IBM employees
# Data and description is available at:
# https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset

#simple and fast summary
a= da.data_analyzer("ibm-employees.csv", columns_to_ignore=["EmployeeCount"])

a.summarize_all()

#todo expand analysis