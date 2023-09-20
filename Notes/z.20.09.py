#ciąg fibonacciego

# F[0] = 0
# F[1] = 1
# F[N] = F[N - 2] + F[N - 1]

# Wersja interacyjna ciągu F 0.1




def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range (n):     # _ dowolny znak by uzupełnic funkcje for
        a, b = b, a + b
    return a

# Wersja interacyjna ciągu F 0.2

def fib(n):
    if  n == 0 or n == 1:
        return n
    a, b = 0, 1
    for _ in range (n):
         a, b = b, a + b
    return a

# Wersja interacyjna ciągu F 0.3

def fib(n):
    a, b = 0, 1
    for _ in range (n):
         a, b = b, a + b
    return a

print(fib(5))


# Wersja rekurencyjna ciągu F
from functools import lru_cache
@lru_cache # przyśpiesz dzialania rekurencyjne

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n -2)

print(fib(20))




def divide(a, b):
    return a / b

print(
    divide(a=1, b=2)
)


def foo(a, b, *arg, **kwargs):
    print(a)

# Tuple/krotka

# x = (1, 2, 3)

# print(x[1]) wyprintuje drugi wyraz z krotki 
# [0] = 1 z x
# [1] = 2 z x
# [2] = 3 z x (ostatni wyraz z krotki)


if __name__ == "__name__":
    print(f"__name__ = {__name__} in 1.py") # 1.py nazwa modułu




