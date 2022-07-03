from collections import defaultdict

prev_to_curr = {
    ((0, 0), (0, 0)): 0,
    ((0, 0), (0, 1)): 1,
    ((0, 0), (1, 0)): 1,
    ((0, 0), (1, 1)): 0,
    ((0, 1), (0, 0)): 1,
    ((0, 1), (0, 1)): 0,
    ((0, 1), (1, 0)): 0,
    ((0, 1), (1, 1)): 0,
    ((1, 0), (0, 0)): 1,
    ((1, 0), (0, 1)): 0,
    ((1, 0), (1, 0)): 0,
    ((1, 0), (1, 1)): 0,
    ((1, 1), (0, 0)): 0,
    ((1, 1), (0, 1)): 0,
    ((1, 1), (1, 0)): 0,
    ((1, 1), (1, 1)): 0,
}

curr_to_prev = {
    1: (
        ((0, 0), (0, 1)),
        ((0, 0), (1, 0)),
        ((0, 1), (0, 0)),
        ((1, 0), (0, 0)),
    ),
    0: (
        ((0, 0), (0, 0)),
        ((0, 0), (1, 1)),
        ((0, 1), (0, 1)),
        ((0, 1), (1, 0)),
        ((0, 1), (1, 1)),
        ((1, 0), (0, 1)),
        ((1, 0), (1, 0)),
        ((1, 0), (1, 1)),
        ((1, 1), (0, 0)),
        ((1, 1), (0, 1)),
        ((1, 1), (1, 0)),
        ((1, 1), (1, 1)),
    ),
}


def gen_column_preimages(column):
    last_matched_top = curr_to_prev[column[0]]
    for i in range(1, len(column)):
        matched_top = []
        for top in last_matched_top:
            for next_row in ((0, 0), (0, 1), (1, 0), (1, 1)):
                if prev_to_curr[(top[-1], next_row)] == column[i]:
                    matched_top.append(
                        top + (next_row,)
                    )  # magical comma at (next_row,) !!!
        last_matched_top = tuple(matched_top)

    return last_matched_top


def solution(g):
    last_preimages_count = {}

    for column in zip(*g):
        preimages_count = defaultdict(int)

        for preimage in gen_column_preimages(column):
            preimage_left, preimage_right = tuple(zip(*preimage))
            if not last_preimages_count:
                preimages_count[preimage_right] += 1
            else:
                preimages_count[preimage_right] += last_preimages_count[preimage_left]
        last_preimages_count = preimages_count

    return sum(last_preimages_count.values())


# solution([[False for _ in range(1)] for _ in range(3)])
print(
    solution(
        [
            [True],
            [False],
            [True],
        ]
    )
)
print(
    solution(
        [
            [True, False, True],
            [False, True, False],
            [True, False, True],
        ]
    )
)
print(
    solution(
        [
            [True, False, True, False, False, True, True, True],
            [True, False, True, False, False, False, True, False],
            [True, True, True, False, False, False, True, False],
            [True, False, True, False, False, False, True, False],
            [True, False, True, False, False, True, True, True],
        ]
    )
)
print(
    solution(
        [
            [True, True, False, True, False, True, False, True, True, False],
            [True, True, False, False, False, False, True, True, True, False],
            [True, True, False, False, False, False, False, False, False, True],
            [False, True, False, False, False, False, True, True, False, False],
        ]
    )
)
print(
    solution(
        [
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
        ]
    )
)
