def prime_factors(natural_number):
    factors = []
    while natural_number > 1:
        for i in range(2, natural_number + 1):
            if (natural_number % i) == 0:
                factors.append(i)
                natural_number = natural_number // i
                break
    return factors
