def solution(xs):
    # if len(xs) == 1:
    #     return str(xs[0])
    if xs == [0] * len(xs):
        return "0"

    result = 1
    negativeNums = []
    for num in xs:
        if num > 1:
            result *= num
        elif num < 0:
            negativeNums.append(num)
    negativeNums.sort()
    for negativeNum in negativeNums[: len(negativeNums) // 2 * 2]:
        result *= negativeNum

    if result == 1:
        try:
            xs.index(result)
        except:
            return str(max(xs))

    return str(result)


print(solution([0, 0, 0]))
print(solution([0, 0, 1]))
print(solution([0, 0, -1]))
print(solution([-1]))
print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))
print(solution([-2, -3, 4, -5, -6]))
