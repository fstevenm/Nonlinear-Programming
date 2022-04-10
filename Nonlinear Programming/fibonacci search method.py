import math
import numpy as np
import matplotlib.pyplot as plt

def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return F(n-1)+F(n-2)
        
f=lambda x  : x**4 - 14*x**3 + 60*x**2 - 70*x
#f=lambda x  : 4*x**3 - 42*x**2 + 120*x - 70
a,b=0,2
print("[",a,",",b,"]")
for i in range(1,5):
    p=1-F(5-i)/F(5-i+1)
    an=a+p*(b-a)
    bn=a+(1-p)*(b-a)
    if f(a)<f(b):
        b=bn
    else:
        a=an
    print("[",p,",",a,",",b,"]")
    
x = np.arange(0,10,0.01)
y = []
for i in x:
    y.append(f(i))
plt.plot(x,y)
plt.axis([0,2,min(y),10])
plt.grid()
plt.show()