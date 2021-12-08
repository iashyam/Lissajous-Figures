import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from numpy.linalg import slogdet
plt.style.use('seaborn-whitegrid')

#definng the range
x = np.linspace(-10,10,100)

#the amplitudes of waves
a = 4 #amplitude of first wave
b = 4
#<-----creating the graph------>
fig,ax = plt.subplots()
plt.subplots_adjust(left=0.1,bottom=0.3)



plot, = plt.plot([],[])

def init():
    theta = np.pi/2
    omega = np.pi/4
    t = np.linspace(-4,4)
    x = a*np.sin(omega*t)
    y = b*np.sin(omega*t+theta)
    plot.set_data(x,y)

init()

plt.axis('equal')
plt.title("Lissajou's Figures")
plt.xlim(-10,10)
plt.ylim(-10,10)

#slider to change ratio of frequency
pos1 = plt.axes([0.1,0.2,0.7,0.03])
slider1 = Slider(pos1,'w1/w2',valmin=1,valmax=8,valinit=1,valstep=1)

#slider to change the phase difference
pos2 = plt.axes([0.1,0.14,0.7,0.03])
slider2 = Slider(pos2,'phi',valmin=0,valmax=2*np.pi,valinit=np.pi/2)

pos3 = plt.axes([0.1,0.09,0.7,0.03])
slider3 = Slider(pos3,'a2/a1',valmin=0,valmax=1,valinit=1)

#creating the lisajoo's figure
def circle(val):
    theta = slider2.val
    omega = np.pi/4
    r = slider1.val
    b = a*slider3.val
    t = np.linspace(-4,4,600)
    x = a*np.sin(omega*t)
    y = b*np.sin(r*omega*t+theta)
    plot.set_data(x,y)

slider2.on_changed(circle)
slider1.on_changed(circle)
slider3.on_changed(circle)


plt.show()
#<-----x--x---x--x--x----->
