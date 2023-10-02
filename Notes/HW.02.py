is_next = True
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
    result = "True"
else:
    is_next = False
    result = "False"
print(result)


is_active = input("Is the user active? ")
is_active = True or False
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")
is_permission = True or False

access = is_active and is_permission
is_admin = True
access = True



work_experience = int(input("Enter your full work experience in years: "))

if work_experience > 1 and work_experience <= 5:
    developer_type = "Middle"
elif work_experience <= 1 :
    developer_type = "Junior"
else:
    developer_type = "Senior"



num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 1:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"



import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)




num = int(input("Enter an integer number: "))

is_even = True if num % 2 == 0 else False



num = int(input("Enter the integer (0 to 100): "))
sum = 0

i = 0
while i <= num:
    print(i)
    sum = sum + i
    print(sum)
    i = i + 1


message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."

search = "r"
result = 0

for letter in message:
    if letter == "r":
        result = result + 1
        print(result)




first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = first if first < second else second

while first % gcd or second % gcd:
     gcd -= 1



sum = 0

while True:
    num = int(input("Podaj liczbę całkowitą (0 aby zakończyć): "))
    
    if num == 0:
        break
    
    for i in range(num + 1):
        sum += i

print("Suma wprowadzonych liczb to:", sum)



sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        sum = sum + i



sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        if i % 2 == 0:          
            sum = sum + i



message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch.isalpha():  # Sprawdź, czy znak jest literą
        if ch.isupper():
            base = ord('A')
        else:
            base = ord('a')
        encoded_char = chr(((ord(ch) - base + offset) % 26) + base)
    else:
        encoded_char = ch   
    encoded_message += encoded_char
print("Encoded message:", encoded_message)



pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
        print('Divide by zero completed!')



result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number == True:
        try:
            operand = float(input('Wprowadź liczbę: '))
            wait_for_number = False
            
            if operator != None:
                
                if operator == '+':
                    result = result + operand
                    print(result)
                elif operator == '-':
                    result = result - operand
                    print(result)
                elif operator == '/':
                    result = result / operand
                    print(result)
                elif operator == '*':
                    result = result * operand
            else:
                result = operand       

        except ValueError:
            print('Musi być podana liczba')
            continue
    
    elif wait_for_number == False:
        
        operator = input('Wprowadź znak działania: ')

        if operator == '=':
            if result == None:
                print(operand)
                break
            else:
                print(result)
                break

        elif operator not in ['+',"-","/",'*']:
            print('Nie właściwy operator działania, wpisz jeszcze raz: ')
            continue

        else:
        
            wait_for_number = True
            result = result

