import numpy as np

cea_output = np.loadtxt("data/tabulation", dtype=str)
# Reads in tabulated values from cea

cea_output = np.delete(cea_output, 0, 0)
cea_output = cea_output.astype(float)
# Deletes header row and converts to floats

mr_min = float(input("Min MR: "))
mr_max = float(input("Max MR: "))
mr_interval = float(input("Interval between: "))
cea_output_mr = np.arange(mr_min, mr_max, mr_interval)
cea_output_mr = np.append(cea_output_mr, mr_max)
print(len(cea_output_mr))

cea_listout_0 = []
cea_listout_1 = []
cea_listout_2 = []

for i in range(len(cea_output)):
    r = i%3
    if r == 0:
        cea_listout_0.append(cea_output[i])
    elif r == 1:
        cea_listout_1.append(cea_output[i])
    elif r == 2:
        cea_listout_2.append(cea_output[i])

cea_arrout_0 = np.array(cea_listout_0)
cea_arrout_1 = np.array(cea_listout_1)
cea_arrout_2 = np.array(cea_listout_2)


