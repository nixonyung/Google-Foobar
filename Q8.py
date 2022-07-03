from itertools import combinations


def solution(num_buns, num_required):
    ans = [[] for _ in range(num_buns)]
    num_key_copies = num_buns - num_required + 1

    for i, positions in enumerate(combinations(range(num_buns), num_required)):
        for position in positions:
            ans[position].append(i)

    return ans


ans = solution(2, 1)
print(ans)
ans = solution(4, 4)
print(ans)
ans = solution(5, 3)
print(ans)


# num_keys_per_bun, num_doors = xgcd(num_buns, num_buns - num_required + 1)
