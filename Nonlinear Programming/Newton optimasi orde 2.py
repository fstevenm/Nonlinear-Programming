import numpy as np
import sympy as sym
def newton(g,dgdx1,dgdx2,w1,w2,alpha,tol):
    global w11,w22
    n = 0
    a,b = 0,0
    w11 = []
    w22 = []
#    print("(w1,w2) awal = ({0},{1})".format(w1,w2))
    while abs(w1-a)>tol or abs(w2-b)>tol:
        n+=1
        a = w1
        b = w2
        w11.append(w1)
        w22.append(w2)
        w1 = w1-alpha*grad1(w1)
        w2 = w2-alpha*grad2(w2)
#        print("(w1,w2) ke-"+str(n)+" = ({0},{1})".format(w1,w2))
    print("Iterasi terakhir adalah","iterasi ke",n)
    return print("\nTitik nilai minimumnya adalah w1 =",
                 w1,"w2 =",w2,
                 "\ndengan g({0},{1})={2}".format(w1,w2,g(w1,w2)))
x = sym.symbols('x')
y = sym.symbols('y')
g_simbol = 0.26*(x**2+y**2)-0.48*x*y
g = sym.lambdify([x,y],g_simbol)
dgdx1_simbol = 0.52*x - 0.48*y #turunan f(x) thd x
dgdx2_simbol =  -0.48*x + 0.52*y #turunan f(x) thd y
dgdx1 = sym.lambdify([x,y],dgdx1_simbol)
dgdx2 = sym.lambdify([x,y],dgdx2_simbol)
mat1 = np.array([[dgdx1_simbol],[dgdx2_simbol]])
mat_invers_df2 = np.array([[13,12],[12,13]])
mat = np.dot(mat_invers_df2 ,mat1)
grad1 = sym.lambdify([x],mat[0][0])
grad2 = sym.lambdify([y],mat[1][0])
newton(g,dgdx1,dgdx2,4,2,1,0.001)

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