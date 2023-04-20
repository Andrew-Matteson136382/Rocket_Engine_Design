import numpy as np

cea_output = np.loadtxt("data/tabulation", dtype=str)

cea_output = np.delete(cea_output, 0, 0)
cea_output = cea_output.astype(float)

cea_output1_p = cea_output[:,0]
cea_output1_t = cea_output[:,1]
cea_output1_mach = cea_output[:,2]
cea_output1_isp = cea_output[:,3]



