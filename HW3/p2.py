import requests
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Download the database of average annual precipitations in California 

url = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/4/pcp/1/1/1895-2024.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000"

response = requests.get(url)
with open("precip_ca.csv", "wb") as f:
        f.write(response.content)
        
# Read it into a Pandas dataframe
        
df = pd.read_csv("precip_ca.csv", skiprows=4, usecols=['Date', 'Value'])

# The year is recorded as a 6 digit number (last 2 for the month of January, 01). It is easy to eliminate by dividing each year by 100 and then convert to integers.
df['Date'] = df['Date'].div(100).astype('int')

print(df)



def proj(x, y):
    # Fetch the number of observations
    n = np.size(x)
 
    # Calculate the average values of x and y
    x_avg = np.mean(x)
    y_avg = np.mean(y)
 
    # Calculate the sum of cross-deviation of y and x
    SS_xy = np.sum(y*x) - n*y_avg*x_avg
    # Calculate the sum of squared deviations of x
    SS_xx = np.sum(x*x) - n*x_avg*x_avg
 
    # Calculate b and m
    m = SS_xy / SS_xx
    b = y_avg - m*x_avg
 
    return (b, m)


# We want the year column to be (year_i - year_midpoint)

b = proj(df["Date"]-df["Date"][df.shape[0]/2], df["Value"])

# Print values of b and m

print('b = ', b[0], 'm = ', b[1])

# Plot the data as scatter plot
plt.scatter(df["Date"]-df["Date"][df.shape[0]/2], df["Value"], color = "m", marker = "o", s = 30)
 
# Calculate the predicted response vector
val_pred = b[0] + b[1]*(df["Date"]-df["Date"][df.shape[0]/2])
 
# Plot the regression line
plt.plot(df["Date"]-df["Date"][df.shape[0]/2], val_pred, color = "g")
plt.xlabel('Year - Year_Midpoint')
plt.ylabel('Precipitation, mm/day')
plt.title("Average annual precipitation in California")

plt.show()