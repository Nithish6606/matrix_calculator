import numpy as np
def multiplication()->None:
  print("Multiplication of matrix:")
  #Enter rows and columns
  row:int=int(input("Enter number of rows:"))
  column:int=int(input("Enter number of columns:"))


  #First matrix code
  print("Enter the elements of First Matrix:")
  matrix_a:list= [[int(input()) for i in range(column)] for i in range(row)]
  print("First Matrix is: ")
  for n in matrix_a:
    print(n)
    
  matrix_a:list=np.array(matrix_a)
    
  #second matrix code
  print("Enter the elements of second Matrix:")
  matrix_b:list= [[int(input()) for i in range(column)] for i in range(row)]
  print("second Matrix is: ")
  for n in matrix_b:
    print(n)
    
  matrix_b:list=np.array(matrix_b)

  #result format   
  result:list=matrix_a.dot(matrix_b)

  #multiplication of matrix
  print("Multiplication of matrix is:")
  for r in result:
    print(r)


if __name__ == "__main__":
  multiplication()
