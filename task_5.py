def cipher(text, shift):
    result = ""
    for char in text:
        unicode_char = ord(char)
        if unicode_char + shift < 122 and not char.isupper():
            unicode_char += shift
        elif unicode_char + shift < 90:
            unicode_char += shift
        else:
            unicode_char -= 26 + shift
        char = chr(unicode_char)  # za wiedzialem jak zmieniac pojedyncze znaki w stringu, ale tak tez dziala xd
        result += char
    return result


def decipher(text, shift):
    result = ""
    for char in text:
        unicode_char = ord(char)
        if unicode_char - shift > 97 and not char.isupper():
            unicode_char -= shift
        elif unicode_char - shift > 65:
            unicode_char -= shift
        else:
            unicode_char += 26 - shift
        char = chr(unicode_char)
        result += char
    return result


print(cipher("Imperator", 1))
print(decipher("Jnqfsbups", 1))
