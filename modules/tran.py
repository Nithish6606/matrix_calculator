import numpy as np
def trans()->None:
  print("Transpose of matrix:")
  #Enter rows and columns
  row:int=int(input("Enter number of rows:"))
  column:int=int(input("Enter number of columns:"))
  print("Enter the elements of  Matrix:")
  matrix_a:list= [[int(input()) for i in range(column)] for i in range(row)]
  print("Matrix is: ")
  for n in matrix_a:
    print(n)
  matrix_a:list=np.array(matrix_a)
  print("Transpose of matrix is:")
  tran:list=matrix_a.transpose()
  print(tran)

if __name__ == "__main__":
  trans()
  