#get_ipython().magic(u'matplotlib inline')
import matplotlib.pylab as plt
import random
import math

x, y = random.random(), random.random()
points=[]
points1=[]
points2=[]
points3=[]
points4=[]
points5=[]
points6=[]
points7=[]
points8=[]
points9=[]
points10=[]
points11=[]
points12=[]
points13=[]
points14=[]
points15=[]


for i in xrange(200000):
    rand = random.random()
    if rand < 0.01:
        x, y = 0.0, 0.16 * y;
    elif rand < 0.86:
        newx = (0.85 * x) + (0.04 * y)
        newy = (-0.04 * x) + (0.85 * y) + 1.6
        x, y = newx, newy
    elif rand < 0.93:
        newx = (0.2 * x) - (0.26 * y)
        newy = (0.23 * x) + (0.22 * y) + 1.6
        x, y = newx, newy
    else:
        newx = (-0.15 * x) + (0.28 * y)
        newy = (0.26 * x) + (0.24 * y) + 0.44
        x, y = newx, newy
    z=[x,y]
    points.append(z)
    z1=[-x,-y]
    points1.append(z1)
    z2=[x,-y]
    points2.append(z2)
    z3=[-x,y]
    points3.append(z3)
    z4=[x*math.cos(math.pi/2.)-y*math.sin(math.pi/2.),x*math.sin(math.pi/2.)+y*math.cos(math.pi/2.)]
    points4.append(z4)
    z5=[x*math.cos(math.pi/2.)+y*math.sin(math.pi/2.),-x*math.sin(math.pi/2.)+y*math.cos(math.pi/2.)]
    points5.append(z5)
    z6=[-x*math.cos(math.pi/2.)+y*math.sin(math.pi/2.),x*math.sin(math.pi/2.)+y*math.cos(math.pi/2.)]
    points6.append(z6)
    z7=[-x*math.cos(math.pi/2.)-y*math.sin(math.pi/2.),-x*math.sin(math.pi/2.)-y*math.cos(math.pi/2.)]
    points7.append(z7)
    z9=[+x*math.cos(math.pi/4.)+y*math.sin(math.pi/4.),-x*math.sin(math.pi/4.)+y*math.cos(math.pi/4.)]
    points9.append(z9)
    z10=[-x*math.cos(math.pi/4.)+y*math.sin(math.pi/4.),x*math.sin(math.pi/4.)+y*math.cos(math.pi/4.)]
    points10.append(z10)
    z11=[-z9[0],-z9[1]]
    points11.append(z11)
    z8=[-z10[0],-z10[1]]
    points8.append(z8)
    z12=[z9[0]*math.cos(math.pi/2.)-z9[1]*math.sin(math.pi/2.),z9[0]*math.sin(math.pi/2.)+z9[1]*math.cos(math.pi/2.)]
    points12.append(z12)
    z13=[z9[0]*math.cos(math.pi/2.)+z9[1]*math.sin(math.pi/2.),-z9[0]*math.sin(math.pi/2.)+z9[1]*math.cos(math.pi/2.)]
    points13.append(z13)
    z14=[z8[0]*math.cos(math.pi/2.)-z8[1]*math.sin(math.pi/2.),z8[0]*math.sin(math.pi/2.)+z8[1]*math.cos(math.pi/2.)]
    points14.append(z14)
    z15=[z8[0]*math.cos(math.pi/2.)+z8[1]*math.sin(math.pi/2.),-z8[0]*math.sin(math.pi/2.)+z8[1]*math.cos(math.pi/2.)]
    points15.append(z15)

fig, ax = plt.subplots(1,figsize=(20,20))
plt.plot([p[0] for p in points9],[p[1] for p in points9],'d',color='cyan')
plt.plot([p[0] for p in points10],[p[1] for p in points10],'bd')
plt.plot([p[0] for p in points8],[p[1] for p in points8],'bd')
plt.plot([p[0] for p in points11],[p[1] for p in points11],'d',color='cyan')
plt.plot([p[0] for p in points14],[p[1] for p in points14],'d',color='grey')
plt.plot([p[0] for p in points12],[p[1] for p in points12],'md')
plt.plot([p[0] for p in points13],[p[1] for p in points13],'md')
plt.plot([p[0] for p in points15],[p[1] for p in points15],'d',color='grey')
plt.plot([p[0] for p in points3],[p[1] for p in points3],'d',color='orange')
plt.plot([p[0] for p in points],[p[1] for p in points],'rd')
plt.plot([p[0] for p in points1],[p[1] for p in points1],'rd')
plt.plot([p[0] for p in points2],[p[1] for p in points2],'d',color='orange')
plt.plot([p[0] for p in points4],[p[1] for p in points4],'gd')
plt.plot([p[0] for p in points6],[p[1] for p in points6],'yd')
plt.plot([p[0] for p in points5],[p[1] for p in points5],'gd')
plt.plot([p[0] for p in points7],[p[1] for p in points7],'yd')

plt.axis('equal')
plt.axis('off')
plt.show()
