

def convert(morse_string):
    # Creat a dictionary of Morse codes
    Dict = {'A': '.-', 'B': '-...','C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....','I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.','O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....','7': '--...', '8': '---..',
            '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
            '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

    morseCode = ""
    for n in morse_string:
        #convert input to upper string and encryption with dictionary of morse codes
        morseCode += Dict[n.upper()]
    return morseCode

# Get the string as input from the user.
morse_string = input('Enter the string: ')
print(convert(morse_string))