# Traemos herramientas de python
import random
import string
# Traemos datos auxiliares
from words import words
from graphic import steps

# Funcion que selecciona una palabra aleatoria a adivinar y la devuelve
def get_word(word):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    print("=======================================")
    print("¡Bienvenido(a)s al juego del Ahorcado! ")
    print("=======================================")

    word = get_word(words) # palabra a adivinar
    guessing_letter = set(word) # Volvemos la palabra iterable en letras sin adivinar
    all_letters = set(string.ascii_uppercase) # Definimos un abecedario
    guessed_letters = set() # iteramos las letras que ya se adivinaron

    lifes = 7

    # Mientras hayan letras sin adivinar
    while len(guessing_letter) > 0 and lifes > 0:
        print(f"Aun tienes {lifes} vidas y ya usaste las letras: {' '.join(guessed_letters)}") #concatemos las letras adivinadas

        word_done = [ letter if letter in guessed_letters else '-' for letter in word] # La letra adivinada la mostramos sino permanece oculta
        print(steps[lifes])
        print(f"Palabra: {' '.join(word_done)}")

        input_letter = input('Escoge una letra: ').upper() #Recibimos la letra a adivinar por el usuario

        if input_letter in all_letters - guessed_letters: # validamos si la letra ingresada esta en el abecedario y en las letras adivinadas
            guessed_letters.add(input_letter) # Listamos las letras adivinadas
            if input_letter in guessing_letter:
                guessing_letter.remove(input_letter) # quitamos las letras pendientes 
                print('')
            else:
                lifes = lifes - 1 # Al fallar restamos 1 vida 
                print(f"\nLa letra, {input_letter} no existe en la palabra")
        elif input_letter in guessed_letters:
            print("\nEsa letra ya fue elegida. Por favor escoge una nueva letra")
        else:
            print("\nLa letra {input_letter} no es una letra válida")

    # Game over
    if lifes == 0:
        print(steps[lifes])
        print(f"Terminaste ahorcado, perdiste. La palabra que intentaste adivinar era: {word}")
    else:
        print(f"Felicidades has adivinado la palabra: {word}") # Win

if __name__ == '__main__':
    hangman()