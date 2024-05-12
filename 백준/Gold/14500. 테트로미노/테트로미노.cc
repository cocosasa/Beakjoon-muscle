#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int map[500][500];

bool visited[500][500];
int dx[] = {0,0,-1,1};
int dy[] = {-1,1,0,0};

int ans = 0;


void dfs(int x, int y, int depth, int sum) {
    if (depth == 4) {
        ans = max(ans, sum) ;
        return;
    }

    for (int i =0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || nx >= N || ny < 0 || ny >= M || visited[nx][ny]) 
            continue;
        visited[nx][ny] = true;

        dfs(nx, ny, depth + 1, sum + map[nx][ny]);
        visited[nx][ny] = false;
    }
}

void checkAiuer(int x, int y) {
    int sum = 0;

    if (x >= 1 && y >= 1 && y < M - 1) {
        sum = map[x][y] + map[x - 1][y] + map[x][y - 1] + map[x][y + 1];
        ans = max(ans, sum);
    }
    if (x >= 1 && x < N - 1 && y < M - 1) {
        sum = map[x][y] + map[x - 1][y] + map[x + 1][y] + map[x][y + 1];
        ans = max(ans, sum);
    }
    if (x < N - 1 && y >= 1 && y < M - 1) {
        sum = map[x][y] + map[x + 1][y] + map[x][y - 1] + map[x][y + 1];
        ans = max(ans, sum);
    }
    if (x >= 1 && x < N - 1 && y >= 1) {
        sum = map[x][y] + map[x - 1][y] + map[x + 1][y] + map[x][y - 1];
        ans = max(ans, sum);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> map[i][j];
        }
    }

    for (int i = 0; i < N; i ++) {
        for (int j = 0; j < M; j++) {
            visited[i][j] = true;
            dfs(i, j, 1, map[i][j]);
            visited[i][j] = false;
            
            checkAiuer(i,j);
        }
    }
    
    cout << ans << endl;

    return 0;
}