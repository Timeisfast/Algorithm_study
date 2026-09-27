def solve():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [i for i in range(N + 1)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        
        if root_x != root_y:
            parent[root_x] = root_y
            return True
        return False
    
    for i in range(0, 2 * M, 2):
        union(arr[i], arr[i + 1])
    
    cnt = 0
    for i in range(1, N + 1):
        if parent[i] == i:
            cnt += 1
    return cnt


T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")