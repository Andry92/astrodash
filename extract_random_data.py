import random
import linecache
import os

# questo script estrae 900 supernove random e le mette in un file

if os.path.exists("randomData.txt"):
  os.remove("randomData.txt")

def random_lines(rng, filename):
    idxs = random.sample(range(rng), 50)
    return [linecache.getline(filename, i) for i in idxs]

cont=0

with open('randomData.txt', 'a') as the_file:

    for line in random_lines(503, 'spettri/503 Ia.txt'):
        print (line)
        the_file.write(line)
        cont+=1

    for line in random_lines(454, 'spettri/454 Ia-norm.txt'):
        print (line)
        the_file.write(line)
        cont+=1

    for line in random_lines(135, 'spettri/135 Ia-91T.txt'):
        print (line)
        the_file.write(line)
        cont+=1

    for line in random_lines(53, 'spettri/53 Ib-norm.txt'):
        print (line)
        the_file.write(line)
        cont+=1

    for line in random_lines(110, 'spettri/110 IIb.txt'):
        print (line)
        the_file.write(line)
        cont+=1

    for line in random_lines(106, 'spettri/106 Ic-broad.txt'):
        print (line)
        the_file.write(line)
        cont+=1

    for line in random_lines(340, 'spettri/340 IIP.txt'):
        print (line)
        the_file.write(line)
        cont+=1

    for line in random_lines(95, 'spettri/95 IIn.txt'):
        print (line)
        the_file.write(line)
        cont+=1

print(cont)
