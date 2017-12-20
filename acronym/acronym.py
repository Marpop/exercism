def abbreviate(words):
    words_list = words.replace('-', ' ').split(' ')
    first_letters = [letter[0].upper() for letter in words_list]
    return "".join(first_letters)
