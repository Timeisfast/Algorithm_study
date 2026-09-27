import heapq

def solve():
    N = int(input())
    town = [list(map(int, input().split())) for _ in range(N)]
    
    battery = [[float('inf')] * N for _ in range(N)]
    battery[0][0] = 0
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    min_heap = []
    heapq.heappush(min_heap, [0, 0, 0])
    while min_heap:
        cur_battery, cur_x, cur_y = heapq.heappop(min_heap)
        
        if battery[cur_x][cur_y] < cur_battery:
            continue
        
        for i in range(4):
            nxt_x, nxt_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nxt_x < N and 0 <= nxt_y < N:
                bat = cur_battery + max(town[nxt_x][nxt_y] - town[cur_x][cur_y], 0) + 1
                if bat < battery[nxt_x][nxt_y]:
                    battery[nxt_x][nxt_y] = bat
                    heapq.heappush(min_heap, [bat, nxt_x, nxt_y])
    return battery[N - 1][N - 1]


T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")