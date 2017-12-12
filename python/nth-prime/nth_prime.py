def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        return True


def nth_prime(positive_number):
    if positive_number <= 0:
        raise ValueError

    prime = 2
    while positive_number > 1:
        prime += 1
        if is_prime(prime):
            positive_number -= 1
    return prime
