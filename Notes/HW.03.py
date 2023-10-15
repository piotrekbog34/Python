def greeting():
    print('Hello world!')
print(greeting)


def invite_to_event(username):
   return f"Dear {username}, we have the honour to invite you to our event"
print(invite_to_event("Vasya"))



base_rate = 40
price_per_km = 10
total_trip = 0

def calculate_trip_price(distance_km):
    global total_trip
    total_price = base_rate + (price_per_km * distance_km)
    total_trip += 1

    return total_price 



def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)

    apply_discount()
    return price


def get_fullname(first_name, last_name, middle_name=None):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}" 



def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        spaces = (length - len(string)) // 2
        formatted_string = ' ' * spaces + string
        return formatted_string



def first(size, *args):
    return size + len(args)

def second(size, **kwargs):
    return size + len(kwargs)   



def cost_delivery(quantity, *args, discount=0):
    delivery_cost = 5

    if quantity > 1:
        delivery_cost += (quantity - 1) * 2

    if 0 <= discount <= 1:
        delivery_cost *= (1 - discount)

    return delivery_cost



def cost_delivery(quantity, *_, discount=0):
    """Funkcja zwraca całkowitą kwotę dostawy.

    Pierwszym parametrem jest liczba pozycji w zamówieniu. 
    Parametr rabatu discount, przesyłany tylko za pomocą klucza, domyślnie ma 
    wartość 0."""
   
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result




def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def number_of_groups(n, k):
    if n < k:
        return 0

    n_factorial = factorial(n)
    nk_factorial = factorial(n - k)
    k_factorial = factorial(k)

    wynik = n_factorial // (nk_factorial * k_factorial)
    return wynik



def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n -2)

























