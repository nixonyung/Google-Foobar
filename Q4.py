def solution(map):
    queue = [(0, 0, 0, 1)]
    visited = []

    while queue:
        x, y, wallCount, moveCount = queue.pop(0)

        if (x < 0) or (x >= len(map[0])) or (y < 0) or (y >= len(map)):
            continue
        if wallCount > 1:
            continue
        if (x, y, wallCount) in visited:
            continue
        else:
            visited.append((x, y, wallCount))

        if (x == len(map[0]) - 1) and (y == len(map) - 1):
            return moveCount

        queue.extend(
            [
                (x + 1, y, wallCount + map[y][x], moveCount + 1),
                (x, y + 1, wallCount + map[y][x], moveCount + 1),
                (x - 1, y, wallCount + map[y][x], moveCount + 1),
                (x, y - 1, wallCount + map[y][x], moveCount + 1),
            ]
        )


print(
    solution(
        [
            [0, 1, 1, 0],
            [0, 0, 0, 1],
            [1, 1, 0, 0],
            [1, 1, 1, 0],
        ]
    )
)
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
        ]
    )
)
print(
    solution(
        [
            [0, 1],
            [1, 0],
        ]
    )
)
print(
    solution(
        [
            [0, 1, 0, 0],
        ]
    )
)
print(
    solution(
        [
            [0],
            [1],
            [0],
            [0],
        ]
    )
)
