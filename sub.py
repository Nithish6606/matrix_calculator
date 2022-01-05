def subtraction():
  print("Subtraction of matrix:")
  #Enter rows and columns
  row=int(input("Enter number of rows:"))
  column=int(input("Enter number of columns:"))


  #First matrix code
  print("Enter the elements of First Matrix:")
  matrix_a= [[int(input()) for i in range(column)] for i in range(row)]
  print("First Matrix is: ")
  for n in matrix_a:
    print(n)
    
  #second matrix code
  print("Enter the elements of second Matrix:")
  matrix_b= [[int(input()) for i in range(column)] for i in range(row)]
  print("second Matrix is: ")
  for n in matrix_b:
    print(n)

  #result format   
  result= [[0 for i in range(column)] for i in range(row)]

  #subtraction of matrix code
  for i in range(row):
    for j in range(column):
      result[i][j]=matrix_a[i][j]-matrix_b[i][j]
    
  #subtraction of matrixes   
  print("Subtraction of two matrixes:")   
  for r in result:
    print(r)