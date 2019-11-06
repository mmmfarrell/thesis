from __future__ import print_function
import numpy as np
import os,sys,inspect,scipy.io
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

np.set_printoptions(linewidth=150)

LOG_WIDTH = 1 + 13 + 4 + 13 + 4 + 1

fname = sys.argv[1]
data = np.reshape(np.fromfile(fname, dtype=np.float64), (-1, LOG_WIDTH)).T

t = data[0,:]
x = data[1:14,:]
u = data[14:18,:]
xc = data[18:31, :]
ur = data[31:35, :]

compute_time = data[35, :]
print("Mean compute time")
print(np.mean(compute_time), "micro seconds")
print("STD")
print(np.std(compute_time), "micro seconds")

print("Saving mat file...")

mat_name = "./" + fname.split("/")[-1].split(".")[0] + ".mat"
scipy.io.savemat(mat_name, {'t':t, 'x':x, 'u':u, 'xc':xc, 'ur':ur, 'compute_time':compute_time})

print("Finished writing to " + mat_name)
