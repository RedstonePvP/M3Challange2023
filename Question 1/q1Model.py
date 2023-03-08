import math
import numpy as np
import matplotlib.pyplot as plt

# This function uses the formula functions and start and stop years to graph those lines
def graph(start, end, formula, color, xAjust=0, label=None):
    x = np.arange(start=start, stop=end, step=1)
    y = []
    
    # Evaluate function for each point in the range
    for year in x:
        y.append(formula(year+xAjust))
    
    # Plot the line
    plt.plot(x, y, color=color, label=label)

# Line functions calculated from the European dataset
europeBikeFormulaExp = lambda x: 55.0244*(math.exp((0.216317)*(x-2000)))
europeBikeFormulaLinear = lambda x: 222.6 * (x-2000) - 1610
europeBikeFormulaLogistic = lambda x: 37500 / (1+757.338*math.exp(-0.226413*(x-2000)))

# Raw european dataset
europeBikeX = []
europeBikeX.extend(range(2006,2019+1))
europeBikeY = [
    98,
    173,
    279,
    422,
    588,
    716,
    854,
    907,
    1139,
    1364,
    1637,
    2074,
    2767,
    3397,
]

# Line functions calculated from the French dataset
franceBikeFormulaExp = lambda x: 1.579*math.exp(.289*(x-2000))
franceBikeFormulaLinear = lambda x: 32.458*(x-2000)-310.267
franceBikeFormulaLogistic = lambda x: 3350 / (1+3612.78*math.exp(-0.328*(x-2000)))

# Raw French dataset
franceBikeX = []
franceBikeX.extend(range(2008, 2019+1))
franceBikeY = [
    15,
    24,
    38,
    37,
    46,
    57,
    78,
    102,
    134,
    278,
    338,
    388
]

# Line functions calculated from the US dataset
usBikeFormulaExp = lambda x: 2.276*math.exp(0.273*(x-2000))
usBikeFormulaLinear = lambda x: 144.5*(x-2000)-2312.7
usBikeFormulaLogistic = lambda x: 16500 / (1 + 8607*math.exp(-0.283*(x-2000)))

# Raw US dataset
usBikeX = []
usBikeX.extend(range(2018, 2022+1))
usBikeY = [
    369,
    423,
    416,
    750,
    928
]

# Setting global parameters for all graphs
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['lines.markersize'] = 10
plt.rcParams.update({'font.size': 22})

# Styles graphs with all labels, legends and parameters
def addStyle(logForm, title):
    plt.plot(2025, logForm(2025), "ro", color="black", marker="D", label="Modeled Logistic Sales")
    plt.text(2025-2.5, logForm(2025)+150, f"2025, {round(logForm(2025), 3)}")

    plt.plot(2028, logForm(2028), "ro", color="black", marker="D")
    plt.text(2028-2.5, logForm(2028)+150, f"2028, {round(logForm(2028), 3)}")

    plt.title(f"{title} E-Bike Sales Data")
    plt.xlabel("Year")
    plt.ylabel("Thousands of Units")

    plt.legend(loc='upper left', frameon=False)

# Global start and end years
startYear = 2006
endYear = 2030

# Calculate, create and style the lines for European dataset
def europePlot():
    graph(startYear, endYear, europeBikeFormulaExp, "red", label="Exponential Model")
    graph(startYear, endYear, europeBikeFormulaLinear, "blue", label="Linear Model")
    graph(startYear, endYear, europeBikeFormulaLogistic, "green", label="Logistic Model")
    plt.scatter(europeBikeX, europeBikeY, color="black", label="Dataset")
    
    addStyle(europeBikeFormulaLogistic, "Europe")

    plt.show()

# Calculate, create and style the lines for French dataset
def francePlot():
    graph(startYear, endYear, franceBikeFormulaExp, "red", label="Exponential Model")
    graph(startYear, endYear, franceBikeFormulaLinear, "blue", label="Linear Model")
    graph(startYear, endYear, franceBikeFormulaLogistic, "green", label="Logistic Model")
    plt.scatter(franceBikeX, franceBikeY, color="black", label="Dataset")

    addStyle(franceBikeFormulaLogistic, "France")

    plt.show()

# Calculate, create and style the lines for US dataset
def usPlot():
    graph(startYear, endYear, usBikeFormulaExp, "red", label="Exponential Model")
    graph(startYear, endYear, usBikeFormulaLinear, "blue", label="Linear Model")
    graph(startYear, endYear, usBikeFormulaLogistic, "green", label="Logistic Model")
    plt.scatter(usBikeX, usBikeY, color="black", label="Dataset")

    addStyle(usBikeFormulaLogistic, "US")

    plt.show()

# Show the while logistic curve for the US
def usLogisticalPlot():
    graph(startYear, 2070, usBikeFormulaLogistic, "green", label="Logistic Model")
    plt.scatter(usBikeX, usBikeY, color="black", label="Dataset")

    addStyle(usBikeFormulaLogistic, "US")
    plt.title("US E-Bike Sales Full Logistical Curve")

    plt.show()

# Output all graphs
europePlot()
francePlot()
usPlot()
usLogisticalPlot()

