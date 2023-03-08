import csv
import math
import numpy as np
import matplotlib.pyplot as plt

# Thousands of Units Sold
ebikesY = [
    369,
    423,
    416,
    750,
    928
]

# Dollars
gasPriceDatasetX = [
    2.72,
    2.60,
    2.17,
    3.01,
    3.85
]

# Thousands of Dollars
carPriceDatasetX = [
    105,
    106,
    106,
    112,
    124
]

largeCarPriceDatasetX = [
    103,
    101,
    100,
    99,
    100,
    101,
    100,
    100,
    101,
    102,
    105,
    107,
    107,
    107,
    107,
    106,
    105,
    105,
    106,
    106,
    112,
    124
]

# Setting global params for all graphs
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['lines.markersize'] = 10
plt.rcParams.update({'font.size': 22})

# This function uses the formula functions and start and stop years to graph those lines
def graph(x, formula, color, xAjust=0, label=None):
    y = []
    for year in x:
        y.append(formula(year+xAjust))
    
    plt.plot(x, y, color=color, label=label)

# Bike sold logistic model from Question 1
usBikeFormulaLogistic = lambda x: 16500 / (1 + 8607*math.exp(-0.283*(x-2000)))

# This graph shows the Gas Prices vs E-Bikes Sold based on existing data
def simpleGasModel():
    plt.scatter(gasPriceDatasetX, ebikesY, color="red")
    
    # Shows line of best fit
    plt.plot(np.unique(gasPriceDatasetX), np.poly1d(np.polyfit(gasPriceDatasetX, ebikesY, 1))(np.unique(gasPriceDatasetX)), label="Line of Best Fit")

    plt.title(f"Gas Prices vs E-Bikes Sold")
    plt.ylabel("E-Bikes in Thousands")
    plt.xlabel("Gas Prices in USD")

    plt.legend(loc='upper left', frameon=False)

    plt.show()

# This graph shows the Car Prices vs E-Bikes Sold based on existing data
def simpleCarModel():
    plt.scatter(carPriceDatasetX, ebikesY, color="red")

    # Shows line of best fit
    plt.plot(np.unique(carPriceDatasetX), np.poly1d(np.polyfit(carPriceDatasetX, ebikesY, 1))(np.unique(carPriceDatasetX)), label="Line of Best Fit")

    plt.title(f"Car Prices vs E-Bikes Sold")
    plt.ylabel("E-Bikes in Thousands")
    plt.xlabel("Car Prices in USD")

    plt.legend(loc='upper left', frameon=False)

    plt.show()

# This graph shows the Car Prices vs E-Bikes Sold based on data predicted from our Q1 model
def predictedCarModel(outlier=True):
    # initialize x and y values, x values are set to the car prices
    dispX = largeCarPriceDatasetX
    dispY = []

    plt.title(f"Car Prices vs Natural Log of Modeled E-Bikes Sold")

    # Removes the outlier in 2022 
    if not outlier:
        dispX = dispX[:-1]
        plt.title("Car Prices vs Natural Log of Modeled E-Bikes Sold (outlier removed)")

    # For each year from 2001 to 2021 or 2022 depending if we exclude the outlier
    for year in range(2001, 2001+len(dispX)):
        # Calculate the bikes per thousand for that year and find natural log
        dispY.append(np.log(usBikeFormulaLogistic(year)))
    
    # Plot all the points and draw the line of best fit
    plt.scatter(dispX, dispY, color="red", label="Natural Log of Modeled E-Bikes")
    plt.plot(np.unique(dispX), np.poly1d(np.polyfit(dispX, dispY, 1))(np.unique(dispX)), label="Line of Best Fit")

    plt.ylabel("Log of E-Bikes in Thousands")
    plt.xlabel("Car Prices in USD")

    plt.legend(loc='upper left', frameon=False)

    plt.show()

# This graph shows the Gas Prices vs E-Bikes Sold based on data predicted from our Q1 model
def predictedGasModel():
    dispX = []
    dispY = []
    
    # gasPrices.csv contains years and corresponding gas prices sourced from the supplied data for Q2
    file = open("gasPrices.csv", "r")
    data = list(csv.reader(file, delimiter=","))[10:31]
    file.close()

    # For each year from the data - 2000 to 2021
    for year in data:
        # Add the gas price to the list of x points
        dispX.append(float(year[1].replace(" ", "")))
        # Calculate the bikes per thousand for that year and find natural log
        dispY.append(np.log(usBikeFormulaLogistic(int(year[0]))))
    
    # Plot all points and draw the line of best fit
    plt.scatter(dispX, dispY, color="red", label="Natural Log of Modeled E-Bikes")
    plt.plot(np.unique(dispX), np.poly1d(np.polyfit(dispX, dispY, 1))(np.unique(dispX)), label="Line of Best Fit")

    plt.title(f"Gas Prices vs Natural Log of Modeled E-Bikes Sold")
    plt.ylabel("Log of E-Bikes in Thousands")
    plt.xlabel("Gas Prices in USD")

    plt.legend(loc='upper left', frameon=False)

    plt.show()

simpleCarModel()
predictedCarModel()
predictedCarModel(False)
simpleGasModel()
predictedGasModel()