def fibonacci(terms):
    fib = [0, 1]
    if terms < 1:
        return None
    else:
        while len(fib) <= terms:
            fib.append(fib[-1] + fib[-2])
    return fib[-1]


def double_investment(principle, rate):
    year = 0
    total = principle * 2
    principle = principle
    while principle < total:
        principle *= (1 + rate)
        year += 1
    return year


def syracuse(num):
    syr = []
    syr.append(num)
    while num != 1:
        if num % 2 != 0:
            num = 3 * num + 1
            syr.append(num)
        else:
            num = num / 2
            syr.append(num)
    return syr


def goldbach(num):
    primes = []
#     while num >= 2:
#         if num % 2 != 0:
#             return None
#         else:
#             prm = num / 2
#             if prm % 2 != 0:
#                 primes.append(prm)
#             else:
#                 prm = prm / 2
#             primes.append(prm)
    return primes

