def caesar_cipher(string, offset):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    secret_word = ''

    for i in string:
        position = alphabet.index(i) - offset
        new_char = alphabet[position]
        secret_word += new_char

    return secret_word

secret = caesar_cipher("jerry", 4)
print(secret)