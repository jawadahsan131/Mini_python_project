count = 0
Flag = True
while Flag:
    a = int(input("Enter a number: "))
    if a % 3 == 0 and a % 5 == 0:
        print("Fizz Buzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print("Game Over")
        print(count)
        print(f"Your highest score = {count}")
        break
    count += 1
