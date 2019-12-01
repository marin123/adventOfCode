import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
from numpy import array
import time
import numpy as np

f = open("input_day_10.txt", "r")
x_list=[]
y_list=[]
vx_list=[]
vy_list=[]
for line in f:
    data = line.split(",")
    x = int(data[0][-6:])
    y = int(data[1][0:7])
    v_x = int(data[1][-2:])
    v_y = int(data[2][0:3])
    # print(data, x,y,v_x, v_y)
    x_list.append(x)
    y_list.append(y)
    vx_list.append(v_x)
    vy_list.append(v_y)
x_np = array(x_list)
y_np = array(y_list)
vx_np= array(vx_list)
vy_np = array(vy_list)
t = 0
plt.plot(x_np, y_np, 'o', color='black')
plt.show()
while t<20000:
    x_np = x_np + vx_np
    y_np = y_np + vy_np
    if t < 10700 and t > 10650 and t%1==0:
        plt.plot(x_np, y_np, 'o', color='black')
        plt.show()
        plt.pause(1e-17)
        time.sleep(0.1)
        print(t)
    t += 1

