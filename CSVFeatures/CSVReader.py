import math
import numpy as np



def leftEyeRubineFeatures(fileName, name):
    coords = np.genfromtxt(fileName, delimiter=',', skip_header=1)

    yMin = coords[0][2]
    yMax = coords[0][2]
    f8 = 0.0
    for i in range(len(coords)):
        if coords[i][2] < yMin:
            yMin = coords[i][2]
        if coords[i][2] > yMax:
            yMax = coords[i][2]


    length = len(coords) - 1

    for x in range(1, length):
        f8 = f8 + math.fabs(math.sqrt(((coords[x][1]-coords[x-1][1])**2) + ((coords[x][2]-coords[x-1][2])**2)))

    xMax = coords[length][1]
    xMin = coords[0][1]

    allFeatures = []

    allFeatures.append((coords[2][1]-coords[0][1])/math.sqrt(((coords[2][2]-coords[0][2])**2)+(coords[2][1]-coords[0][1])**2)) #f1
    allFeatures.append((coords[2][2]-coords[0][2])/math.sqrt(((coords[2][2]-coords[0][2])**2)+(coords[2][1]-coords[0][1])**2)) #f2
    allFeatures.append(math.sqrt(((yMax - yMin)**2)+((xMax - xMin)**2))) #f3
    allFeatures.append(math.atan((yMax - yMin)/(xMax-xMin))) #f4
    f5 = math.sqrt(((coords[length][1] - coords[0][1])**2) + ((coords[length][2]- coords[0][2])**2)) #f5
    allFeatures.append(f5)
    allFeatures.append((coords[length][1] - coords[0][1])/f5) #f6
    allFeatures.append((coords[length][2] - coords[0][2]) / f5) #f7
    allFeatures.append(f8) #f8
    allFeatures.append(name) #classifier
    print allFeatures

def findFeatures(name, total, starting):
    #print(name)
    for y in range(starting, total + 1):
        fileName = name + "_" + str(y) + ".csv"
        leftEyeRubineFeatures(fileName, name)


findFeatures("alpha", 20, 0)
findFeatures("beta", 20, 0)
findFeatures("delta", 23, 0)
findFeatures("epsilon", 37, 1)
findFeatures("eta", 32, 1)
findFeatures("gamma", 16, 0)
findFeatures("iota", 38, 1)
findFeatures("theta", 33,1)
findFeatures("zeta", 34, 1)
findFeatures("mu", 35, 1)
findFeatures("lamda", 36, 1)



