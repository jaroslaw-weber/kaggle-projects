import kagglehelper as kh
import pandas as pd


#class used for data analysis. contains simple tools for fast analysis.
class data_analyzer:
    #todo columns to ignore implementation
    def __init__(self, csv_path, columns_to_ignore=[]):
        self.all_data=kh.load_dataframe(csv_path)
        self.categorical, self.numerical=kh.divide_data_to_categorical_and_numerical(self.all_data)

    #summarize all of data
    def summarize_basic(self):
        kh.show_basic_info(self.all_data)

    #show info about categorical data
    def summarize_categorical(self):
        categorical_data=kh.get_columns(self.all_data,self.categorical)
        kh.summarize_all_categorical_data(categorical_data)

    #show info about numerical data
    def summarize_numerical(self):
        self.plot_histograms()

    #get few summaries about data
    def summarize_all(self):
        self.summarize_basic()
        self.summarize_categorical()
        self.summarize_numerical()

    #plot univariate histograms for data
    def plot_histograms(self):
        for column_name in self.numerical:
            column= self.all_data[column_name]
            kh.plot_histogram(column)

    #plot grid of histograms for numerical data
    def plot_histograms_grid(self):
        categorical_data=kh.get_columns(self.all_data,self.categorical)
        dataframe= pd.concat(categorical_data, axis=1)
        kh.plot_multiple_bivariate_distributions_grid(dataframe)




