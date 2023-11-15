def amount_payment(payment):
    total_payment = 0

    for payments in payment:
        if payments > 0:
            total_payment += payments

    return total_payment

#######################################      

def prepare_data(data):
    total_data = 0



def prepare_data(data):
    if len(data) < 2:
 
        return data

    data.remove(max(data))
    data.remove(min(data))
    data.sort()
    return data

#######################################

def format_ingredients(items):
    if not items:
        return ""
    elif len(items) == 1:
        return items[0]
    else:
        formatted_items = ", ".join(items[:-1])
        formatted_items = f"{formatted_items} and {items[-1]}"
        return formatted_items

#######################################

ects_to_grades = {
    "F": 1,
    "FX": 2,
    "E": 3,
    "D": 3,
    "C": 4,
    "B": 5,
    "A": 5,
}

ects_to_descriptions = {
    "F": "Unsatisfactorily",
    "FX": "Unsatisfactorily",
    "E": "Enough",
    "D": "Satisfactorily",
    "C": "Good",
    "B": "Very good",
    "A": "Perfectly",
}

def get_grade(key):
    return ects_to_grades.get(key, None)

def get_description(key):
    return ects_to_descriptions.get(key, None)

#######################################

def lookup_key(dictionary, value):
    keys = []
    for key, val in dictionary.items():
        if val == value:
            keys.append(key)
    return keys

#######################################

def split_list(grade):
    if not grade:
        return ([], [])
    
    average = sum(grade) / len(grade)
    lower_or_equal_avg = [x for x in grade if x <= average]
    greater_than_avg = [x for x in grade if x > average]
    
    return (lower_or_equal_avg, greater_than_avg)

#######################################

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
coordinates = [0, 1, 3, 2, 0]

def calculate_distance(coordinates):
    if not coordinates or len(coordinates) == 1:
        return 0

    total_distance = 0
    for i in range(len(coordinates) - 1):
        start_point = coordinates[i]
        end_point = coordinates[i + 1]


        if (start_point, end_point) in points:
            total_distance += points[(start_point, end_point)]
        elif (end_point, start_point) in points:
            total_distance += points[(end_point, start_point)]
        else:
            raise ValueError(f"Brak danych w słowniku points dla odległości między punktami {start_point} i {end_point}")

    return total_distance

#######################################

terra = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
power = 1

def game(terra, power):
    for level in terra:
        for enemy_energy in level:
            if enemy_energy <= power:
                power += enemy_energy
            else:
                break
    return power

#######################################

def is_valid_pin_codes(pin_list):
    if not pin_list:
        return False

    unique_pins = set()

    for pin in pin_list:
        if len(pin) != 4:
            return False

        if not pin.isdigit():
            return False

        unique_pins.add(pin)

    return len(unique_pins) == len(pin_list)

#######################################

from random import randint

def get_random_password():
    password_length = 8
    password_characters = "()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    random_password = [password_characters[randint(0, len(password_characters)-1)] for _ in range(password_length)]

    return ''.join(random_password)

random_password = get_random_password()
print(random_password)

#######################################

def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit

password_to_check = "Abcd1234"
result = is_valid_password(password_to_check)

if result:
    print("Hasło jest silne i bezpieczne")
else:
    print("Hasło nie spełnia wymagań bezpieczeństwa")


#######################################

from random import randint

def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num

def get_password():
    max_attempts = 100
    attempts = 0

    while attempts < max_attempts:
        password_candidate = get_random_password()

        if is_valid_password(password_candidate):
            return password_candidate
        else:
            attempts += 1

    print("Nie udało się wygenerować hasła")
    return None

#######################################

from pathlib import Path

def parse_folder(path):
    files = []
    folders = []

    if path.is_dir():
        files = [item.name for item in path.iterdir() if item.is_file()]
        folders = [item.name for item in path.iterdir() if item.is_dir()]

    return files, folders

#######################################

import sys

def parse_args():
    result = ' '.join(sys.argv[1:])
    return result