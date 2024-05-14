import numpy as np
def trace_matrix()->None:
  print("Trace of matrix:")
  row:int=int(input("Enter number of rows:"))
  column:int=int(input("Enter number of columns:"))
  if row==column:
    print("Enter the elements of  Matrix:")
    matrix_a:list= [[int(input()) for i in range(column)] for i in range(row)]
    print("Entered Matrix is: ")
    for n in matrix_a:
      print(n)
    matrix_a:list=np.array(matrix_a)
    print("Trace of matrix is:",matrix_a.trace())
  else:
    print("Please give square matrix")
 
if __name__ == "__main__":
  trace_matrix()
  