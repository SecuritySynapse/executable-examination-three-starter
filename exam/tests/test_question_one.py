"""Confirm the correctness of functions in question_one."""

import pytest

# ruff: noqa: PLR2004
from questions.question_one import (
    Client,
    decrypt_caesar_cipher,
    decrypt_latin_alphabet,
    encrypt_caesar_cipher,
    encrypt_latin_alphabet,
    general_decrypt,
    general_encrypt,
    reverse_string_decrypt,
    reverse_string_encrypt,
    reverse_string_encrypt_dictionary,
    send_message_to_client_using_caesar_cipher,
)


@pytest.mark.question_one_part_a
def test_encrypt_caesar_cipher():
    """Confirm correctness of question part."""
    assert encrypt_caesar_cipher("ABC", 3) == "DEF", "Failed to shift uppercase letters"
    assert encrypt_caesar_cipher("abc", 3) == "def", "Failed to shift lowercase letters"
    assert (
        encrypt_caesar_cipher("XYZ", 3) == "ABC"
    ), "Failed to wrap around uppercase letters"
    assert (
        encrypt_caesar_cipher("xyz", 3) == "abc"
    ), "Failed to wrap around lowercase letters"
    assert (
        encrypt_caesar_cipher("AbC", 3) == "DeF"
    ), "Failed to handle mixed case letters"
    assert (
        encrypt_caesar_cipher("AbC", 3) == "DeF"
    ), "Failed to handle mixed case letters with symbols"


@pytest.mark.question_one_part_a
def test_decrypt_caesar_cipher():
    """Confirm correctness of question part."""
    assert decrypt_caesar_cipher("DEF", 3) == "ABC", "Failed to shift uppercase letters"
    assert decrypt_caesar_cipher("def", 3) == "abc", "Failed to shift lowercase letters"
    assert (
        decrypt_caesar_cipher("ABC", 3) == "XYZ"
    ), "Failed to wrap around uppercase letters"
    assert (
        decrypt_caesar_cipher("abc", 3) == "xyz"
    ), "Failed to wrap around lowercase letters"
    assert (
        decrypt_caesar_cipher("DeF", 3) == "AbC"
    ), "Failed to handle mixed case letters"


@pytest.mark.question_one_part_a
def test_send_message_to_client_using_caesar_cipher():
    """Test sending multiple encrypted messages to a client using Caesar cipher."""
    client = Client(client_id="client_123")
    # send the first message
    send_message_to_client_using_caesar_cipher(client, "ABC", shift=3)
    assert (
        len(Client.message_history) == 1
    ), "Message history should have 1 message after the first send"
    assert (
        Client.message_history[0] == "DEF"
    ), "First message should be correctly encrypted"
    # send the second message
    send_message_to_client_using_caesar_cipher(client, "abc", shift=3)
    assert (
        len(Client.message_history) == 2
    ), "Message history should have 2 messages after the second send"
    assert (
        Client.message_history[1] == "def"
    ), "Second message should be correctly encrypted"
    # send the third message
    send_message_to_client_using_caesar_cipher(client, "AbC", shift=3)
    assert (
        len(Client.message_history) == 3
    ), "Message history should have 3 messages after the third send"
    assert (
        Client.message_history[2] == "DeF"
    ), "Third message should be correctly encrypted"

@pytest.mark.question_one_part_a
def test_send_message_to_client_using_caesar_cipher_multiple_clients():
    """Test sending multiple encrypted messages to a client using Caesar cipher."""
    Client.message_history = []
    client_one = Client(client_id="client_123")
    # send the first message
    send_message_to_client_using_caesar_cipher(client_one, "ABC", shift=3)
    assert (
        len(Client.message_history) == 1
    ), "Message history should have 1 message after the first send"
    assert (
        Client.message_history[0] == "DEF"
    ), "First shared message should be correctly encrypted"
    # send the second message
    send_message_to_client_using_caesar_cipher(client_one, "abc", shift=3)
    assert (
        len(Client.message_history) == 2
    ), "Message history should have 2 messages after the second send"
    assert (
        Client.message_history[1] == "def"
    ), "Second shared message should be correctly encrypted"
    client_two = Client(client_id="client_abc")
    # send the third message
    send_message_to_client_using_caesar_cipher(client_two, "AbC", shift=3)
    assert (
        len(Client.message_history) == 3
    ), "Message history should have 3 messages after the third send"
    assert (
        Client.message_history[2] == "DeF"
    ), "Third shared message should be correctly encrypted"
    # send the fourth message
    send_message_to_client_using_caesar_cipher(client_two, "AbC", shift=3)
    assert (
        len(Client.message_history) == 4
    ), "Message history should have 4 messages after the fourth send"
    assert (
        Client.message_history[3] == "DeF"
    ), "Fourth shared message should be correctly encrypted"


@pytest.mark.question_one_part_b
def test_encrypt_latin_alphabet():
    """Confirm correctness of question part."""
    assert encrypt_latin_alphabet("abc") == "123", "Failed on simple word 'abc'"
    assert encrypt_latin_alphabet("AbC") == "123", "Failed on mixed case 'AbC'"
    assert (
        encrypt_latin_alphabet("a b c") == "1 2 3"
    ), "Failed on input with spaces 'a b c'"
    assert (
        encrypt_latin_alphabet("a,b.c!") == "1,2.3!"
    ), "Failed on input with punctuation 'a,b.c!'"
    assert encrypt_latin_alphabet("") == "", "Failed on empty string"
    assert encrypt_latin_alphabet("123") == "123", "Failed on input with numbers '123'"
    assert (
        encrypt_latin_alphabet("@#$") == "@#$"
    ), "Failed on input with special characters '@#$'"
    assert (
        encrypt_latin_alphabet("@ # $") == "@ # $"
    ), "Failed on input with special characters '@#$' with spaces"
    assert encrypt_latin_alphabet("") == "", "Failed on empty string"


@pytest.mark.question_one_part_b
def test_decrypt_latin_alphabet():
    """Confirm correctness of question part."""
    assert (
        decrypt_latin_alphabet("123") == "ABC"
    ), "Failed on encrypted string '123' with no spaces"
    assert (
        decrypt_latin_alphabet("1 2 3") == "A B C"
    ), "Failed on encrypted string '123' with spaces"
    assert (
        decrypt_latin_alphabet("1,2.3!") == "A,B.C!"
    ), "Failed on input with punctuation '1,2.3!'"
    assert (
        decrypt_latin_alphabet("@ # $") == "@ # $"
    ), "Failed on input with special characters '@ # $' with spaces"
    assert (
        decrypt_latin_alphabet("@#$") == "@#$"
    ), "Failed on input with special characters '@ # $' with spaces"
    assert decrypt_latin_alphabet("") == "", "Failed on empty string"


@pytest.mark.question_one_part_c
def test_reverse_string_encrypt():
    """Confirm correctness of question part."""
    assert reverse_string_encrypt("ABC") == "CBA", "Failed to reverse string"
    assert reverse_string_encrypt("123") == "321", "Failed to reverse numeric string"
    assert reverse_string_encrypt("abc") == "cba", "Failed to reverse lowercase string"
    assert reverse_string_encrypt("AbC") == "CbA", "Failed to reverse mixed case string"
    assert reverse_string_encrypt("X") == "X", "Failed to handle singleton string"
    assert reverse_string_encrypt("") == "", "Failed to handle empty string"


@pytest.mark.question_one_part_c
def test_reverse_string_decrypt():
    """Confirm correctness of question part."""
    assert reverse_string_decrypt("CBA") == "ABC", "Failed to reverse string"
    assert reverse_string_decrypt("321") == "123", "Failed to reverse numeric string"
    assert reverse_string_decrypt("cba") == "abc", "Failed to reverse lowercase string"
    assert reverse_string_decrypt("CbA") == "AbC", "Failed to reverse mixed case string"
    assert reverse_string_decrypt("X") == "X", "Failed to handle singleton string"
    assert reverse_string_decrypt("") == "", "Failed to handle empty string"


@pytest.mark.question_one_part_c
def test_reverse_string_encrypt_dictionary():
    """Confirm correctness of question part."""
    assert reverse_string_encrypt_dictionary(["ABC", "123", "abc", "AbC", "X", ""]) == {
        "ABC": "CBA",
        "123": "321",
        "abc": "cba",
        "AbC": "CbA",
        "X": "X",
        "": "",
    }, "Failed to encrypt and map plaintexts to ciphertexts"


@pytest.mark.question_one_part_d
def test_general_encrypt():
    """Confirm correctness of question part."""
    # test with encrypt_latin_alphabet and decrypt_latin_alphabet
    plaintext = "ABC"
    ciphertext = general_encrypt(plaintext, encrypt_latin_alphabet)
    decrypted_text = general_decrypt(ciphertext, decrypt_latin_alphabet)
    assert (
        decrypted_text == plaintext
    ), "Failed on encrypt_latin_alphabet and decrypt_latin_alphabet with input 'ABC'"
    # test with encrypt_caesar_cipher and decrypt_caesar_cipher
    plaintext = "XYZ"
    shift = 3
    ciphertext = general_encrypt(
        plaintext, lambda text: encrypt_caesar_cipher(text, shift)
    )
    decrypted_text = general_decrypt(
        ciphertext, lambda text: decrypt_caesar_cipher(text, shift)
    )
    assert (
        decrypted_text == plaintext
    ), "Failed on encrypt_caesar_cipher and decrypt_caesar_cipher with input 'XYZ' and shift 3"
    # test with reverse_string_encrypt and reverse_string_decrypt
    plaintext = "HELLO"
    ciphertext = general_encrypt(plaintext, reverse_string_encrypt)
    decrypted_text = general_decrypt(ciphertext, reverse_string_decrypt)
    assert (
        decrypted_text == plaintext
    ), "Failed on reverse_string_encrypt and reverse_string_decrypt with input 'HELLO'"
