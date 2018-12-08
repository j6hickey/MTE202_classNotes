import numpy as np
import matplotlib.pyplot as plt

 x=np.linspace(-np.pi,np.pi,1000)

y1=np.sin(x)
y2=np.sin(2*x)

plt.plot(x,y1*y2)
plt.plot([-4,4],[0,0],'k')
plt.savefig('explan.png')
plt.show()
