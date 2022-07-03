from fractions import Fraction, gcd
from functools import reduce

import numpy as np


def lcm(x, y):
    return int(x * y / gcd(x, y))


def find_lcm(list):
    return reduce(lcm, list)


def find_gcd(list):
    return reduce(gcd, list)


def fracs_to_ints(list):
    denominators = [x.denominator for x in list]
    result = [(x * find_lcm(denominators)).numerator for x in list]
    result = [x // find_gcd(result) if find_gcd(result) != 0 else x for x in result]

    return result


def solution(m):
    m = np.array(m) + Fraction()
    for i in range(len(m)):
        row_sum = sum(m[i])
        if row_sum != 0:
            m[i] /= row_sum

    is_terminal = np.sum(m, axis=1) == 0

    def state_part_of(current):
        state = np.copy(current)
        state[is_terminal] = Fraction(0)

        return fracs_to_ints(state)

    current = np.zeros(len(m), dtype="int") + Fraction()
    current[0] = Fraction(1)

    state_queue = [state_part_of(current)]
    result = np.zeros(len(m), dtype="int") + Fraction()

    while True:
        current = np.dot(current.T, m)

        if sum(current) == 0:
            break

        result += current

        state = state_part_of(current)
        if state in state_queue:
            break
        else:
            state_queue.append(state)

    ans = fracs_to_ints(result[is_terminal])
    return ans + [sum(ans) or 1]


print(
    solution(
        [
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)
print(
    solution(
        [
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)
print(
    solution(
        [
            [0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)
print(
    solution(
        [
            [1, 0],
            [0, 0],
        ]
    )
)
print(
    solution(
        [
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
    )
)
print(
    solution(
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
    )
)
print(
    solution(
        [
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ]
    )
)
