def solution(l, t):
    for startIdx in range(len(l)):
        row = [sum(l[startIdx : i + 1]) for i in range(len(l))]

        try:
            foundIdx = row.index(t)
            return [startIdx, foundIdx]
        except ValueError:
            pass

    return [-1, -1]


print(solution([4, 3, 10, 2, 8], 12))
