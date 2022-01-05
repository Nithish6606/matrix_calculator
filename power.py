import numpy as np
def power():
  print("Power of a matrix:")
  #Enter rows and columns
  row=int(input("Enter number of rows:"))
  column=int(input("Enter number of columns:"))
  if row==column:
    print("Enter the elements of  Matrix:")
    matrix_a= [[int(input()) for i in range(column)] for i in range(row)]
    print("Matrix is: ")
    for n in matrix_a:
      print(n)
    matrix_a=np.array(matrix_a)
    n=int(input("Enter power of a matrix:"))
    powe = np.linalg.matrix_power(matrix_a,n) 
    print(powe)
  else:
    print("Please give square matrix")
 