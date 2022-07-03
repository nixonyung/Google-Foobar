from fractions import Fraction, gcd
from functools import reduce

import numpy as np


def lcm(x, y):
    return abs(x * y) // gcd(x, y)


def find_lcm_of(list):
    return reduce(lcm, list)


def solution(m):
    m = np.array(m) + Fraction()

    indices_row_all_zero = np.sum(m, axis=1) == 0
    m[indices_row_all_zero, indices_row_all_zero] = 1

    m /= np.sum(m, axis=1)[:, np.newaxis]

    is_absorbing_states = m.diagonal() == 1
    if m[0][0] == 1:
        result = [0] * sum(is_absorbing_states) + [1]
        result[0] = 1
        return result

    rearranged_indices = np.concatenate(
        (np.where(is_absorbing_states)[0], np.where(~is_absorbing_states)[0])
    )
    m = m[rearranged_indices, :]
    m = m[:, rearranged_indices]

    Q = m[sum(is_absorbing_states) :, sum(is_absorbing_states) :].copy()
    R = m[sum(is_absorbing_states) :, : sum(is_absorbing_states)].copy()
    F = np.linalg.inv(np.identity(Q.shape[0]) - Q.astype(float))
    FR = np.dot(F, R)

    result = [Fraction(x).limit_denominator() for x in FR[0]]
    result_lcm = find_lcm_of(x.denominator for x in result)
    result = [(x * result_lcm).numerator for x in result]

    return result + [sum(result)]


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
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ]
    )
)


# https://github.com/ivanseed/google-foobar-help/blob/master/challenges/doomsday_fuel/doomsday_fuel.md
