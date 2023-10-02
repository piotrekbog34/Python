
x = 42
if x % 2 == 0: # jeżeli reszta z dzielenia X przez 2 wyniesie 0, liczba jest parzysta
    print("This number is even")
else:
    print("This number is odd")


weight = float(input("Input your weight: "))
height = float(input("Input your height: "))

bmi = weight / height ** 2
print(f"BMI: {bmi:.2f}") # f str ing , w nawiasie klamrowy dajemy zmienna, .2f oznacza float i 2 znaki po przecinku

if bmi < 18.4:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal")
else:
    print("Overweight")



x = 15

result = ""
while x != 0:
    bit = str(x % 2)
    x = x // 2
    result = bit + result

print(result)



items = (1, 2, 3, 4, 5)

x, y, *_ = items
print(x, y)



x = 65535

result = ""
while x != 0:
    rem = str(x % 2)
    x //= 2  # x = x // 2
    result = rem + result

print(result)



from math import log2, floor

x = 11

bits = floor(log2(x)) + 1
result = ""
for _ in range(bits):
    rem = str(x % 2)
    x //= 2  # x = x // 2
    result = rem + result

print(result)



print("This program will conver decimal to bin")

while True:
    x = int(input("Input non-negative integer: "))

    result = ""
    while x != 0:
        rem = str(x % 2)
        x //= 2  # x = x // 2
        result = rem + result

    print(f"Binary value: {result}")

    answer = input("Do you want to try again? Y/N ")
    while answer not in ["Y", "N"]:
        print(f"Unrecognized command '{answer}', use Y/N")
        answer = input("Do you want to try again? Y/N ")
    
    if answer == "N":
        break



print("This program will conver decimal to bin")

while True:
    x = int(input("Input non-negative integer: "))

    result = bin(x)
    print(f"Binary value: {result}")

    answer = input("Do you want to try again? Y/N ")
    while answer not in ["Y", "N"]:
        print(f"Unrecognized command '{answer}', use Y/N")
        answer = input("Do you want to try again? Y/N ")
    
    if answer == "N":
        break



print("This program will conver decimal to bin")

while True:
    try:
        x = int(input("Input non-negative integer: "))
    except ValueError:
        print("Can't convert value to integer")
        print("Please try again...")
        continue
    except KeyboardInterrupt:
        print("\nExiting program...")
        break

    result = bin(x)
    print(f"Binary value: {result}")

    answer = input("Do you want to try again? Y/N ")
    while answer not in ["Y", "N", "n", "y"]:
        print(f"Unrecognized command '{answer}', use Y/N")
        answer = input("Do you want to try again? Y/N ")
    
    if answer == "N":
        break




print("This program will conver decimal to bin")

while True:
    try:
        x = int(input("Input non-negative integer: "))
    except ValueError as error:
        print(error)
        print("Please try again...")
        continue
    except Exception:
        print("Unknown error!!!")
        print("Exiting program...")
        break
    except KeyboardInterrupt:
        print("\nExiting program...")
        break

    result = bin(x)
    print(f"Binary value: {result}")

    answer = input("Do you want to try again? Y/N ")
    while answer not in ["Y", "N", "n", "y"]:
        print(f"Unrecognized command '{answer}', use Y/N")
        answer = input("Do you want to try again? Y/N ")
    
    if answer in ["N", "n"]:
        break