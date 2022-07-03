# max flow
# refer to: https://cp-algorithms.com/graph/edmonds_karp.html#implementation
# added "for start in entrances"


def bfs(start, exits, path, N, adj):
    parents = [-1] * N
    parents[start] = -2
    queue = [(start, float("inf"))]

    while queue:
        cur, flow = queue.pop(0)
        for neighbor in adj[cur]:
            if parents[neighbor] == -1 and path[cur][neighbor] > 0:
                parents[neighbor] = cur
                new_flow = min(flow, path[cur][neighbor])
                if neighbor in exits:
                    return new_flow, neighbor, parents
                queue.append((neighbor, new_flow))

    return 0, None, parents


def solution(entrances, exits, path):
    N = len(path)
    adj = [[j for j in range(N) if path[i][j] > 0 or path[j][i] > 0] for i in range(N)]

    flow = 0

    for start in entrances:
        new_flow, end, parents = bfs(start, exits, path, N, adj)
        while new_flow:
            flow += new_flow

            cur = end
            while cur != start:
                prev = parents[cur]
                path[prev][cur] -= new_flow
                path[cur][prev] += new_flow
                cur = prev

            new_flow, end, parents = bfs(start, exits, path, N, adj)

    return flow


ans = solution(
    [0],
    [3],
    [
        [0, 7, 0, 0],
        [0, 0, 6, 0],
        [0, 0, 0, 8],
        [9, 0, 0, 0],
    ],
)
print(ans)

ans2 = solution(
    [0, 1],
    [4, 5],
    [
        [0, 0, 4, 6, 0, 0],
        [0, 0, 5, 2, 0, 0],
        [0, 0, 0, 0, 4, 4],
        [0, 0, 0, 0, 6, 6],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ],
)
print(ans2)
