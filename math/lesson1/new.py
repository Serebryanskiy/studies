# %matplotlib inline
import matplotlib.pyplot as plt

x=[]
y=[]

for i in range(100):
    _x=i/100
    x.append(_x)
    y.append(2*_x)
plt.plot(x,y)

x=input()