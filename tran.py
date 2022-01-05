import numpy as np
def trans():
  print("Transpose of matrix:")
  #Enter rows and columns
  row=int(input("Enter number of rows:"))
  column=int(input("Enter number of columns:"))
  print("Enter the elements of  Matrix:")
  matrix_a= [[int(input()) for i in range(column)] for i in range(row)]
  print("Matrix is: ")
  for n in matrix_a:
    print(n)
  matrix_a=np.array(matrix_a)
  print("Transpose of matrix is:")
  tran=matrix_a.transpose()
  print(tran)
  