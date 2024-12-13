#Here I will be Practicing EDA on game sales CSV dataset. each and every basic steps will be practiced and uploaded more than once a week.

#First, numpy, pandas, seaborn and matplotlib are imported, then the CSV is loaded into a DataFrame and its structure.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv('C:/Users/visha/Downloads/video-game-sales.csv')
#First step in Data science is to analyse the data which means exploratory analysis of the dataset
print(data.head())
print(data.info())
print(data.describe())
#Here The information of the dataset like no. of columns, what are all the columns their datatype and also its quantity are shown.
#After this let us try to visualize a graph. Taking Year column and lets try to visualize it in a histogram.Histogram can be visualized using seaborn
sns.histplot(data['Year'], bins=30) #here there will be a histogram(graph) with column year in the x axis and count on the y axis.
#data cleaning, First step in Data cleaning is checking the missing values of the dataset for that we use dataset name.isna().sum().
print(data.isna().sum())
#when the dataframe or dataset has missing values
data.dropna(inplace=True)  # Removes all rows with ANY missing values.
data.dropna(subset=['ColumnName'], inplace=True)  # Removes rows where 'ColumnName' has NaN.
#To fill these missing values we will use .fillna method on columns
data['ColumnName'].fillna('Missing', inplace=True)  # Replace NaN in 'ColumnName' with 'Missing'.
data['ColumnName'].fillna(data['ColumnName'].mean(), inplace=True)  # Fill NaN with column's mean.
data['ColumnName'].fillna(data['ColumnName'].median(), inplace=True)  # Fill NaN with median.
#now lets again check for the missing values 
print(data.isna().sum())  # Shows the count of NaN in each column.
#These are all the basic steps of exploratorydata analysis on a dataset.We can even perform more actions in a dataset.
--

