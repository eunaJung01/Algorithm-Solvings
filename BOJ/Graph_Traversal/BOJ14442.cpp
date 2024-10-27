#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <climits>

using namespace std;

int N, M, K;
int map[1000][1000];
int numberOfMoves[1000][1000][11];

struct Pos {
    int y;
    int x;
    int numberOfBrokenWalls;
};

const vector<pair<int, int>> d{
        {-1, 0}, {0, -1}, {0, 1}, {1, 0}
};

int BFS() {
    memset(numberOfMoves, -1, sizeof(numberOfMoves));

    queue<Pos> queue;
    queue.push({0, 0, 0});
    numberOfMoves[0][0][0] = 1;

    while (!queue.empty()) {
        Pos pos = queue.front();
        queue.pop();

        int y = pos.y;
        int x = pos.x;
        int numberOfBrokenWalls = pos.numberOfBrokenWalls;

        for (int i = 0; i < 4; ++i) {
            int ny = y + d[i].first;
            int nx = x + d[i].second;

            if (ny < 0 || ny >= N || nx < 0 || nx >= M) {
                continue;
            }

            if (numberOfBrokenWalls < K && map[ny][nx] == 1 &&
                (numberOfMoves[ny][nx][numberOfBrokenWalls + 1] == -1 ||
                 numberOfMoves[y][x][numberOfBrokenWalls] + 1 < numberOfMoves[ny][nx][numberOfBrokenWalls + 1])) {

                numberOfMoves[ny][nx][numberOfBrokenWalls + 1] = numberOfMoves[y][x][numberOfBrokenWalls] + 1;

                if (ny == N - 1 && nx == M - 1) {
                    continue;
                }
                queue.push({ny, nx, numberOfBrokenWalls + 1});
            }

            if (map[ny][nx] == 0 &&
                (numberOfMoves[ny][nx][numberOfBrokenWalls] == -1 ||
                 numberOfMoves[y][x][numberOfBrokenWalls] + 1 < numberOfMoves[ny][nx][numberOfBrokenWalls])) {

                numberOfMoves[ny][nx][numberOfBrokenWalls] = numberOfMoves[y][x][numberOfBrokenWalls] + 1;

                if (ny == N - 1 && nx == M - 1) {
                    continue;
                }
                queue.push({ny, nx, numberOfBrokenWalls});
            }
        }
    }

    int answer = INT_MAX;
    for (int i = 0; i <= K; ++i) {
        if (numberOfMoves[N - 1][M - 1][i] >= 0) {
            answer = min(answer, numberOfMoves[N - 1][M - 1][i]);
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

    cin >> N >> M >> K;

    for (int i = 0; i < N; ++i) {
        string line;
        cin >> line;
        for (int j = 0; j < M; ++j) {
            map[i][j] = line[j] - '0';
        }
    }

    cout << BFS();
}
