import data_analyzer as da

#### Analysing US homicide reports with simple summaries and graphs.
# Data and description is available at:
# https://www.kaggle.com/murderaccountability/homicide-reports

a=da.data_analyzer("homicide-reports.csv")

a.summarize_all()

#todo plot victim and perpetrator age relations
#todo expand analysis