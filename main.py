#To get Rectangle perimeter 
print("Press 1 or 2 otherwise it will not work")
UserChoice = input()

if UserChoice == 1:
  print("First number is width, Second is Length")

  W = 25
  L = 50

  print(W)
  print(L)
  print("What is the perimeter of the rectangle?")

  UserAnswer = input()
  RectanglePerimeter = W + W + L + L  

  if UserAnswer == RectanglePerimeter:
    print("Correct!")
  if UserAnswer > RectanglePerimeter or RectanglePerimeter > UserAnswer:
    print("Wrong!")

  print("RectanglePerimeter")

if UserChoice == 2:
  print("Width(Number Only!)")
  W = input()
  print("Length(Number Only)")
  L = input()
  print("What is the Perimeter of the rectangle?")
  UserAnswer = input()
  if UserAnswer == W + W + L + L:
    print("Correct!")
  if not UserAnswer == W + W + L + L:
    print("Wrong!")