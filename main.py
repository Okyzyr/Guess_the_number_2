"""
Odwróćmy teraz sytuację z pierwszego zadania: ("Gra w zgadywanie liczb").
Niech użytkownik pomyśli sobie liczbę z zakresu 1-1000, a komputer będzie zgadywał.
Zrobi to maksymalnie w 10 ruchach (pod warunkiem, że gracz nie będzie oszukiwał).
Zadaniem gracza będzie udzielanie odpowiedzi "To small", "To big", "You win".
Do tego warsztatu dołączony jest schemat blokowy algorytmu. Zaimplementuj go w Pythonie.
"""

from random import randint

def guess2():
    print("Rules: Pick one number and I will try to guess it in 10 tries.")
    number = 0
    while True:
        try:
            get_number = input("Input natural number in range 1-1000: ")
            get_number = int(get_number)
        except:
            print("It's not a natural number!")
            continue
        if get_number > 1000 or get_number < 1:
            print("Out of range")
            continue
        number = get_number
        break
    return number


print(guess2())