import random
secret_number=random.randint(1,100)
print("Welcome to Number guessing Game...!!!!")
print("I have selected a number between 1 and 100...")
attempts=0
while True:
  try:
    Guess= int(input("Enter your guessing Number: "))
    attempts+=1
    if Guess<secret_number:
      print("It's Very Low... Try Again....!!!!!")
    elif Guess >secret_number:
      print("It's Very High.... Try Again....!!!!")
    else:
      print(f"Congratulations You Guessed Number in {attempts} attempts ")
      break
  except ValueError:
    print("1Enter numbers only")
  except KeyboardInterrupt:
    print("\n Game stopped by user.")
