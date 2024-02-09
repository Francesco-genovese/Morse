MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                   'C':'-.-.', 'D':'-..', 'E':'.',
                   'F':'..-.', 'G':'--.', 'H':'....',
                   'I':'..', 'J':'.---', 'K':'-.-',
                   'L':'.-..', 'M':'--', 'N':'-.',
                   'O':'---', 'P':'.--.', 'Q':'--.-',
                   'R':'.-.', 'S':'...', 'T':'-',
                   'U':'..-', 'V':'...-', 'W':'.--',
                   'X':'-..-', 'Y':'-.--', 'Z':'--..',
                   '1':'.----', '2':'..---', '3':'...--',
                   '4':'....-', '5':'.....', '6':'-....',
                   '7':'--...', '8':'---..', '9':'----.',
                   '0':'-----', ', ':'--..--', '.':'.-.-.-',
                   '?':'..--..', '/':'-..-.', '-':'-....-',
                   '(':'-.--.', ')':'-.--.-', ' ':'/'}

def encrypt(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += ' '
    return morse_code

def decrypt(morse_code):
    morse_code = morse_code.split(' ')
    decrypted_text = ''
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                decrypted_text += key
    return decrypted_text

def main():
    choice = input("Vuoi criptare o decriptare? (c/d): ")
    
    if choice.lower() == 'c':
        text_to_encrypt = input("Inserisci il testo da criptare: ")
        encrypted_text = encrypt(text_to_encrypt)
        print(f"Testo originale: {text_to_encrypt}")
        print(f"Codice Morse: {encrypted_text}")
    elif choice.lower() == 'd':
        morse_code_to_decrypt = input("Inserisci il codice Morse da decriptare: ")
        decrypted_text = decrypt(morse_code_to_decrypt)
        print(f"Codice Morse: {morse_code_to_decrypt}")
        print(f"Testo decriptato: {decrypted_text}")
    else:
        print("Scelta non valida. Inserisci 'c' per criptare o 'd' per decriptare.")

if __name__ == "__main__":
    main()
