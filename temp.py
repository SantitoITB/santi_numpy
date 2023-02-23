

import numpy as np

#        [ 3 1 2 ]   
#    A = [ 4 1 3 ] 
#        [ 2 0 1 ] 
# creame la siguiente matriz
A = np.array([[3, 1, 2], [4, 1, 3], [2, 0, 1]])
#         [ 2 0 3 ]   
#    B = [ 1 1 1 ] 
#        [ 0 2 4 ] 
# creame la siguiente matriz
B = np.array([[2, 0, 3], [1, 1, 1], [0, 2, 4]])

# Realitza la multiplicació matricial de AxB i BxA. Són iguals? 
# Realiza la multiplicación matricial de AxB y BxA. Son iguales?
print(A.dot(B))
print(B.dot(A))

# Realitza la multiplicació matricial de AxA i BxB. Són iguals?
# Realiza la multiplicación matricial de AxA y BxB. Son iguales?
print(A.dot(A))
print(B.dot(B))

# Realitza la multiplicació de la matriu A x 2
# Realiza la multiplicación de la matriz A x 2
print(A*2)


# Quan és la multiplicació escalar d'AxB? i de BxA? Són iguals?
# Cuando es la multiplicación escalar de AxB? y de BxA? Son iguales?
print(np.sum(A*B))
print(np.sum(B*A))

# 5- Usant la matriu A de l'exercici anterior, calcula:
# A^3

# 5- Usando la matriz A del ejercicio anterior, calcula:
# A^3
print(A.dot(A.dot(A)))

# El determinant d'A
# El determinante de A
print(np.linalg.det(A))

# Resol l'equació Ax = y, essent *y* l'array [3,2,5]
# Resuelve la ecuación Ax = y, siendo *y* el array [3,2,5]
y = np.array([3, 2, 5])
print(np.linalg.solve(A, y))















