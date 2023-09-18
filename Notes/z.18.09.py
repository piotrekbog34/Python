def say_hello(name):        # funkcja
    print(f"Hello {name}")  # argument funkcji

say_hello("Bob")    # wywolanie funkcji



def say_hello(name=None):        # funkcja None daje mozliwosc przypisania wartosci lub zostawienie pustej wartosci 
    if name is None:               # is nie równa sie ==
        print("Hello stranger")
    else:
        print(f"Hello {name}")

say_hello()
say_hello("Bob")    




def add(a, b):
    return a + b

x = add(2, 3)   # wywowalanie funkcji
print(x)        # wyswietlenie wyniku



def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

x = my_abs(10)
print(x)


import bisect # funkcjia bisect ctrl + click  do podgladu funkcji


def factorial(n):
    p = 1
    for i in range(n, n +1):
        p *= 1
    return p

x = factorial(7)
print = x



def my_sum(n):
    s = 0
    for i in range (1, n + 1):
        s += i
    return

x = my_sum(10)
print(x)


# n! = n * (n-1)!
# 0! - 1
# wzor rekurencyjny dla silni

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

x = factorial(10)
print = x


