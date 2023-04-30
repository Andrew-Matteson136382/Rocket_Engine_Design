
with open('data/output') as ceaOut:
    ceaOutLines = [line.rstrip() for line in ceaOut]

    ceaEq = []

    for i in range(len(ceaOutLines)):
        if 'THEORETICAL ROCKET PERFORMANCE ASSUMING EQUILIBRIUM' in ceaOutLines[i]:
            ceaEq.append([[], [], [], [], [], [], []])
            for j in range(i, len(ceaOutLines), 1):
                if 'WEIGHT FRACTION' in ceaOutLines[j]:
                    break
                elif 'O/F' in ceaOutLines[j]:
                    tmp = ceaOutLines[j].split()
                    ceaEq[-1][0].append(tmp[1])
                elif 'Pinf/P' in ceaOutLines[j]:
                    tmp = ceaOutLines[j].split()
                    for k in range(1, len(tmp), 1):
                        ceaEq[-1][1].append(tmp[k])
                elif 'P, BAR' in ceaOutLines[j]:
                    tmp = ceaOutLines[j].split()
                    for k in range(2, len(tmp), 1):
                        ceaEq[-1][2].append(tmp[k])
                elif 'T, K' in ceaOutLines[j]:
                    tmp = ceaOutLines[j].split()
                    for k in range(2, len(tmp), 1):
                        ceaEq[-1][3].append(tmp[k])
                elif 'RHO, KG/CU M' in ceaOutLines[j]:
                    tmp = ceaOutLines[j].split()
                    for k in range(3, len(tmp), 1):
                            ceaEq[-1][4].append(tmp[k])
                elif 'GAMMAs' in ceaOutLines[j]:
                    tmp = ceaOutLines[j].split()
                    for k in range(1, len(tmp), 1):
                        ceaEq[-1][5].append(tmp[k])
                elif 'MACH NUMBER' in ceaOutLines[j]:
                    tmp = ceaOutLines[j].split()
                    for k in range(2, len(tmp), 1):
                        ceaEq[-1][6].append(tmp[k])

for i in range(len(ceaEq)):
    if (ceaEq[i] == ceaEq[-1]) or (i >= len(ceaEq)):
        break
    elif (ceaEq[i][0] == ceaEq[i+1][0]) and (ceaEq[i][1][1] == ceaEq[i+1][1][1]):
        for j in range(2, len(ceaEq[i+1][1]), 1):
            ceaEq[i][1].append(ceaEq[i+1][1][j])
            ceaEq[i][2].append(ceaEq[i+1][2][j])
            ceaEq[i][3].append(ceaEq[i+1][3][j])
            ceaEq[i][4].append(ceaEq[i+1][4][j])
            ceaEq[i][5].append(ceaEq[i+1][5][j])
            ceaEq[i+1].append('delete')

for i in range(len(ceaEq[2])):
    # for j in range(len((ceaEq[i]))):
    print(ceaEq[2][i])
# print(ceaEq[1])
