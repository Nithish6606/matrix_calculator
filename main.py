from modules.add import addition
from modules.sub import subtraction
from modules.mul import multiplication
from modules.det import determinent
from modules.inv import inverse
from modules.tran import trans
from modules.tra import trace_matrix
from modules.rank import rank_matrix
from modules.power import power

print("1.Addition of a matrix\n2.Subtraction of matrix\n3.Multiplication of matrix\n4.Determinant of matrix\n5.Inverse of a matrix\n6.Transpose of a matrix\n7.Trace of a matrix\n8.Rank of matrix\n9.Power of a matrix") 
choice:int = int(input("Enter choice:"))

match choice:
  case 1:
    print(addition())
  case 2:
    print(subtraction())
  
  case 3:
    print(multiplication())
  
  case 4:
    print(determinent())
  
  case 5:
    print(inverse())
  
  case 6:
    print(trans())
 
  case 7:
    print(trace_matrix())
  
  case 8:
    print(rank_matrix())
  
  case 9:
    print(power())
  
  case _:
    print("Please select from choice")
