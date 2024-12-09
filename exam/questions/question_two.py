"""Question Two: Executable Examination."""

# Note: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import Callable, List
import math

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break other function(s).

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml file
# in this GitHub repository for the configuration and name of each tool used
# to analyze the code inside of this file.

# }}}

# Part (a) {{{

# Instructions: Implement and/or debug the following functions so that they
# adheres to all aspects of the following specification.

# Function specification for encrypt_atbash_cipher:
# The function encrypt_atbash_cipher should:
# --> Take as input the parameter:
#     plaintext: a string that represents the plaintext to be encrypted
# --> Produce as output a string that represents the encrypted text
# --> The output string will be encrypted using the Atbash cipher.
#     This means that the cipher will take a letter in the plaintext and replace it
#     with the letter in the opposite position in the alphabet to produce that
#     specific letter in the output ciphertext.

# Function specification for decrypt_atbash_cipher:
# The function decrypt_atbash_cipher should:
# --> Take as input the parameter:
#     ciphertext: a string that represents the ciphertext to be decrypted
# --> Produce as output a string that represents the decrypted text
# --> The output string will be decrypted using the Atbash cipher,
#     This means that the cipher will take a letter in the ciphertext and replace it
#     with the letter in the opposite position in the alphabet to produce that
#     specific letter in the output plaintext.

# The following property should hold for all inputs:
# --> The original plaintext should be equal to the output of
#     decrypt_atbash_cipher(encrypt_atbash_cipher(plaintext)).
# --> In other words, the decryption of the encryption of the plaintext
#     should be equal to the original plaintext.
# --> In other words, the decryption algorithm should "undo" or "reverse"
#     the encryption algorithm.

def encrypt_atbash_cipher(plaintext):
    """Encrypt the provided plaintext using the Atbash cipher."""
    result = ""
    return result


def decrypt_atbash_cipher(ciphertext):
    """Decrypt the provided ciphertext using the Atbash cipher."""
    return ""


# }}}

# Part (b) {{{

# Instructions: Implement and/or debug the following functions so that they
# adheres to all aspects of the following specification.

# Function specification for encrypt_transposition_cipher:
# The function encrypt_transposition_cipher should:
# --> Take as input the parameter:
#     key: an integer that represents the key for the transposition cipher
#     message: a string that represents the plaintext to be encrypted
# --> Produce as output a string that represents the encrypted text
# --> The output string will be encrypted using the Transposition cipher.
#     This means that the cipher will rearrange the order of characters in the plaintext
#     based on a certain algorithm to produce the output ciphertext.

# Function specification for decrypt_transposition_cipher:
# The function decrypt_transposition_cipher should:
# --> Take as input the parameter:
#     key: an integer that represents the key for the transposition cipher
#     message: a string that represents the plaintext to be encrypted
# --> Produce as output a string that represents the decrypted text
# --> The output string will be decrypted using the Transposition cipher,
#     This means that the cipher will rearrange the order of characters in the ciphertext
#     based on a certain algorithm to produce the output plaintext.

# The following property should hold for all inputs:
# --> The original plaintext should be equal to the output of
#     decrypt_transposition_cipher(encrypt_transposition_cipher(plaintext)).
# --> In other words, the decryption of the encryption of the plaintext
#     should be equal to the original plaintext.
# --> In other words, the decryption algorithm should "undo" or "reverse"
#     the encryption algorithm.

# Note that the transposition cipher involves placing the input message into a
# grid, and then reading the message out column by column. This algorithm uses
# a symmetric key to determine the number of columns in the grid. It is
# possible that certain positions in the grid will be "shaded" or "blanked" out
# if the input message's length is not a multiple of the key.

def encrypt_transposition_cipher(key, message):
    ciphertext = [""] * key
    return "".join(ciphertext)


def decrypt_transposition_cipher(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    plaintext = [""] * numOfColumns
    return "".join(plaintext)


# }}}


# Part (c) {{{

# Instructions: Implement and/or debug the following functions so that they
# adheres to all aspects of the following specification.

# Function specification for rot13_encrypt:
# The function rot13_encrypt should:
# --> Take as input the parameter:
#     plaintext: a string that represents the plaintext to be encrypted
# --> Produce as output a string that represents the encrypted text
# --> The output string will be encrypted by shifting each alphabetic character
#     13 places to the right in the alphabet, wrapping around from 'z' to 'a' and 'Z' to 'A'.

# Function specification for rot13_decrypt:
# The function rot13_decrypt should:
# --> Take as input the parameter:
#     ciphertext: a string that represents the ciphertext to be decrypted
# --> Produce as output a string that represents the decrypted text
# --> The output string will be decrypted by shifting each alphabetic character
#     13 places to the left in the alphabet, wrapping around from 'a' to 'z' and 'A' to 'Z'.

# The following property should hold for all inputs:
# --> The original plaintext should be equal to the output of
#     rot13_decrypt(rot13_encrypt(plaintext)).
# --> In other words, the decryption of the encryption of the plaintext
#     should be equal to the original plaintext.
# --> In other words, the decryption algorithm should "undo" or "reverse"
#     the encryption algorithm.

# Please note that neither the encryption or decryption algorithms should
# handle inputs such as numbers or punctuation marks. The algorithms should
# only work with alphabetic characters and simply "pass through" (i.e., not
# attempt to encrypt or decrypt) any non-alphabetic characters.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.

def rot13_encrypt(plaintext):
    result = ""
    return result


def rot13_decrypt(ciphertext):
    result = ""
    return result


# }}}

# Part (d) {{{

# Instructions: Implement and/or debug the following functions so that they
# adhere to all aspects of the following specification.

# Function specification for apply_encryption_methods:
# The function apply_encryption_methods should:
# --> Take as input the parameters:
#     functions: a list of functions that take a string as input and return a string
#     plaintext: a string that represents the plaintext to be encrypted
# --> Produce as output a string that represents the encrypted text
#     that results from applying the encryption functions to the plaintext
#     in the order they appear in the functions list.
# --> This function only needs to work for the encryption algorithms that
#     provide the ROT13 and Atbash ciphers.

# Function specification for apply_decryption_methods:
# The function apply_decryption_methods should:
# --> Take as input the parameters:
#     functions: a list of functions that take a string as input and return a string
#     ciphertext: a string that represents the ciphertext to be decrypted
# --> Produce as output a string that represents the decrypted text
#     that results from applying the decryption functions to the ciphertext
#     in the order they appear in the functions list.
# --> This function only needs to work for the decryption algorithms that
#     provide the ROT13 and Atbash ciphers.

# Function specification for encrypt_and_package:
# The function encrypt_and_package should:
# --> Take as input the parameters:
#     functions: a list of functions that take a string as input and return a string
#     plaintext: a string that represents the plaintext to be encrypted
# --> Produce as output a dictionary that represents the encrypted text
#     that results from applying the encryption functions to the plaintext
# --> The dictionary should have the following key-value pairs:
#    - "action": a string that represents the action taken (e.g., "encrypt")
#    - "result": a string that stores the encrypted text

# Function specification for unpackage_and_decrypt:
# The function unpackage_and_decrypt should:
# --> Take as input the parameters:
#     functions: a list of functions that take a string as input and return a string
#     data: a dictionary that represents the packaged version of the encrypted text
# --> Produce as output a string that represents the decrypted text
#     that results from applying the decryption functions to the ciphertext

# Note: These functions may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: These functions may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.

def apply_encryption_methods(
    functions: List[Callable[[str], str]], plaintext: str
) -> str:
    return plaintext


def apply_decryption_methods(
    functions: List[Callable[[str], str]], ciphertext: str
) -> str:
    return ciphertext


def encrypt_and_package(functions: List[Callable[[str], str]], plaintext: str) -> dict:
    """Encrypt the plaintext and package it in a dictionary for network transmission."""
    return {}


def unpackage_and_decrypt(functions: List[Callable[[str], str]], data: dict) -> str:
    """Unpackage the data dictionary after network transmission and decrypt the ciphertext."""
    return ""


# }}}
