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







