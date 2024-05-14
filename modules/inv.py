import numpy as np
def inverse()->None:
  print("Inverse of a matrix:")
  #Enter rows and columns
  row:int=int(input("Enter number of rows:"))
  column:int=int(input("Enter number of columns:"))
  if row==column:
    print("Enter the elements of  Matrix:")
    matrix_a:list= [[int(input()) for i in range(column)] for i in range(row)]
    print("Matrix is: ")
    for n in matrix_a:
      print(n)
    matrix_a:list=np.array(matrix_a)
    print("Inverse of a matrix is:")
    inv:list = np.linalg.inv(matrix_a) 
    print(inv)
  else:
    print("Please give square matrix")

if __name__ == "__main__":
  inverse()
 
