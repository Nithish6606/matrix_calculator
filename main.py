print("1.Addition of a matrix\n2.Subtraction of matrix\n3.Multiplication of matrix\n4.Determinant of matrix\n5.Inverse of a matrix\n6.Transpose of a matrix\n7.Trace of a matrix\n8.Rank of matrix\n9.Power of a matrix") 
choice=int(input("Enter choice:"))
if choice==1:
  from add import addition
  print(addition())
  
elif choice==2:
  from sub import subtraction
  print(subtraction())
  
elif choice==3:
  from mul import multiplication
  print(multiplication())
  
elif choice==4:
  from det import determinent
  print(determinent())
  
elif choice==5:
  from inv import inverse
  print(inverse())
  
elif choice==6:
  from tran import trans
  print(trans())
 
elif choice==7:
  from tra import trace_matrix
  print(trace_matrix())
  
elif choice==8:
  from rank import rank_matrix
  print(rank_matrix())
  
elif choice==9:
  from power import power
  print(power())
  
else:
  print("Please select from choice")
