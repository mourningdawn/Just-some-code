while True:
  print ("Options: ")
  print("Enter 'add' to add")
  print("Enter 'subtract' to subtract")
  print("Enter 'multiply' to multiply")
  print("Enter 'divide' to divide")
  print("Enter 'modulus' to modulus")
  print("Quit to end the program")
  uInput = input(":")
  if uInput == "quit":
    break
  elif uInput == "add":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = str(num1 + num2)
    print(result)
  elif uInput == "subtract":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = str(num1 - num2)
    print(result)
  elif uInput == "multiply":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number:"))
    result = str(num1 * num2)
    print(result)
  elif uInput == "divide":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = str(num1 / num2)
    print(result)
  elif uInput == "modulus":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number"))
    result = str(num1 % num2)
    print (result)
