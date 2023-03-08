import math
import numpy as np
import matplotlib.pyplot as plt

# Constants and Formulas
bikeModel = lambda x: 16500 / (1 + 8607*math.exp(-0.283*(x-2000)))
startYear = 2021
endYear = 2050
years = np.arange(startYear, endYear, step=1)

# Average co2 use by car per mile in 2020 and 2000 to get average change for future
co2PerMile2000 = 449.6
co2PerMile2020 = 348.2
# x is number of years since 2000
co2Slope = lambda x: ((co2PerMile2020-co2PerMile2000) / (2020-2000))*x + 450

# Calculate the number of people who will get an E-Bike between 2021-2050
eBikeReady = bikeModel(2050) - bikeModel(2020)

# Amount of people who commute to work by car
eBikeReadyCars = eBikeReady * .756

totalCo2PerMile = co2Slope(50) * eBikeReadyCars

# 41 Miles per day average commute * 260 work days per year in US
totalCo2G = totalCo2PerMile * (41*260)

# Convert grams of CO2 to tons by dividing by 1M but then multiply by 1,000 because the bikes are in 1 per 1,000 units
totalCo2Tons = totalCo2G / 1000

# Output value of CO2 per year
print(totalCo2Tons)