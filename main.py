def prime_numbers(low, high):
    if not isinstance(low, int) or not isinstance(high, int) or low > high:
        return []

    primes = []

    for num in range(max(low, 2), high+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes
print(prime_numbers(0,32))