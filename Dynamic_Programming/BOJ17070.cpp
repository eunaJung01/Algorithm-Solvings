#include <iostream>
#include <vector>

using namespace std;

int N;
int home[17][17];
int dp[17][17][3]; // 가로, 대각선, 세로

vector<pair<int, int>> d{
        {0, 1},
        {1, 1},
        {1, 0}
};

vector<vector<int>> directions{
        {0, 1},
        {0, 1, 2},
        {1, 2}
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> home[i][j];
        }
    }

    dp[0][1][0] = 1;
    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            if (home[y][x] == 1) {
                continue;
            }
            for (int previousDirection = 0; previousDirection < 3; previousDirection++) {
                for (int nextDirection: directions[previousDirection]) {
                    int ny = y - d[nextDirection].first;
                    int nx = x - d[nextDirection].second;

                    if (ny >= 0 && ny < N && nx >= 0 && nx < N) {
                        if (nextDirection == 1 && (home[y - 1][x] == 1 || home[y][x - 1] == 1)) {
                            continue;
                        }
                        dp[y][x][nextDirection] += dp[ny][nx][previousDirection];
                    }
                }
            }
        }
    }
    cout << dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2];
}
