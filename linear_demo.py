# linear_demo.py
# Simple demonstration of Linear Regression using the linear_model
# ~dwulf,

#Importing other libraries,
#Aka standing on the shoulders of giants
#---------------------------------------------------------
# pandas; for utilizing a dataframe
# sklearn; the machine learining library for this example
# matplotlib, to plot out and illustrate our data
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data
# using the pd method read_fwf() we read the sample.txt data
# and using the data_frame object we assign the Brain column
# to the x_values variable and Body to the y_values variable
dataframe = pd.read_fwf('sample.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

#train model on data

body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

#visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()
