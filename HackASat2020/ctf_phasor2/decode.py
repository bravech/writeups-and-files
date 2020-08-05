from scipy.io import wavfile
import matplotlib.pyplot as plt

fs, data = wavfile.read('demod.wav')
chan1 = data[:, 0]
plt.hist(chan1)
plt.show()

symbs = [] # possible= 0, 1, 2, 3


print(data)

#Dividing between symbols: < 75 & > 175 

last = [0, 0]
for samp in data:
    x, y = samp
    a = b = None
    if x < 75: 
        a = 0
    if x > 175: 
        a = 1
    if y < 75: 
        b = 0
    if y > 175: 
        b = 1
    symbs.append([a, b])

diff_symbs = []
last = [0, 0]
for symb in symbs:
    if  symb == last:
        diff_symbs.append(0)



