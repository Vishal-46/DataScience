#Here I will be Practicing EDA on game sales CSV dataset. each and every basic steps will be practiced and uploaded more than once a week.

#First, numpy, pandas, and matplotlib are imported, then the CSV is loaded into a DataFrame and its structure.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv('C:/Users/visha/Downloads/video-game-sales.csv')
print(data.head())
print(data.info())
print(data.describe())
---
#
