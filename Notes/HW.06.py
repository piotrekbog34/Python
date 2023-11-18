def total_salary(path):
    try:
        file = open(path, 'r')

        total_salary = 0.0

        line = file.readline()
        while line:
            parts = line.strip().split(',')
            if len(parts) == 2:
                total_salary += float(parts[1])

            line = file.readline()

        return total_salary

    except FileNotFoundError:
        print(f"Plik o ścieżce {path} nie został znaleziony.")
        return 0.0
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return 0.0
    finally:
        # Zamknij plik
        if file:
            file.close()

#######################################

def write_employees_to_file(employee_list, path):
    file = open(path, "w")
    
    try:
         for department in employee_list:
             for employee in department:
                 file.write(employee + "\n")
    finally:
        file.close()

#######################################

def read_employees_from_file(path):
    file = open(path, "r")
    try:
        employees = [line.strip() for line in file]
    finally:
        file.close()  
    return employees

#######################################

def add_employee_to_file(record, path):
    file = open(path, "a")
    
    try:
        file.write(record + "\n")
    finally:
        file.close()

#######################################

def get_cats_info(path):
    cats_info_list = []

    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split(',')
      
            if len(parts) == 3:
                cat_info = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                }
                cats_info_list.append(cat_info)

    return cats_info_list

#######################################

def get_recipe(path, search_id):
    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split(',')
            
            if len(parts) >= 2 and parts[0] == search_id:
                recipe_info = {
                    "id": parts[0],
                    "name": parts[1],
                    "ingredients": parts[2:]
                }
                return recipe_info
    
    return None

#######################################

def sanitize_file(source, output):
    with open(source, "r") as source_file, open(output, "w") as output_file:
        for line in source_file:
            sanitized_line = ''.join(char for char in line if not char.isdigit())
            output_file.write(sanitized_line)

#######################################

def save_applicant_data(source, output):
    with open(output, "w") as output_file:
        for applicant in source:
            data_line = f"{applicant['name']},{applicant['specialty']},{applicant['math']},{applicant['lang']},{applicant['eng']}\n"
            
            output_file.write(data_line)

#######################################

def is_equal_string(utf8_string, utf16_string):
    try:
        unicode_utf8 = utf8_string.decode('utf-8')
        unicode_utf16 = utf16_string.decode('utf-16')

        return unicode_utf8 == unicode_utf16
    except UnicodeDecodeError:
        return False

#######################################

def save_credentials_users(path, users_info):
    with open(path, "wb") as file:
        for username, password in users_info.items():
            credentials_line = f"{username}:{password}\n"          
            file.write(credentials_line.encode('utf-8'))

#######################################

def save_credentials_users(path, users_info):
    with open(path, "wb") as file:
        for username, password in users_info.items():
            credentials_line = f"{username}:{password}\n"           
            file.write(credentials_line.encode('utf-8'))

#######################################


def get_credentials_users(path):
    credentials_list = []
    with open(path, "rb") as file:
        for line in file:
            decoded_line = line.decode('utf-8').strip()
            credentials_list.append(decoded_line)
    return credentials_list

#######################################

import base64

def encode_data_to_base64(data):
    encoded_list = []
    for item in data:
        username, password = item.split(':')       
        encoded_pair = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')
        encoded_list.append(encoded_pair)
    
    return encoded_list

#######################################

import shutil

def create_backup(path, file_name, employee_residence):
    file_path = f"{path}/{file_name}"

    with open(file_path, "wb") as file:
        for name, country in employee_residence.items():
            line = f"{name} {country}\n".encode('utf-8')
            file.write(line)

    backup_folder = shutil.make_archive('backup_folder', 'zip', path)

    return backup_folder

#######################################

import shutil

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)   












