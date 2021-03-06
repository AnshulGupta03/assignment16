
#Q.1 - Create a numpy array with 10 elements of the shape(10,1) using np.random and find out the mean of the elements using basic numpy function
print("Question 1.")
import numpy as np

np_arr = np.random.randint(100, size=(10,1))
print(np_arr)
print("mean=",np.mean(np_arr))

print("\n\n")



#Q.2 - Create a numpy array with 20 elements of the shape(20,1) using np.random find the variance and standard deviation of the elements.
print("Question 2.")
import numpy as np

np_arr = np.random.randint(100, size=(20,1))
print(np_arr)

print("variance=",np.var(np_arr))
print("standard deviation=",np.std(np_arr))

print("\n\n")





#Q.3 - Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random. Print the matrix which is the matrix multiplication of A and B.
#The shape of the new matrix should be (10,25). Using basic numpy math functions only find the sum of all the elements of the new matrix.

print("Question 3.")
import numpy as np

a = np.random.randint(10, size=(10,20))
b = np.random.randint(10, size=(20,25))
c = np.matmul(a,b)
print("MATRIX A:\n",a)
print("MATRIX B:\n",b)
print("MATRIX C:\n",c)
print("Shape of matrix C:",np.shape(c))
print("Sum of elements of Matrix C:",np.sum(c))

print("\n\n")





#Q.4 - Create a numpy array A of shape(10,1).Using the basic operations of the numpy array generate an array of shape(10,1)
#such that each element is the following function applied on each element of A. 

#f(x)=1 / (1 + exp(-x)) 
#Apply this function to each element of A and print the new array holding the value the function returns
#Example:
#a=[a1,a2,a3]   
#n(new array to be printed )=[ f(a1), f(a2), f(a3)]

print("Question 3.")
import math
import numpy as np

a = np.random.randint(10, size=(10,1))

def f(x):
    return(1/(1+math.exp(-x)))

arr = np.array(list(map(f,a)))
print(arr)
print(math.exp(10))
