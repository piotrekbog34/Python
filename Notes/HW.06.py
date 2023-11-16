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












