from collections import deque

def solve():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N + 1)]
    incomes = [0 for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a].append(b)
        incomes[b] += 1
    
    q = deque()
    for i in range(1, N + 1):
        if incomes[i] == 0:
            q.append(i)
    
    ans = []
    while q:
        cur = q.popleft()
        ans.append(str(cur))
        
        for e in edges[cur]:
            incomes[e] -= 1
            if incomes[e] == 0:
                q.append(e)
    return " ".join(ans)


T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")