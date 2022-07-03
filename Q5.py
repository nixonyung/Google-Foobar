def helper(n, firstStep):
    if results[n][firstStep] is not None:
        return results[n][firstStep]

    if firstStep > n:
        result = 0
    elif n == firstStep:
        result = 1
    elif n == 2 and firstStep == 1:
        result = 0
    else:
        result = sum(
            helper(n - firstStep, nextStep) for nextStep in range(1, firstStep)
        )

    results[n][firstStep] = result
    return result


def solution(n):
    global results
    results = [[None for _ in range(201)] for _ in range(201)]

    return sum(helper(n, fs) for fs in range(1, n))


print(solution(3))
print(solution(200))

print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
