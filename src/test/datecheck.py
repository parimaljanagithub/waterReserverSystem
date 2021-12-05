import numpy as np

EVR=[85.1,96.1,198.6,264.3,368.8,247.1,141.9,141.9,120.1,124.1,82.4,85.1]

EV=[0]*len(EVR)

for index in range(0,len(EVR)):
    EV[index]=EVR[index]/1000
S=np.zeros((301,6))
print(S[-1,0])