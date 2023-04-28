dataStore = []
with open("justin/Data.txt") as data:
    with open("justin/ReadFormat.txt") as readFormat:
        with open("justin/StoreFormat.txt") as storeFormat:
            for RFLine in readFormat.readlines():
                i = 0
                j = 0
                dataLine = data.readline()
                line = []
                for char in RFLine:
                    if char == '?':
                        number = ''
                        while (not dataLine[i + j].isspace()):
                            number += dataLine[i + j]
                            j += 1
                            if ((i + j) == (len(dataLine))):
                                break
                        j -= 1
                        line.append(float(number))
                        
                    i += 1
                    
                if (line != []):
                    dataStore.append(line)
                
print(dataStore)