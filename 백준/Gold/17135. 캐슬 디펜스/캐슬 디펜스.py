from collections import deque

def bfs_shot(si,sj) :
    visited = [[0] * M for _ in range(si+1)] 
    queue = deque()
    queue.append((si,sj))
    visited[si][sj] = 1
    for z in range(D) :
        for k in range(len(queue)) :
            i, j = queue.popleft()
            if enemy[i][j] == 1 :
                return i,j
            for di, dj in d :
                ni , nj = i + di, j + dj
                if 0<= ni and 0<= nj < M and visited[ni][nj] == 0 :
                    queue.append((ni,nj))
                    visited[ni][nj] = 1
    return None, None

# 오답임
N, M, D = map(int,input().split())

enemy = [list(map(int,input().split())) for _ in range(N)]
total_enemy = sum(sum(enemy[i]) for i in range(N))

max_kill = 0

d = ((0,-1),(-1,0),(0,1))

for archer1 in range(M-2) :
    for archer2 in range(archer1+1, M-1) :
        for archer3 in range(archer2+1, M) :
            # 모든 조합
            kill = 0
            # 궁수의 y위치
            total_dead = []
            for position_y in range(N-1, -1, -1) :
                dead = []
                # 궁수의 x위치
                for position_x in (archer1, archer2, archer3) :
                    # bfs
                    shot_y, shot_x = bfs_shot(position_y,position_x)
                    
                    if shot_x != None :
                        dead.append((shot_y,shot_x))
                
                # 죽이기
                for dead_y, dead_x in dead :
                    total_dead.append((dead_y, dead_x))
                    if enemy[dead_y][dead_x] == 1 :
                        enemy[dead_y][dead_x] = 0
                        kill += 1
                        total_enemy -= 1
                
                # 적이 남았는지 체크
                total_enemy -= sum(enemy[position_y])
                if total_enemy == 0:
                    break
            # 되돌려버리기
            for dead_y, dead_x in total_dead :
                enemy[dead_y][dead_x] = 1
            # 최대값 갱신
            if max_kill < kill :
                max_kill = kill
print(max_kill)


# 궁수의 위치에서 3방향 bfs 순회하면서 적을 만나면 좌표 return
# 모든 궁수를 순회하고 나면 그 자리에 있는 적 삭제 & cnt += 1 & total_enemy -= 1
# 성에 도달한 적 수 계산해서 마이너스
# 적이 남아있는지 체크
# 남아 있으면 궁수의 y위치 - 1