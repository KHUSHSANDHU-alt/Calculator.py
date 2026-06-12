num1 = float(input("enter num:")
num2 = float(input("enter num:") 
print("choose option:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("enter option")

if choice =="1":
   print("Result",num1+num2)
elif choice =="2":
   print("Result",num1-num2)
elif choice =="3":
   print("Result" , num1*num2)
elif choice == "4":
   if num2 !=0:
     print("Cannot divide by 0")
   else:
     print("Result",num1/num2)
else:
   print("Invalid choice")
  
          
