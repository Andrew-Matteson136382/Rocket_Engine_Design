

class CEA:
    def __int__(self, mr, pressure, temperature, density, gamma, mach):
        self.mr = []
        self.pressure = []
        self.temperature = []
        self.density = []
        self.gamma = []
        self.mach = []

with open('data/output') as ceaOut:
    ceaOutLines = [line.rstrip() for line in ceaOut]

    ceaEq = [[], [], [], [], [], []]

    for i in range(len(ceaOutLines)):
        if 'EQUILIBRIUM' in ceaOutLines[i]:
            for j in range(i, len(ceaOutLines), 1):
                if 'WEIGHT FRACTION' in ceaOutLines[j]:
                    break
                elif 'O/F' in ceaOutLines[j]:
                    tmp = ceaOutLines[j].split()
                    ceaEq[0].append(tmp[1])
                elif ' Pinf/P' in ceaOutLines[j]:
                    tmp = ceaOutLines[j].split()
                    for k in range(1, len(tmp), 1):
                        ceaEq.append(tmp[k])
    print(ceaEq)
    # # print(ceaEq)

    # ceaOutChunked = []
    #
    # start = 0
    # end = len(ceaOutLines)
    # step = 134
    # for i in range(start, end, step):
    #     x = i
    #     ceaOutChunked.append(ceaOutLines[x:x + step])
    #     print(ceaOutLines[x:x + step])
    #
    # for i in range(len(ceaOutChunked)):
    #     for j in range(len(keyLines)):
    #         pass


