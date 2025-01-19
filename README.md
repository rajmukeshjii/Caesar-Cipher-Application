This is a Python application that implements the Caesar Cipher, a simple encryption technique where each letter in the plaintext is shifted by a certain number of positions in the alphabet. The application supports both encryption and decryption of text.

Features

Encrypt text using the Caesar Cipher technique.

Decrypt text to retrieve the original plaintext.

Handles both uppercase and lowercase letters.

Retains non-alphabetic characters (e.g., spaces, punctuation) unchanged.

User-friendly interface for inputting text, choosing operation mode (encrypt/decrypt), and specifying the shift value.

How It Works

The user selects whether they want to encrypt or decrypt a text.

The user provides the input text and a shift value (an integer).

The application processes each character:

Alphabetic characters are shifted by the specified value.

Non-alphabetic characters remain unchanged.

The resulting text is displayed.

Encryption Example

Input:

Mode: encrypt

Text: Hello, World!

Shift: 3

Output: Khoor, Zruog!

Decryption Example

Input:

Mode: decrypt

Text: Khoor, Zruog!

Shift: 3

Output: Hello, World!

