print("1.Addition of a matrix\n2.Subtraction of matrix\n3.Multiplication of matrix\n4.Determinant of matrix\n5.Inverse of a matrix\n6.Transpose of a matrix\n7.Trace of a matrix\n8.Rank of matrix\n9.Power of a matrix") 
choice=int(input("Enter choice:"))
if choice==1:
  from matrix.add import addition
  print(addition())
  
elif choice==2:
  from matrix.sub import subtraction
  print(subtraction())
  
elif choice==3:
  from matrix.mul import multiplication
  print(multiplication())
  
elif choice==4:
  from matrix.det import determinent
  print(determinent())
  
elif choice==5:
  from matrix.inv import inverse
  print(inverse())
  
elif choice==6:
  from matrix.tran import trans
  print(trans())
 
elif choice==7:
  from matrix.tra import trace_matrix
  print(trace_matrix())
  
elif choice==8:
  from matrix.rank import rank_matrix
  print(rank_matrix())
  
elif choice==9:
  from matrix.power import power
  print(power())
  
else:
  print("Please select from choice")