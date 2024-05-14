import numpy as np
def determinent()->None:
  print("Determinent of matrix:")
  #Enter rows and columns
  row:int=int(input("Enter number of rows:"))
  column:int=int(input("Enter number of columns:"))
  if row==column:
    print("Enter the elements of  Matrix:")
    matrix_a:list= [[int(input()) for i in range(column)] for i in range(row)]
    print("Entered Matrix is: ")
    for n in matrix_a:
      print(n)
    det:float = np.linalg.det(matrix_a) 
    print("Determinent of a matrix is:",int(det))
  else:
    print("Please give square matrix")

if __name__ == "__main__":
  determinent()
 
