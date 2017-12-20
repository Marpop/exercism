def nth_prime(positive_number):
    if positive_number <= 0:
        raise ValueError

    prime_list = [2]
    number = 3

    while len(prime_list) < positive_number:
        for prime in prime_list:
            if number % prime == 0:
                break
        else:
            prime_list.append(number)
        number += 2

    return prime_list[-1]
