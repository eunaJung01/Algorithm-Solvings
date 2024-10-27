#include <iostream>
#include <queue>

using namespace std;

int R, C;

const pair<int, int> d[4]{
        {-1, 0},
        {1,  0},
        {0,  1},
        {0,  -1}
};

char maze[1000][1000];

int visited_fires[1000][1000];
int visited_moves[1000][1000];

queue<pair<int, int>> fires;
queue<pair<int, int>> moves;

void BFS() {
    pair<int, int> init = moves.front();
    int start_y = init.first;
    int start_x = init.second;
    if (start_y == 0 || start_y == R - 1 || start_x == 0 || start_x == C - 1) {
        cout << 1;
        return;
    }

    while (!fires.empty()) {
        pair<int, int> pos = fires.front();
        int y = pos.first;
        int x = pos.second;
        fires.pop();

        for (int i = 0; i < 4; ++i) {
            int ny = y + d[i].first;
            int nx = x + d[i].second;

            if (ny < 0 || ny >= R || nx < 0 || nx >= C || maze[ny][nx] == '#' || visited_fires[ny][nx] > 0) {
                continue;
            }

            visited_fires[ny][nx] = visited_fires[y][x] + 1;
            fires.emplace(ny, nx);
        }
    }

    while (!moves.empty()) {
        pair<int, int> pos = moves.front();
        int y = pos.first;
        int x = pos.second;
        moves.pop();

        for (int i = 0; i < 4; ++i) {
            int ny = y + d[i].first;
            int nx = x + d[i].second;

            if (ny < 0 || ny >= R || nx < 0 || nx >= C || maze[ny][nx] == '#'
                || visited_moves[ny][nx] > 0
                || (visited_fires[ny][nx] > 0 && visited_fires[ny][nx] <= visited_moves[y][x] + 1)) {
                continue;
            }

            if (ny == 0 || ny == R - 1 || nx == 0 || nx == C - 1) {
                cout << visited_moves[y][x] + 1;
                return;
            }

            visited_moves[ny][nx] = visited_moves[y][x] + 1;
            moves.emplace(ny, nx);
        }
    }
    cout << "IMPOSSIBLE";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> R >> C;

    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            cin >> maze[i][j];

            if (maze[i][j] == 'F') {
                fires.emplace(i, j);
                visited_fires[i][j] = 1;
                continue;
            }
            if (maze[i][j] == 'J') {
                moves.emplace(i, j);
                visited_moves[i][j] = 1;
            }
        }
    }

    BFS();
}
