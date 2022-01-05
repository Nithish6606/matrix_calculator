import numpy as np
def multiplication():
  print("Multiplication of matrix:")
  #Enter rows and columns
  row=int(input("Enter number of rows:"))
  column=int(input("Enter number of columns:"))


  #First matrix code
  print("Enter the elements of First Matrix:")
  matrix_a= [[int(input()) for i in range(column)] for i in range(row)]
  print("First Matrix is: ")
  for n in matrix_a:
    print(n)
    
  matrix_a=np.array(matrix_a)
    
  #second matrix code
  print("Enter the elements of second Matrix:")
  matrix_b= [[int(input()) for i in range(column)] for i in range(row)]
  print("second Matrix is: ")
  for n in matrix_b:
    print(n)
    
  matrix_b=np.array(matrix_b)

  #result format   
  result=matrix_a.dot(matrix_b)

  #multiplication of matrix
  print("Multiplication of matrix is:")
  for r in result:
    print(r)
