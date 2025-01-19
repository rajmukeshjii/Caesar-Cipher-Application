def caesar_cipher(text, shift, mode='encrypt'):
   
    if mode == 'decrypt':
        shift = -shift

    result = ''
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char  # Non-alphabetic characters remain unchanged

    return result

# Example usage
if __name__ == "__main__":
    print("Welcome to the Caesar Cipher program!")
    mode = input("Would you like to encrypt or decrypt? (Type 'encrypt' or 'decrypt'): ").strip().lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (a number): "))

    result = caesar_cipher(text, shift, mode)
    print(f"The resulting text is: {result}")
