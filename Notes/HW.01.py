name ='Danila'
age = 26


rate = 1.68
value = 14
payment = rate * value


rate = 1.68
value_day = 14
value_night = 4
payment = value_day * rate + (rate / 2 )*value_night


rate = 1.68
value_day = 358
value_night = 103
#Payment for electricity for the current month
payment = rate * value_day + rate / 2 * value_night


first_name = "Piotr"
last_name = "Bogusz"
Fullname_string = first_name + last_name


first_name = "Piotr"
last_name = "Bogusz"
full_name = first_name + ' ' + last_name


first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
message = f"Dear {first_name}, we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at {full_name}. We are looking forward to seeing you!"


length = 2.75
width = 1.75
area = length * width
show = f"With width {width} and length {length} of the room, its area is equal to {area}"


a = "complex = -2 + 3j"
b = "complex = 4 + 2,1j"
result = a + b


import math
a = -2
b = 7
c = -6
D =b**2 - 4*a*c
x1 =(-b + D**0.5)/(2*a)
x2 =(-b - D**0.5)/(2*a)


is_active = True
is_delete = False
is_active > is_delete #prawda


name = "Piotr"
age = 26
is_active = True
subscription = None

length = "2.75"
width = "1.75"
area = float(length)*float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"


import math
RADIUS = 6371.01
lat1 = math.radians(50.45)
lon1 = math.radians(30.523)
lat2 = math.radians(51.5072)
lon2 = math.radians(-0.1275)
distance = RADIUS * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))


name = input("Your name? ")
email = input("twój email")
age = int(input("wiek"))
height = float(input("wzrost"))
is_active = True


length = float(input("Wysokość"))
width = float(input("Szerokość"))
area = length * width
