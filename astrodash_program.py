import astrodash
import re
from sklearn.metrics import confusion_matrix
import numpy as np

f=open("randomData.txt", "r")
f1 = f.readlines()


spectrum = [] # spectrum list
y_true = [] # vettore dei veri

for x in f1:
    randomSNE = re.findall("SN\w+", x)
    sne = 'osc-' + randomSNE[0] + '-10'
    sne = sne.replace('\n', '')
    spectrum.append((sne, 'osc'))

    randomType = re.findall("I[A-Za-z][-]*[a-zA-Z]*[0-9]*[a-zA-Z]*", x)
    y_true.append(randomType[0])

print(spectrum)
print("dim spectrum: ", len(spectrum))
print("y_true: ", y_true)

'''
spectrum = [
    ('osc-AT2019jvj-10', 'osc')
]
print(spectrum)
'''

# Create filenames and knownRedshifts lists
filenames = [i[0] for i in spectrum]
knownRedshifts = [i[1] for i in spectrum]
#print(knownRedshifts)

# Classify all spectra
classification = astrodash.Classify(filenames, knownRedshifts, classifyHost=False, knownZ=True, smooth=6)
bestFits, redshifts, bestTypes, rlapFlag, matchesFlag, redshiftErrs = classification.list_best_matches(n=5, saveFilename='best_fits.txt')

# estraggo i tipi predetti
f2 = open('best_fits.txt').read()
f2 = f2.strip().replace('\n', '')   # rimuovo tutte le newLine in best_fits

y_pred = [] # vettore dei predetti

y_pred = re.findall("I[A-Za-z][-]*[a-zA-Z]*[0-9]*[a-zA-Z]*['][,]", f2)

i=0
for x in y_pred:
    y_pred[i] = x.replace("'", "")
    y_pred[i] = y_pred[i].replace(',', '')
    i+=1

print("y_true: ", y_true)
print("y_pred: ", y_pred)

# calcolo la matrice di confusione
conf_m = confusion_matrix(y_true, y_pred,
    labels=["Ia", "Ia-norm", "Ia-91T", "Ib-norm", "IIb", "Ic-broad", "IIP", "IIn"])

print("matrice di confusione", conf_m)

# calcolo la matrice dei rate a partire dalla matrice di confusione
conf_m = conf_m.astype(np.float) # converto in float la matrice di confusione
rateMatrix = [[conf_m[i][j]/50 for j in range(8)] for i in range(8)]
print("matrice dei rate", rateMatrix)

# scrivo sul file rateMatrices le matrici di rate da utilizzare per lo script finale
f4 = open("rateMatrices.txt", "a")
np.savetxt(f4, rateMatrix, fmt="%s", delimiter=',', footer='\n')