from pprint import pprint

import numpy as np
from tqdm import tqdm

current = []
result_dict = {}


def one_of_four(input_list):
    return (
        (
            input_list[0]
            and not input_list[1]
            and not input_list[2]
            and not input_list[3]
        )
        or (
            not input_list[0]
            and input_list[1]
            and not input_list[2]
            and not input_list[3]
        )
        or (
            not input_list[0]
            and not input_list[1]
            and input_list[2]
            and not input_list[3]
        )
        or (
            not input_list[0]
            and not input_list[1]
            and not input_list[2]
            and input_list[3]
        )
    )


def transform(mask2d):
    new_height = len(mask2d) - 1
    new_width = len(mask2d[0]) - 1

    result = [[] for _ in range(new_height)]

    for i in range(new_height):
        for j in range(new_width):
            result[i].append(
                one_of_four(
                    (
                        mask2d[i][j],
                        mask2d[i][j + 1],
                        mask2d[i + 1][j],
                        mask2d[i + 1][j + 1],
                    )
                )
            )

    # debug
    # for i in range(len(result)):
    #     result[i] = tuple(result[i])
    # result = tuple(result)

    return result


def compare(mask, grid):
    width = len(grid[0]) + 1
    mask2d = [
        list(map(lambda x: bool(int(x)), mask[i : i + width]))
        for i in range(0, len(mask), width)
    ]

    # debug:
    # print(mask)
    # mask2d_debug = [["0" if el else "." for el in row] for row in mask2d]
    # mask2d_transform_debug = [
    #     ["0" if el else "." for el in row] for row in transform(mask2d)
    # ]
    # print(np.array(mask2d_debug))
    # print(np.array(mask2d_transform_debug))

    # debug:
    global result_dict
    key = "".join(
        "".join(["0" if el else "." for el in row]) for row in transform(mask2d)
    )
    if key in result_dict:
        result_dict[key] += 1
    else:
        result_dict[key] = 1

    return transform(mask2d) == grid


def solution(grid):
    previous_height = len(grid) + 1
    previous_width = len(grid[0]) + 1
    max_power = previous_width * previous_height
    # global current
    # current =
    global result_dict
    result_dict = {}
    ans = 0

    for i in tqdm(range(pow(2, previous_width * previous_height))):
        # for i in range(pow(2, previous_width * previous_height)):
        mask = f"{i:0{max_power}b}"
        ans += int(compare(mask, grid))

    print(f"{ans = }")
    result_dict_sorted = {
        k: v
        for k, v in sorted(result_dict.items(), key=lambda item: item[1], reverse=True)
    }
    pprint(result_dict_sorted, sort_dicts=False)


# solution([[False for _ in range(2)] for _ in range(2)])
solution([[False for _ in range(1)] for _ in range(3)])
# solution([[False for _ in range(4)] for _ in range(3)])
# solution([[True, False, True], [False, True, False], [True, False, True]])
# solution(
#     [
#         [True, False, True, False, False, True, True, True],
#         [True, False, True, False, False, False, True, False],
#         [True, True, True, False, False, False, True, False],
#         [True, False, True, False, False, False, True, False],
#         [True, False, True, False, False, True, True, True],
#     ]
# )
