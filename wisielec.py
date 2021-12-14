import sys
import linecache
import random

no_of_tries = 5
word = ""
user_word = []
used_letters = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostałe życia:", no_of_tries)
    print("Użyte litery:", used_letters)
    print()

def ask_about_life():
    while True:
        no_of_tries = input("Jaką ilość prób potrzebujesz? ")
        if( no_of_tries.isdigit()):
            if( int(no_of_tries) > 0):
                break
            else:
                print("Podaj liczbę większą od zera")
        else:
            print("Podaj liczbę, a nie inny znak")

    no_of_tries = int(no_of_tries)
    return no_of_tries

def pick_a_word():
    word = linecache.getline('slowa-nopl.txt', random.randint(0, 304584))
    word = word.strip()
    return word

def clear_user_word():
    user_word.clear()
    for _ in word:
        user_word.append("_")
    return user_word

word = pick_a_word()

user_word = clear_user_word()

no_of_tries = ask_about_life()

while True:

    letter = input("Podaj literę: ")

    while (len(letter) == 0 or letter == int or ord(letter) < ord('A') or ord(letter) > ord('z')):
        letter = input("Błąd! Podaj litere:")

    cont = 0

    for lett in used_letters:
        if (letter == lett):
            print("Ta litera już wystąpiła. Podaj inna")
            cont = 1
    
    if cont == 1:
        continue
    used_letters.append(letter)


    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery")
        no_of_tries -= 1

        if no_of_tries == 0:
            print("Koniec gry. Przegrałeś!!!")
            one_more_try = input("Chcesz zagrać jeszcze raz? T/N ")
            if((one_more_try == 'T') or (one_more_try == "t")):
                no_of_tries = ask_about_life()
                word = pick_a_word()
                user_word = clear_user_word()
                used_letters.clear()
            else:
                sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("Brawo to jest to słowo\n")
            print(word) 
            one_more_try = input("\nChcesz zagrać jeszcze raz? T/N ")

            
            if((one_more_try == 'T') or (one_more_try == "t")):
                no_of_tries = ask_about_life()
                word = pick_a_word()
                user_word = clear_user_word()
                used_letters.clear()
            else:
                sys.exit(0)
    

    show_state_of_game()