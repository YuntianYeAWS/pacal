from pacal.depvars.models import Model
from pacal import *

#from pacal.depvars.copulas import *
#from pacal.depvars.models import Model
from pylab import figure, show
import numpy as _np
import time

n = 5
X = [0]*n
S = [0]*n
t0 = time.time()

#show()
#A = UniformDistr(0,1, sym = "A")
#B = UniformDistr(0,1, sym = "B")
for i in range(n):
    print "X{}".format(i)
    X[i] = BetaDistr(2, 2, sym = "X{}".format(i))
    if i==0:
        S[i] = X[0]        
    else:
        S[i] = S[i-1] + X[i]
        S[i].setSym("S{}".format(i))

M = Model(X, S[1:])
print M
M.toGraphwiz()
#M = M.inference([S[-1], S[-4]], [S[-3]], [1])
#M = M.inference([X[0], X[1]], [S[-1]], [3.5])

M_S4X5 = M.inference(wanted_rvs =[S[1], S[4]])
print "===================="
MC_S4X5 = M.inference(wanted_rvs =[S[1], S[4]], cond_rvs=[S[3]], cond_X=[2])
print "===================="
MC_X0X1 = M.inference(wanted_rvs =[X[0], X[1]], cond_rvs=[S[-1]], cond_X=[1])
print "===================="
MC_X0 = M.inference(wanted_rvs =[X[0]], cond_rvs=[S[-1]], cond_X=[1])
print "===================="

print M_S4X5
figure()
M_S4X5.plot()
figure()
M_S4X5.plot(have_3d=True)

print MC_S4X5
figure()
MC_S4X5.plot()
figure()
MC_S4X5.plot(have_3d=True)

print MC_X0X1
figure()
MC_X0X1.plot()
figure()
MC_X0X1.plot(have_3d=True)

print MC_X0
figure()
MC_X0.plot()

show()
