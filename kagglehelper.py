import seaborn as sns
from sklearn import preprocessing, ensemble
from scipy.stats import kendalltau
import pandas as pd
import random

#todo change module name

#load csv file at path
def load_dataframe(csv_path):
    return pd.read_csv(csv_path) # returns dataframe

#show info about csv
def show_basic_info(dataframe):
    print("data basic info:")
    print("size: {0}".format(dataframe.size))
    print("columns: {0}".format(dataframe.columns))

#convert to numeric data
def convert_to_numeric(column, drop_missing_data=True):
    numeric = pd.to_numeric(column, errors='coerce')
    if(drop_missing_data):
        numeric = numeric.dropna()
    return numeric

#get columns for pandas dataframe
def get_columns(dataframe, columns_names_arr):
    return dataframe[columns_names_arr]

#plot basic hex graph for pair of numerical data
def plot_hex_graph(numerical_data1, numerical_data2):
    with sns.axes_style("white"):
        hex_plt=sns.jointplot(x=numerical_data1, y=numerical_data2, kind="hex", gridsize=24, space=0, color="r")
        print("--> plotting data on hex graph....")
        sns.plt.show()

#numerical data needs to be pndas.series
def plot_histogram(numerical_data):
    print("plotting histogram for {0}".format(numerical_data.name))
    try:
        sns.distplot(numerical_data)
        sns.plt.show()
    except:
        print("failed to plot histogram")

#summarize one categorical data (csv column)
#column needs to be pandas series
def summarize_categorical_data(data_name, column):
    print("________________________")
    print("{0}:".format(data_name))
    description=column.describe()
    counts_description=description.sort(['counts'], ascending=False)
    print(counts_description)

#summarize all categorical data (multiple csv columns)
#categorical_data needs to be array of pandas series
def summarize_all_categorical_data(categorical_data):
    print("--> categorical data summaries:")
    for i in range(len(categorical_data.columns)):
        column_name=categorical_data.columns[i]
        column_data=categorical_data[column_name]
        converted_to_categorical=pd.Categorical(column_data)
        summarize_categorical_data(column_name,converted_to_categorical)

#get names of categorical and numerical data columns
def divide_data_to_categorical_and_numerical(data):
        numerical_column_names=[]
        categorical_column_names=[]
        for column_name in data.columns:
            column= data[column_name] # column type is "pandas.core.series.Series"
            few=10
            few_elements=column.values[:few] # ten first elements
            is_categorical=[type(x) for x in few_elements].count(type("string"))==few
            #print("column: {0}. Categorical {1}".format(column_name,is_categorical))
            if(is_categorical):
                categorical_column_names.append(column_name)
            else:
                numerical_column_names.append(column_name)
        return categorical_column_names, numerical_column_names

#create bivariate distributions for numerical data
def plot_multiple_bivariate_distributions_grid(dataframe):
    sns.pairplot(dataframe)