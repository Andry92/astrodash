import fileinput
import numpy as np
import matplotlib.pyplot as plt

filename = 'rateMatrices.txt'

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace('# \n', ''), end='')

with open(filename, 'r') as f:
    l = [[num for num in line.strip().split(',')] for line in f]
print(l)

# funzione per convertire in float gli elementi nelle matrici
def convertToFloat(matrix):
    i = 0
    j = 0
    for i in range(8):
        for j in range(8):
            matrix[i][j] = float(matrix[i][j])
            j += 1
        i += 1
    return matrix

# funzione per separare le 10 matrici di rate per fare la media
def fillRateMatrix(i, rateMatrix):
    for element in range(8):
        rateMatrix.append(l[i])
        i += 1
    rateMatrix = convertToFloat(rateMatrix)
    print(rateMatrix)

    return rateMatrix

rateMatrix1 = []
rateMatrix2 = []
rateMatrix3 = []
rateMatrix4 = []
rateMatrix5 = []
rateMatrix6 = []
rateMatrix7 = []
rateMatrix8 = []
rateMatrix9 = []
rateMatrix10 = []

rateMatrix1 = fillRateMatrix(0, rateMatrix1)
rateMatrix2 = fillRateMatrix(8, rateMatrix2)
rateMatrix3 = fillRateMatrix(16, rateMatrix3)
rateMatrix4 = fillRateMatrix(24, rateMatrix4)
rateMatrix5 = fillRateMatrix(32, rateMatrix5)
rateMatrix6 = fillRateMatrix(40, rateMatrix6)
rateMatrix7 = fillRateMatrix(48, rateMatrix7)
rateMatrix8 = fillRateMatrix(56, rateMatrix8)
rateMatrix9 = fillRateMatrix(64, rateMatrix9)
rateMatrix10 = fillRateMatrix(72, rateMatrix10)

averageMatrix = (8,8)
averageMatrix = np.zeros(averageMatrix)

for i in range(8):
   for j in range(8):
       averageMatrix[i][j] = float(rateMatrix1[i][j] + rateMatrix2[i][j] + rateMatrix3[i][j] + rateMatrix4[i][j]\
                             + rateMatrix5[i][j]  + rateMatrix6[i][j] + rateMatrix7[i][j] + rateMatrix8[i][j]\
                             + rateMatrix9[i][j] + rateMatrix10[i][j])

print("averageMatrix dopo somma", averageMatrix)

for i in range(8):
    for j in range(8):
        averageMatrix[i][j] = float(averageMatrix[i][j]/10)

print("averageMatrix dopo media", averageMatrix)

x = ["Ia", "Ia-norm", "Ia-91T", "Ib-norm", "IIb", "Ic-broad", "IIP", "IIn"]
y = []

for i in range(8):
    y.append(averageMatrix[i][i])

print("diagonale matrice media: ", y)

plt.bar(x, y)
plt.xlabel('Supernova type', fontsize=8)
plt.ylabel('Accuracy', fontsize=8)
plt.title('Supernova spectrum classification')
plt.xticks(fontsize=7, rotation=30)
plt.show()