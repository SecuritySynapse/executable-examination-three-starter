"""Question One: Executable Examination."""

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import Callable

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

# Function specification for encrypt_caesar_cipher:
# The function encrypt_caesar_cipher should:
# --> Take as input the parameters:
#   - plaintext: a string that represents the plaintext to be encrypted
#   - shift: an integer that represents the shift to be applied
# --> Produce as output a string that represents the encrypted text
# --> The output string will be encrypted using a Caesar cipher with the provided shift,
#     This means that the cipher will take a letter in the plaintext and shift it
#     by the shift amount to produce that specific letter in the output ciphertext.

# Function specification for decrypt_caesar_cipher:
# The function decrypt_caesar_cipher should:
# --> Take as input the parameters:
#   - ciphertext: a string that represents the ciphertext to be decrypted
#   - shift: an integer that represents the shift to be applied
# --> Produce as output a string that represents the decrypted text
# --> The output string will be decrypted using a Caesar cipher with the provided shift,
#     This means that the cipher will take a letter in the ciphertext and shift it
#     by the shift amount in the opposite direction (of the encryption algorithm) to
#     produce that specific letter in the output plaintext.

# The following property should hold for all inputs to these functions:
# --> The original plaintext should be equal to the output of
#     decrypt_caesar_cipher(encrypt_caesar_cipher(plaintext, shift), shift).
# --> In other words, the decryption of the encryption of the plaintext
#     should be equal to the original plaintext.
# --> In other words, the decryption algorithm should "undo" or "reverse"
#    the encryption algorithm.

# The function send_message_to_client_using_caesar_cipher should:
# --> Take as input the parameters:
#     - client: an instance of the Client
#     - plaintext: a string that represents the plaintext to be encrypted
#     - shift: an integer that represents the shift to be applied
# --> This function does not need to return anything. However, it should use
# the receive_message method of the client to send the encrypted message.

# --> Importantly, you must modify the implementation of the Client class so
# that it stores the received messages in the message_history attribute that
# is shared across all instances of the Client class. This means that you will
# need to make sure that the message_history is a class variable.
# --> For this implementation of simple "network communication" there is
# one history of messages across all of the instances of the Client class.


class Client:
    """A class representing a client."""

    def __init__(self, client_id: str):
        """Initialize the Client instance."""
        self.client_id = client_id
        self.message_history = []

    def receive_message(self, message: str):
        """Receive a message and store it in the message history."""
        self.message_history.append(message)

    def __repr__(self):
        """Return a string representation of the Client instance."""
        return f"Client(client_id={self.client_id}, message_history={self.message_history})"


def encrypt_caesar_cipher(plaintext, shift):
    result = ""
    return result


def decrypt_caesar_cipher(ciphertext, shift):
    result = ""
    return result


def send_message_to_client_using_caesar_cipher(client, plaintext, shift):
    return None

# }}}

# Part (b) {{{

# Instructions: Implement the following functions so that they adhere to all
# aspects of the following specification.

# Function specification:
# The function encrypt_latin_alphabet should:
# --> Take as input the parameter called text, which is a string
# --> Produce as output a string that represents the encrypted
#     text using the Latin alphabet cipher
# --> The Latin alphabet cipher will encrypt each letter in the
#     plaintext with the corresponding number of the letter in the
#     alphabet. For example, the letter "A" will be encrypted to "1",
#     the letter "B" will be encrypted to "2", and so on.
# --> If there is a non-alphabetic letter in the plaintext, this
#     function should leave it unchanged in the output ciphertext. This
#     means that if there is a space, number, or symbol in the plaintext,
#     it should be left unchanged in the output ciphertext.
# --> This function should only work with upper-case letters in
#     the English alphabet. This means that if it sees a lower-case
#     letter it should convert it to upper-case before encrypting it.

# Function specification:
# The function decrypt_latin_alphabet should:
# --> Take as input the parameter called text, which is a string
# --> Produce as output a string that represents the decrypted
#     text using the Latin alphabet cipher
# --> The Latin alphabet cipher will decrypt each number in the
#     ciphertext with the corresponding letter of the alphabet. For example,
#     the number "1" will be decrypted to "A", the number "2" will be decrypted
#     to "B", and so on.
# --> If there is a non-numeric character in the ciphertext, this
#     function should leave it unchanged in the output plaintext. This
#     means that if there is a space, letter, or symbol in the ciphertext,
#     it should be left unchanged in the output plaintext.
# --> This function should only work with numbers representing
#     upper-case letters in the English alphabet. This means that the
#     decrypted letters should be in upper-case.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.

# The following property should hold for all inputs:
# --> The original plaintext should be equal to the output of
#     decrypt_latin_alphabet(encrypt_latin_alphabet(plaintext)).
# --> In other words, the decryption of the encryption of the plaintext
#     should be equal to the original plaintext.
# --> In other words, the decryption algorithm should "undo" or "reverse"
#    the encryption algorithm.


def encrypt_latin_alphabet(text: str) -> str:
    """Encrypt the provided plaintext using the Latin alphabet cipher."""
    encrypted = []
    return "".join(encrypted)


def decrypt_latin_alphabet(text: str) -> str:
    """Decrypt the provided ciphertext using the Latin alphabet cipher."""
    decrypted = []
    return decrypted


# }}}


# Part (c) {{{

# Instructions: Implement and/or debug the following functions so that they
# adheres to all aspects of the following specification.

# Function specification for reverse_string_encrypt:
# The function reverse_string_encrypt should:
# --> Take as input the parameter:
#     plaintext: a string that represents the plaintext to be encrypted
# --> Produce as output a string that represents the encrypted text
# --> The output string will be encrypted by reversing the order of the
#     characters in the plaintext.

# Function specification for reverse_string_decrypt:
# The function reverse_string_decrypt should:
# --> Take as input the parameter:
#     ciphertext: a string that represents the ciphertext to be decrypted
# --> Produce as output a string that represents the decrypted text
# --> The output string will be decrypted by reversing the order of the
#     characters in the ciphertext.

# The following property should hold for all inputs:
# --> The original plaintext should be equal to the output of
#     reverse_string_decrypt(reverse_string_encrypt(plaintext)).
# --> In other words, the decryption of the encryption of the plaintext
#     should be equal to the original plaintext.
# --> In other words, the decryption algorithm should "undo" or "reverse"
#     the encryption algorithm.

# TODO: Even though this is not considered an example of a useful cryptographic
# algorithm, it is still a suitable example of a way to associated the
# plaintext with the ciphertext during a cryptanalysis process for a more
# realistic cryptographic algorithm.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def reverse_string_encrypt(plaintext):
    """Encrypt the provided plaintext by reversing the order of its characters."""
    return ""


def reverse_string_decrypt(ciphertext):
    """Decrypt the provided ciphertext by reversing the order of its characters."""
    return ""


def reverse_string_encrypt_dictionary(plaintexts):
    """Encrypt a list of plaintexts by reversing and returning a dictionary of data."""
    return {}


# }}}

# Part (d) {{{

# Instructions: Implement the following functions so that they adhere to all
# aspects of the following specification.

# Function specification for general_encrypt:
# The function general_encrypt should:
# --> Take as input the parameters:
#     - plaintext: a string that represents the plaintext to be encrypted
#     - encrypt_function: a function that will be used to encrypt the plaintext
# --> Produce as output a string that represents the encrypted text
# --> The output string will be encrypted using the provided encrypt_function
# --> The provided encrypt_function will be one of the encryption functions
#     provided in this file

# Function specification for general_decrypt:
# The function general_decrypt should:
# --> Take as input the parameters:
#     - ciphertext: a string that represents the ciphertext to be decrypted
#     - decrypt_function: a function that will be used to decrypt the ciphertext
# --> Produce as output a string that represents the decrypted text
# --> The output string will be decrypted using the provided decrypt_function
# --> The provided decrypt_function will be one of the decryption functions
#     provided in this file

# The following property should hold for all inputs:
# --> The original plaintext should be equal to the output of
#     general_decrypt(general_encrypt(plaintext, encrypt_function), decrypt_function)
# --> In other words, the decryption of the encryption of the plaintext
#     should be equal to the original plaintext.
# --> In other words, the decryption algorithm should "undo" or "reverse"
#    the encryption algorithm

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def general_encrypt(plaintext: str, encrypt_function: Callable):
    """Encrypt the provided plaintext using the specified encrypt function."""
    return ""


def general_decrypt(ciphertext: str, decrypt_function: Callable):
    """Decrypt the provided ciphertext using the specified decrypt function."""
    return ""


# }}}
