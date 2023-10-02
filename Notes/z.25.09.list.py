
scores = [4, 5, 5, 4, 5, 5, 5, 5, 2]

# metoda, wywoluje funkcje po .
#operacja dla struktur danych
scores.append(42)   #dodaje wartość na koniec listy

scores.extend([100, 200, 300]) # rozszerza liste o kolekcje pod koniec listy

scores.insert(0, 100) # wsadza element do kolecji, na pozycje 0 (przed pierwszym elementem) , elemnt 100
# pierwsze miejsce na liście = 0, ostatni w kolekcji n to miejsce n- 1

for item in [100, 50, 200]: # metoda pentli
    scores.insert(0, item)

# operacja append działa szybko

scores.pop()    # usuwa ostatni element
# aby zobaczyc ostani element usunie trzeba zdefiniowac funckje np x i wyprintowac ją stringiem
x = scores.pop() 
print (scores)
print(f"x ={x} ")


scores.sort()   # sortuje rosnąco tylko liczby

scores.reverse()    # zamienia kolejnosc elementow

scores.clear()  # czyści liste z wszystkich elementów

scores.count()  # zlicza ile razy przekazany argument występuje na liście
x = scores.count(100)
print(f"x = {x}")   # pokazuje ile razy 100 wystąpiło na liście


# wersja 1.0
pos = scores.index(300, 0, 7)     # szuka elemntu na liscie i pokazuje jegho miejscie na liście, zaczyna szukac od miejsca 0 a konczy szukac na 7, staqrt i stop nie muszą byc podawane
print(f"pos = {pos}")

# wersja 2.0
start = 0
stop = 7

pos = scores.index(300, start, stop)
print(f"pos = {pos}")

len(scores) # funkcja len zwraca liczbe elementow w liście

scores.remove(90)   # usuwa element z listy

# usuwa wszystkie 30 z listy
# wersja 1.0
cnt = scores.count(30)
for _ in range(cnt):
    scores.remove(30)
print(scores)

# wersja 2.0
while 30 in scores:
    scores.remove(30)
print(scores)




students = [
    "Bob", "Sam", "Joe"
]

items = [
    42, 100, 300, students
]

items_copy = items.copy()

students.append("Justin")
print(students)
print(items)
print(items_copy)



scores = [4, 5, 5, 4, 5, 5, 5, 5, 2]
print(scores[4]) # printuje 5 element listy

n = len(scores)
print(scores[n - 1])    # printuje ostatni element listy

print(scores[-1])     # printuje ostatni element listy
print(scores[-2])     # printuje przed ostatni element listy
print(scores[4:7])   # printuje od 5 do 7 elementu z listy(ostatni element w nawiasie nie jest printowany)
print(scores[4:1000])  # printuje od 5 elementu do konca listy jesli jest mniej niz 1000 elementow na liscie

print(scores[::-1]) # printuje odwróconą liste



a = (1, 3, 4)
print(list(a))  # konwertuje krotke na liste

a = [1, 2 ,3]
print(tuple(a)) # konwertuje liste na krotke



n = int(input("How many elements you need? "))

elements = [1, 2, 3, 4, 5]
for _ in range(n):
    element = input("Input emelemnt of the list: ")
    elements.append(element)

my_tuples = tuple(elements)
print(my_tuples)