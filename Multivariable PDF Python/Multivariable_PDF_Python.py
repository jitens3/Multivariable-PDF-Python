from scipy import random
import genDataSet as genDat
import numpy as np
import matplotlib.pyplot as plt

#Establish limits
a_x = -100
b_x = 100
a_y = -100
b_y = 100

N = genDat.num_samples
mean = genDat.mean
std = genDat.std

#for i in range(N):
    #print("(X,Y): ", xData[i], yData[i])

def equation(inputX, inputY):
    angle = 1/(np.sqrt(2*np.square(std)))
    exponent1 = -((np.square(inputY - mean)) / (np.square(std)))
    exponent2 = -((np.square(inputX - mean)) / (np.square(std)))
    answer = angle * (np.exp(exponent1) * np.exp(exponent2))
    return answer

totals = []
for i in range(N):
    xData = genDat.randGen(N)
    yData = genDat.randGen(N)

    realIntegral = 0.00
    for i in range(N):
        realIntegral += equation(xData[i], yData[i])

    result = (b_y - a_y) / (float(N) * realIntegral)
    totals.append(result)

plt.title("PDF of Y=X1 + X2")
plt.hist(totals, bins = 50, ec = 'black')
plt.xlabel("Total Areas")
plt.show()

