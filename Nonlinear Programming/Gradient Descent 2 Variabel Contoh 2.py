'''Metode Gradient Descent 2 Variabel Contoh 2'''
import numpy as np
import sympy as sym

'''Iterasi gradient descent'''
def grad_desc(g,dgdx1,dgdx2,w1,w2,alpha,tol):
    global w11,w22
    n = 1
    a = 0
    w11 = []
    w22 = []
#    print("(w1,w2) awal = ({0},{1})".format(w1,w2))
    while abs(w1-a)>tol or abs(w2-b)>tol:
        a = w1
        b = w2
        w11.append(w1)
        w22.append(w2)
        w1 = w1-alpha*dgdx1(w1,w2) 
        w2 = w2-alpha*dgdx2(w1,w2) 
#        print("(w1,w2) ke-"+str(n)+" = ({0},{1})".format(w1,w2))
        n+=1
    print("Iterasi terakhir adalah","iterasi ke",n)
    return print("\nTitik nilai minimumnya adalah w1 =",
                 w1,"w2 =",w2,
                 "\ndengan g({0},{1})={2}".format(w1,w2,g(w1,w2)))

g = lambda x,y:0.26*(x**2+y**2)-0.48*x*y #g(x,y)
dgdx1 = lambda x,y: 0.52*x - 0.48*y #turunan g(x,y)) thd x
dgdx2 = lambda x,y: -0.48*x + 0.52*y #turunan g(x,y) thd y
grad_desc(g,dgdx1,dgdx2,4,2,1,0.001)


'''Kontur'''
import matplotlib.pyplot as plt
w1 = np.arange(-1,5, 0.1)
w2 = np.arange(-1,5, 0.1)
W1, W2 = np.meshgrid(w1, w2)
Z = 0.26*(W1**2+W2**2)-0.48*W1*W2
plt.contour(W1,W2,Z,50,cmap='cool')
plt.axis('square')
plt.title('$g(w_1,w_2)=0.26(w_1^2+w_2^2)-0.48w_1w_2$')
plt.xlabel('$w_1$')
plt.ylabel('$w_2$')
plt.plot(w11,w22,'yo-',label='hasil iterasi')
plt.plot(w11[0],w22[0],'go',label='titik awal iterasi')
plt.plot(w11[-1],w22[-1],'ro',label='titik akhir iterasi')
plt.legend()
plt.grid()
plt.colorbar()
plt.show()




'''Surface'''
#from numpy import *
#from numpy.linalg import norm
#from mpl_toolkits.mplot3d import Axes3D
#from matplotlib import cm
#from matplotlib.ticker import LinearLocator, FormatStrFormatter
#from matplotlib.pyplot import *
#from numpy import *
#
#def f(x, y):
#    return x**2+y**2+2
#def dfdx(x,y):
#    return 2*x
#def dfdy(x,y):
#    return 2*y
#
#x = arange(-15, 15, 0.25)
#y = arange(-15, 15, 0.25)
#X, Y = meshgrid(x, y)
#Z = X**2+Y**2+2
#
#fig = figure()
#ax = axes(projection='3d')
#surface = ax.plot_surface(X,Y,Z,cmap='viridis')
#
#ax.set_xlabel('$x$')
#ax.set_ylabel('$y$')
#ax.set_zlabel('$z$')
##ax.plot(x,y,'r', zs=0, zdir='z', label='$x^2+y^2=1$')
#
#ax.set_title('$f(x,y)=x^2+y^2+2$')
##ax.legend()
#fig.colorbar(surface, shrink=0.5, aspect=10)
#show()




#figure(1)
#CS = contour(X, Y, Z, 12, cmap=cm.coolwarm)
#clabel(CS, inline=1, fontsize=10)
#title('Kontur $f(x,y)=x^2+y^+2$')
#plot(w11,w22,'ro-')
#show()





