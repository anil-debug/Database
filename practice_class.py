def get_number(prompt):
  """Gets a number from the user as a float."""
  while True:
    try:
      number = float(input(prompt))
      return number
    except ValueError:
      print("Invalid input. Please enter a number.")

def get_operation():
  """Gets the operation selection from the user."""
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Power")
  print("0. Exit")

  while True:
    choice = input("Enter choice(1/2/3/4/5/0): ")
    if choice in ('1', '2', '3', '4', '5', '0'):
      return int(choice)
    else:
      print("Invalid input. Please select a valid option (1-5 or 0 to exit).")

class Calculator:
  def __init__(self):
    pass

  def calculate(self):
    """Performs the selected operation on user-provided numbers."""
    operation = get_operation()
    if operation == 0:
      print("Exiting calculator.")
      return

    number1 = get_number("Enter first number: ")
    number2 = get_number("Enter second number: ")

    if operation == 1:
      result = number1 + number2
      print(f"{number1} + {number2} = {result}")
    elif operation == 2:
      result = number1 - number2
      print(f"{number1} - {number2} = {result}")
    elif operation == 3:
      result = number1 * number2
      print(f"{number1} * {number2} = {result}")
    elif operation == 4:
      if number2 == 0:
        print("Error: Cannot divide by zero.")
      else:
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")
    elif operation == 5:
      result = number1 ** number2
      print(f"{number1} ^ {number2} = {result}")

# Create a calculator object
calculator = Calculator()

# Keep calculating until the user exits
while True:
  calculator.calculate()
  print("-" * 20)