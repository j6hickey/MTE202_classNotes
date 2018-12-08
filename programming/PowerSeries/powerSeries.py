############################
# Small code snippet to show the error of the power series
import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(-1.5,1.5)
y1=np.ones(len(x))
y2=1-x**2
y3=1-x**2+x**4/2
y4=1-x**2+x**4/2-x**6/6
y5=1-x**2+x**4/2-x**6/6+x**8/24
yexact  = np.exp(-x**2)

plt.scatter(x,yexact,label="exact")
plt.plot(x,y1,label="1 term")
plt.plot(x,y2,label="2 terms")
plt.plot(x,y5,label="5 terms")
plt.xlim(-1.5,1.5)
plt.ylim(0,1.05)
plt.legend()
#plt.savefig("powerSeries.png")
plt.show()
