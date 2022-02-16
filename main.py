# Morse code alphabet
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', }


# Function to cipher the inputted text from the user
def cipher(message):
    # String that will be the new ciphered word
    translated_text = " "

    # Loop trough each letter in the inputted message and replace the letter with the equivalent in form of morse
    for letter in message:
        # If the message contains a space, add a / instead. (space in morse code)
        if letter == " ":
            translated_text += "/"
            continue

        # To separate each letter a longer gap, equal to the length of a dash, is left at the end of each letter
        translated_text += MORSE_CODE_DICT[letter.upper()] + " "

    print(translated_text)


print('TRANSLATE TEXT TO MORSE CODE')
user_text = input('Type message text here: ')

cipher(user_text)

"""
Alexander Darwiche
2022
"""