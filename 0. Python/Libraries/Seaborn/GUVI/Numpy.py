import numpy as np
#X = np.array([1,2,3])
l = [1,2,3,4]
#X = np.array(l)
#X = np.array(l, float)
X = np.array([[1,2,3],[4,5,6]])
print(type(X))
print(X)


print(X.shape," is the dimention of the array") #prints the dimentions of the array
print(X[0,0],X[1,2]) # prints the elemnt from the forst row and first column, the second element prints 2nd row 3rd column
print(X[0,0:2]) # prints the zeroth row and the range from column starting from the initialisation 0 to the number of elemts you want to print.
print(X[0,:]) # print the first row

Y = np.zeros((4,5)) # 4 rows and 5 Column filed with zeros
print(Y)

Y = np.eye(4,4) # Identity matrix
print(Y)

Y = np.random.random((4,5))
print(Y)
Z = Y.T
print("Transpose of Y")
print(Z)

# To reshape the elements of a matrix into another configuration for example 4,5 matrix into 20,1
Z = Y.reshape(20,1)
print(Z)

A = np.arange(5)
print(A)
print(A, A+1)

A = np.random.random((2,3))
print(A)
print(" ")
print(A+1)

# to take only floor values
A = np.floor(np.random.random((2,3))*10)
print(A)
print(" ")
print(A+1)
print(" ")
u = [1,2,3]
v = [-1,0,1]

pl = np.inner (u,v)
print(pl)
print("")
pl2 = np.outer(u, v)
print(pl2)
print("")

A = np.ones((2,3))
#print(A)
B = np.ones((3,2))
#print(B)
print(np.dot(A,B))

print(A.sum())
