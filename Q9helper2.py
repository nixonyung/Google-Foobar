def one_of_four(cells):
    return cells in ("1000", "0100", "0010", "0001")


def check_valid_preimage(preimage, column):
    return (
        tuple(one_of_four(preimage[i * 2 : i * 2 + 4]) for i in range(len(column)))
        == column
    )


def solution(g):
    prev_valid_preimages_count = {}

    for column in zip(*g):
        # if column is k-by-1, then its preimages are (k+1)-by-2
        # let n = (k+1) * 2
        n = (len(column) + 1) * 2

        valid_preimages_count = {}
        # all_preimages = (f"{i:0{n}b}" for i in range(1 << n))  # python 3
        all_preimages = (bin(i)[2:].zfill(n) for i in range(1 << n))  # python 2
        for preimage in all_preimages:
            if check_valid_preimage(preimage, column):
                print(preimage)
                if not prev_valid_preimages_count:
                    valid_preimages_count[preimage] = 1
                else:
                    valid_preimages_count[preimage] = sum(
                        prev_valid_preimages_count[prev_preimage]
                        if preimage[::2] == prev_preimage[1::2]
                        else 0
                        for prev_preimage in prev_valid_preimages_count
                    )

        prev_valid_preimages_count = valid_preimages_count

    return sum(prev_valid_preimages_count.values())


# solution([[False for _ in range(1)] for _ in range(3)])
solution(
    [
        [True],
        [False],
        [True],
    ]
)
# print(
#     solution(
#         [
#             [True, False, True],
#             [False, True, False],
#             [True, False, True],
#         ]
#     )
# )
# print(
#     solution(
#         [
#             [True, False, True, False, False, True, True, True],
#             [True, False, True, False, False, False, True, False],
#             [True, True, True, False, False, False, True, False],
#             [True, False, True, False, False, False, True, False],
#             [True, False, True, False, False, True, True, True],
#         ]
#     )
# )
# print(
#     solution(
#         [
#             [True, True, False, True, False, True, False, True, True, False],
#             [True, True, False, False, False, False, True, True, True, False],
#             [True, True, False, False, False, False, False, False, False, True],
#             [False, True, False, False, False, False, True, True, False, False],
#         ]
#     )
# )
# print(
#     solution(
#         [
#             [True, True, True, True, True, True, True, True, True, True],
#             [True, True, True, True, True, True, True, True, True, True],
#             [True, True, True, True, True, True, True, True, True, True],
#             [True, True, True, True, True, True, True, True, True, True],
#             [True, True, True, True, True, True, True, True, True, True],
#             [True, True, True, True, True, True, True, True, True, True],
#             [True, True, True, True, True, True, True, True, True, True],
#             [True, True, True, True, True, True, True, True, True, True],
#         ]
#     )
# )
