def is_pangram(sentence):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if sentence.lower().count(letter) < 1:
            return False
    return True
