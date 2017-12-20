def is_isogram(words):
    words = words.lower()
    for char in words:
        if words.count(char) > 1:
            if char == '-' or char == ' ':
                break
            return False
    return True
