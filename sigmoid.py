EULER = 2.7182818284590452353602874713527


def sigmoidalFunction(x,d):
    if d == True:
        return x*(1-x)
    return 1/(1+EULER**(-x))


def sigmoidDerivative(x):
    return sigmoidalFunction(x,False) * (1-sigmoidalFunction(x,False))


valor = 0

print(sigmoidalFunction(0.5,True))
print(sigmoidDerivative(0.5))
print(sigmoidalFunction(0.5,False))