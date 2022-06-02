import matplotlib as mpl
import numpy as np 
import matplotlib.pyplot as mplt
import random
# X1=A*np.sin(F*np.pi*2*T)
# X11=A*np.cos(F*np.pi*2*T)
# X12=np.abs(A*np.sin(F*np.pi*2*T))
# X2=2*np.sin(5*np.pi*2*T)
# X3=X1+X2
# for i in range(len(X1)):
#     X1[i] = X1[i]+random.random()*0.05
#     X11[i] = X11[i]+random.random()*0.05
#     X12[i] = X12[i]+random.random()*0.05
# X1=np.abs(A*np.sin(F*np.pi*2*T))
# for i in range(len(X1)):
#     X1[i] = X1[i]+random.random()*0.05
# X1=A*np.sin(F*np.pi*2*T)


F=2 
A=1

T=np.linspace(0,1,1001)

X1=A*np.sin(F*np.pi*2*T)
# X2=2*np.sin(5*np.pi*2*T)
# X3=X1+X2

X1ech = []
Tech= []
a=0

c=20

d=int(len(X1)/c)+1

q=0.2

X1q = []

for i in range(d):
    X1ech.append(X1[a])
    Tech.append(T[a])
    a += c
    X1q.append(q*np.round(X1ech[i]/q))

 # pas de quantification 

 # signal quantifié

# E = X1ech-X1q

mplt.plot(T,X1)
mplt.plot(Tech,X1ech,'o')
mplt.plot(Tech,X1q,'+')
# mplt.plot(T,E)

# mplt.plot(T,X11)
# mplt.plot(T,X12)
# mplt.plot(T,X2)
# mplt.plot(T,X3)
# mplt.legend(["X1 SIN","X1.2 COS","X1.3 ABS"])

mplt.legend(["X1","X1ech","X1eq"])
mplt.xlabel("Temps")
mplt.ylabel("Amplitude")

mplt.title("Te = 20ms")

mplt.grid()
mplt.show()
