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
















