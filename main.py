import random

EULER = 2.7182818284590452353602874713527


def sigmoidalFunction(x,d):
    if d == True:
        #simplificacion de la derivada x * (1-x)
        return sigmoidalFunction(x,False)*(1-sigmoidalFunction(x,False))
    return 1/(1+EULER**(-x))


def dotProduct(x,y):
    # This function only calculates the dot product of a matrix "x" and an array "y".
    dotProduct = 0.0
    for i in range(len(x)):
        #for j in range(len(x[i])):
        dotProduct = dotProduct + float(x[i])*y[i]
        #falta la dimension columna a la matriz x, y cambiar la i por y
    return dotProduct


def transpose(x):
    y = [[0 for i in range(len(x))] for j in range(len(x[0]))]
    for i in range(len(x[0])):
        for j in range(len(x)):
            y[i][j] = x[j][i]
    return y

random.seed(1)
numRandom0 = 2*random.random() -1
numRandom1 = 2*random.random() -1
numRandom2 = 2*random.random() -1
inputMatrixValued = [[0,0,1],[0,1,1],[1,0,1],[1,1,1]]
outputMatrix = [[0],[0],[1],[1]]
weighsArray = [numRandom0,numRandom1,numRandom2]
#weighsMatrix = [[-0.16595599],[0.44064899],[-0.99977125]]
l1 = [0 for t in range(len(outputMatrix))]
for i in range(10000):#change to 10000
    l0 = inputMatrixValued
    trainingSet = 0
    for trainingSet in range(len(l0)):
        l1[trainingSet] = sigmoidalFunction(dotProduct(l0[trainingSet],weighsArray),False)
        l1_error = []
        l1_delta = []
        for j in range(len(outputMatrix)):
            l1_error.append(outputMatrix[trainingSet][0] - l1[trainingSet])
            l1_delta.append(l1_error[j] * sigmoidalFunction(l1[trainingSet],True))

        for k in range(len(weighsArray)):
            weighsArray[k] += dotProduct(inputMatrixValued[trainingSet],l1_delta)
    print(weighsArray)


