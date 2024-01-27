# Un array de una dimension es conocido como Vector

vector1 = [5, 2, 6]
vector2 = [3, 2, 1]
vector3 = [4, 4, 4]

vectorA = [0,0,0]
vectorB = [0,0,0]

valorA = 3

for i in range(len(vector1)):
    vectorA[i] = vector3[i] - vector2[i]
    vectorB[i] = vector3[i] + vector2[i]
    valorA  = vector3[i] * vector2[i] + valorA

print('vectorA: ', vectorA)
print('vectorB: ', vectorB)
print('valorA: ', valorA)

