import matplotlib.pyplot as plt
from scipy import *
from scipy import integrate
from scipy.integrate import ode
import numpy as np

fig = plt.figure(num=1)
ax=fig.add_subplot(111)

## Vector field function
def vf(t,x):
  dx=np.zeros(2)
  dx[0]=1
 # dx[1]=x[0]**2-x[0]-2
  dx[1]= 4-3*x[0] -x[1]
  return dx

#Solution curves
t0=0; tEnd=10; dt=0.01;
r = ode(vf).set_integrator('vode', method='bdf',max_step=dt)
ic=[[-1,7.5], [-1,0], [1,0]]
color=['r','b','g']
for k in range(len(ic)):
    Y=[];T=[];S=[];
    r.set_initial_value(ic[k], t0).set_f_params()
    while r.successful() and r.t +dt < tEnd:
        r.integrate(r.t+dt)
        Y.append(r.y)

    S=np.array(np.real(Y))
    ax.plot(S[:,0],S[:,1], color = color[k], lw = 1.25)

#Vector field
X,Y = np.meshgrid( np.linspace(-1,2,20),np.linspace(-10,10,20) )
U = 1
V = 4-3*X -Y
#Normalize arrows
N = np.sqrt(U**2+V**2)
U2, V2 = U/N, V/N
ax.quiver( X,Y,U2, V2)


plt.xlim([-1,2])
plt.ylim([-10,10])
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig("DirectionField.pdf")
plt.show()
