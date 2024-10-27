#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <cstring>

using namespace std;

const vector<pair<int, int>> horse{
        {-1, -2},
        {-2, -1},
        {-2, 1},
        {-1, 2},
        {1,  -2},
        {2,  -1},
        {2,  1},
        {1,  2}
};

const vector<pair<int, int>> monkey{
        {-1, 0},
        {0,  -1},
        {1,  0},
        {0,  1}
};

struct Position {
    int y;
    int x;
    int numberOfHorse = 0;
};

int K, W, H;

int board[200][200];
int visited[200][200][31];

int BFS() {
    memset(visited, -1, sizeof(visited));

    queue<Position> queue;
    queue.push({0, 0, 0});
    visited[0][0][0] = 0;

    while (!queue.empty()) {
        Position pos = queue.front();
        queue.pop();

        if (pos.numberOfHorse < K) {
            for (pair<int, int> n: horse) {
                int ny = pos.y + n.first;
                int nx = pos.x + n.second;

                if (0 <= ny && ny < H && 0 <= nx && nx < W &&
                    board[ny][nx] == 0 && visited[ny][nx][pos.numberOfHorse + 1] == -1) {

                    visited[ny][nx][pos.numberOfHorse + 1] = visited[pos.y][pos.x][pos.numberOfHorse] + 1;
                    queue.push({ny, nx, pos.numberOfHorse + 1});
                }
            }
        }

        for (pair<int, int> n: monkey) {
            int ny = pos.y + n.first;
            int nx = pos.x + n.second;

            if (0 <= ny && ny < H && 0 <= nx && nx < W &&
                board[ny][nx] == 0 && visited[ny][nx][pos.numberOfHorse] == -1) {

                visited[ny][nx][pos.numberOfHorse] = visited[pos.y][pos.x][pos.numberOfHorse] + 1;
                queue.push({ny, nx, pos.numberOfHorse});
            }
        }
    }

    int answer = INT_MAX;
    for (int i = 0; i <= K; ++i) {
        if (visited[H - 1][W - 1][i] > -1) {
            answer = min(answer, visited[H - 1][W - 1][i]);
        }
    }

    if (answer != INT_MAX) {
        return answer;
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> K >> W >> H;
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            cin >> board[i][j];
        }
    }

    cout << BFS();
}
