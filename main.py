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
    guess = 0
    answers = ["too big", "too small", "correct"]
    min_num, max_num = 1, 1000
    tryed = 0
    while True:
        try:
            get_number = input("Input natural number in range 1-1000: ")
            get_number = int(get_number)
        except:
            print("It's not a natural number!")
            continue
        if get_number <= 1000 and get_number >= 1:
            break
        print("Out of range")
    while tryed < 2:
        guess = randint(min_num, max_num)
        print("I'm guessing: ", guess, f"|Range {min_num} - {max_num}|")
        tryed += 1
        if guess == get_number:
            return answers[10]
        elif guess < get_number:
            min_num = guess
            print(answers[1])
            continue
        else:
            max_num = guess
            print(answers[0])
            continue
    return "za duzo prób"


guess2()
