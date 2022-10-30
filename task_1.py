def remove_parentheses(text):
    i1 = ""
    i2 = ""

    if ('(' or ')') not in text:
        print("Nie ma co usuwać ¯\_(ツ)_/¯")
        return text

    for character in text:
        if character == '(':
            i1 = text.index(character)
        if character == ')':
            i2 = text.index(character)
        if i1 != "" and i2 != "":
            text = text[0:i1] + text[i2+2:len(text)]
            i1 = ""
            i2 = ""
    return text


string = "(Nie) jest (tak) źle"

print(remove_parentheses(string))
