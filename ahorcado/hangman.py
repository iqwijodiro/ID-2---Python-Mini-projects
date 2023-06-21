import random
import string

from words import words
from graphic import steps

def get_valid_word(word):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    print("=======================================")
    print("¡Bienvenido(a)s al juego del Ahorcado! ")
    print("=======================================")

    word = get_valid_word(words)
    guessing_letter = set(word)
    all_letters = set(string.ascii_uppercase)
    guessed_letters = set()

    lifes = 5

    while len(guessing_letter) > 0 and lifes > 0:
        print(f"Aun tienes {lifes} vidas y ya usaste las letras: {' '.join(guessed_letters)}")

        word_done = [ letter if letter in guessed_letters else '-' for letter in word]
        print(steps[lifes])
        print(f"Palabra: {' '.join(word_done)}")

        input_letter = input('Escoge una letra: ').upper()

        if input_letter in all_letters - guessed_letters:
            guessed_letters.add(input_letter)
            if input_letter in guessing_letter:
                guessing_letter.remove(input_letter)
                print('')
            else:
                lifes = lifes - 1
                print(f"\nLa letra, {input_letter} no existe en la palabra")
        elif input_letter in guessed_letters:
            print("\nEsa letra ya fue elegida. Por favor escoge una nueva letra")
        else:
            print("\nLa letra {input_letter} no es una letra válida")

    if lifes == 0:
        print(steps[lifes])
        print(f"Terminaste ahorcado, perdiste. La palabra que intentaste adivinar era: {word}")
    else:
        print(f"Felicidades has adivinado la palabra: {word}")

if __name__ == '__main__':
    hangman()