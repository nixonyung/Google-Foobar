import itertools


def xgcd(a, b):
    prev_x = 1
    prev_y = 0
    x = 0
    y = 1
    a1 = a
    b1 = b

    while b1:
        q = a1 // b1
        prev_x, x = x, prev_x - q * x
        prev_y, y = y, prev_y - q * y
        a1, b1 = b1, a1 - q * b1

    return a1, prev_x, prev_y


# def solution(num_buns, num_required):
#     num_key_copies = num_buns - num_required + 1
#     _, num_keys_per_bun, num_doors = xgcd(num_buns, num_key_copies)

#     print(num_keys_per_bun, num_doors)
#     possible_key_distributions = itertools.combinations(
#         list(range(num_doors)), num_keys_per_bun
#     )
#     print(list(possible_key_distributions))


def is_valid_distribution(distributions, num_required, num_doors):
    for i in range(1, num_required):
        for selecting_fewer_buns in itertools.combinations(distributions, i):
            if set().union(*selecting_fewer_buns) == set(range(num_doors)):
                return False
    for selecting_all_required_buns in itertools.combinations(
        distributions, num_required
    ):
        if set().union(*selecting_all_required_buns) != set(range(num_doors)):
            return False
    return True


def solution(num_buns, num_required):
    if num_required == 1:
        return [[0]] * num_buns

    num_doors = 1
    num_keys_per_bun = 1

    while num_doors <= 10:
        # print(num_doors, num_keys_per_bun)
        if num_keys_per_bun * num_buns % num_doors == 0:
            possible_keysets_for_a_bun = itertools.combinations(
                range(num_doors), num_keys_per_bun
            )
            possible_distributions = itertools.combinations(
                possible_keysets_for_a_bun, num_buns
            )
            # print(list(range(num_doors)))
            # print(num_keys_per_bun)
            # print(list(possible_keysets_for_a_bun))
            # print(list(possible_distributions))

            for distribution in possible_distributions:
                if is_valid_distribution(distribution, num_required, num_doors):
                    return distribution

        if num_keys_per_bun == num_doors:
            num_doors += 1
            num_keys_per_bun = 1
        else:
            num_keys_per_bun += 1


if __name__ == "__main__":
    print(solution(2, 1))
    print(solution(3, 1))
    print(solution(3, 2))
    print(solution(4, 2))
    print(solution(4, 3))
    print(solution(4, 4))
    print(solution(5, 3))

    # ans = [
    #     [0, 1, 2],
    #     [0, 3, 4],
    #     [1, 3, 5],
    #     [2, 4, 5],
    # ]

    # for combination in itertools.combinations(ans, 3):
    #     s = []
    #     for elm in combination:
    #         s = s + elm
    #     s = set(s)
    #     print(s)
