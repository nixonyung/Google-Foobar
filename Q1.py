def primes(n):
    """Returns a list of primes < n"""
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - 1 - i * i) // (2 * i) + 1)
    return ["2"] + [str(i) for i in range(3, n, 2) if sieve[i]]


# using 21000 so that the length of the string of primes just exceeds 10000
primesList = primes(21000)


def solution(i):
    return "".join(primesList)[i : i + 5]


print(solution(0))
print(solution(3))
