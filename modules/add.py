import numpy as np
def get_matrix_input(rows, columns)->list:
  matrix:list = [[int(input()) for _ in range(columns)] for _ in range(rows)]
  return matrix
def addition()->None:
  # Enter rows and columns
  print("Addition of matrices:")
  rows:int = int(input("Enter the number of rows: "))
  columns:int = int(input("Enter the number of columns: "))

  # First matrix input
  print("Enter the elements of the first matrix:")
  matrix_a:list = get_matrix_input(rows, columns)
  print("First matrix is:")
  for row in matrix_a:
    print(row)

  # Second matrix input
  print("Enter the elements of the second matrix:")
  matrix_b:list = get_matrix_input(rows, columns)
  print("Second matrix is:")
  for row in matrix_b:
    print(row)

  # Result matrix
  result:list =np.zeros((rows,columns))
  #Addition of matrices
  result:list=np.add(matrix_a,matrix_b)
  # Print the sum of matrices
  print("Sum of the two matrices:")
  for row in result:
    print(row)

if __name__ == "__main__":
  print(addition())
