import numpy as np
import data

cea_output = np.loadtxt("data/cea_output_34.4bar", dtype=str)

print(len(cea_output))
cea_output = np.delete(cea_output, 0, 0)
cea_output = cea_output.astype(float)
print(cea_output[:,0])