def distance(strand_a, strand_b):

    hamming_distance = 0
    list_a = list(strand_a)
    list_b = list(strand_b)

    if len(list_a) != len(list_b):
        raise ValueError
    else:
        hamming_distance = 0
        for index, value in enumerate(list_a):
            if list_a[index] != list_b[index]:
                hamming_distance += 1
        return hamming_distance
