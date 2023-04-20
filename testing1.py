import numpy as np

cea_output = np.loadtxt("data/tabulation", dtype=str)

cea_output = np.delete(cea_output, 0, 0)
cea_output = cea_output.astype(float)

cea_output_p = cea_output[:,0]
cea_output_t = cea_output[:,1]
cea_output_mach = cea_output[:,2]
cea_output_isp = cea_output[:,3]

cea_output_p0 = []
cea_output_p1 = []
cea_output_p2 = []

for i in range(len(cea_output_t)):
    r = i%3
    cea_output_p +=
    print(cea_output_p)