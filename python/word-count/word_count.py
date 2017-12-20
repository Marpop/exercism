def word_count(phrase):
    words = phrase.lower().replace(
        '.', ' ').replace(
        ':', ' ').replace(
        ',', ' ').replace(
        '!', ' ').replace(
        '&', ' ').replace(
        '@', ' ').replace(
        '$', ' ').replace(
        '^', ' ').replace(
        '%', ' ').replace(
        '&', ' ').replace(
        '_', ' ').replace(
        '\' ', ' ').replace(
        ' \'', ' ').split()

    result = {}
    for word in words:
        result[word] = words.count(word)
    print("\n" + str(result) + "\n")
    return result
