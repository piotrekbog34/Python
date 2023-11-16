
def real_len(text):
    special_chars = ['\n', '\f', '\r', '\t', '\v']
    filtered_text = ''.join(char for char in text if char not in special_chars)
    return len(filtered_text)

#######################################

articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key, letter_case=False):
    found_articles = []

    for article in articles_dict:
        title = article["title"]
        author = article["author"]

        if not letter_case:
            key = key.lower()
            title = title.lower()
            author = author.lower()

        if key in title or key in author:
            found_articles.append({
                "author": article["author"],
                "title": article["title"],
                "year": article["year"]
            })

    return found_articles

#######################################

def sanitize_phone_number(phone):
    cleaned_phone = ''.join(char for char in phone if char.isdigit())
    return cleaned_phone

#######################################

def is_check_name(fullname, first_name):
    return fullname.startswith(first_name)

#######################################

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

def get_phone_numbers_for_countries(list_phones):
    country_numbers = {
        "JP": [],
        "SG": [],
        "TW": [],
        "UA": [],
    }


    for phone in list_phones:
        sanitized_phone = sanitize_phone_number(phone)

        if sanitized_phone.startswith("81"):
            country_numbers["JP"].append(sanitized_phone)
        elif sanitized_phone.startswith("65"):
            country_numbers["SG"].append(sanitized_phone)
        elif sanitized_phone.startswith("886"):
            country_numbers["TW"].append(sanitized_phone)
        else:
            country_numbers["UA"].append(sanitized_phone)

    return country_numbers

#######################################

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for a, b in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(a)] = b
    TRANS[ord(a.upper())] = b.upper()

def translate(name):
    return name.translate(TRANS)

#######################################

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    formatted_list = []

    for i, (name, grade) in enumerate(students.items(), start=1):
        formatted_grade = f"{grades[grade]}"

        formatted_list.append(
            f"{i:4}|{name:10}|{grade:^5}|{formatted_grade:^5}"
        )

    return formatted_list

#######################################

def formatted_numbers():
    formatted_list = []
    header = "| decimal | hex | binary |"
    separator = "+----------+-----------+----------+"
    formatted_list.extend([separator, header, separator])

    for i in range(16):
        decimal = f"{i:<10}"
        hex_num = f"{hex(i)[2:]:^10}"
        binary = f"{bin(i)[2:]:>10}"

        row = f"|{decimal}|{hex_num}|{binary}|"
        formatted_list.append(row)

    formatted_list.append(separator)

    return formatted_list

#######################################

def formatted_numbers():
    formatted_list = []
    header = "| decimal  |   hex    |  binary  |"
    formatted_list.extend([header])

    for i in range(16):
        decimal = f"{i:<10}"
        hex_num = f"{i: ^10x}"
        binary = f"{bin(i)[2:]:>10}"

        row = f"|{decimal}|{hex_num}|{binary}|"
        formatted_list.append(row)

    return formatted_list

#######################################

import re

def find_word(text, word):
    result = {}
    search_result = re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)

    if search_result:
        result['result'] = True
        result['first_index'] = search_result.start()
        result['last_index'] = search_result.end() - 1
        result['search_string'] = search_result.group()
        result['string'] = text
    else:
        result['result'] = False
        result['first_index'] = None
        result['last_index'] = None
        result['search_string'] = word
        result['string'] = text

    return result

import re

def find_word(text, word):
    result = {}
    search_result = re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)

    if search_result:
        result['result'] = True
        result['first_index'] = search_result.start()
        result['last_index'] = search_result.end()
        result['search_string'] = search_result.group()
        result['string'] = text
    else:
        result['result'] = False
        result['first_index'] = None
        result['last_index'] = None
        result['search_string'] = word
        result['string'] = text

    return result




import re

def find_word(text, word):
    result = {}
    search_result = re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)

    if search_result:
        result['result'] = True
        result['first_index'] = search_result.start()
        result['last_index'] = search_result.end() - 1
        result['search_string'] = search_result.group()
        result['string'] = text
    else:
        result['result'] = False
        result['first_index'] = None
        result['last_index'] = None
        result['search_string'] = word
        result['string'] = text

    return result

def find_word(text, word):
    result = {}
    search_result = text.find(word)
    
    result['result'] = search_result != -1
    result['first_index'] = search_result if search_result != -1 else None
    result['last_index'] = search_result + len(word) - 1 if search_result != -1 else None
    result['search_string'] = word
    result['string'] = text
    
    return result