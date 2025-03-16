Num1 = float (input("Enter the first number:"))
Num2 = float(input ("Enter the second number:"))
operation = input ("Enter an operation (+ , -, /,*):")

if operation == "+":
  print(Num1+Num2)
elif operation == "-":
  print(Num1, "-", Num2, "=", Num1-Num2)
elif operation == "*":
  print(Num1, "*", Num2, "=", Num1*Num2)
elif operation == "/":
  if Num2 != 0: 
     print(Num1, "/", Num2, "=", Num1/Num2)
  else:
    print("Error: Division by zero is not allowed.")
  print(Num1/Num2)
else:
  print("Invalid input")