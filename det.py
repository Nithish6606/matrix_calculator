import numpy as np
def determinent():
  print("Determinent of matrix:")
  #Enter rows and columns
  row=int(input("Enter number of rows:"))
  column=int(input("Enter number of columns:"))
  if row==column:
    print("Enter the elements of  Matrix:")
    matrix_a= [[int(input()) for i in range(column)] for i in range(row)]
    print("Entered Matrix is: ")
    for n in matrix_a:
      print(n)
  #matrix_a=np.array(matrix_a)
    det = np.linalg.det(matrix_a) 
    print("Determinent of a matrix is:",int(det))
  else:
    print("Please give square matrix")
 
