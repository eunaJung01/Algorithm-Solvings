#include <iostream>
#include <climits>

#define MAX 501

using namespace std;

int sum[MAX];
int dp[MAX][MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int K;
        cin >> K;

        for (int i = 1; i < K + 1; ++i) {
            int file;
            cin >> file;
            sum[i] = sum[i - 1] + file;
        }

        for (int sub = 1; sub < K; ++sub) {
            for (int i = 1; i + sub < K + 1; ++i) {
                int j = i + sub;

                dp[i][j] = INT_MAX;
                for (int k = i; k < j; ++k) {
                    dp[i][j] = min(dp[i][j],
                                   dp[i][k] + dp[k + 1][j] + sum[j] - sum[i - 1]);
                }
            }
        }
        cout << dp[1][K] << "\n";
    }
}
