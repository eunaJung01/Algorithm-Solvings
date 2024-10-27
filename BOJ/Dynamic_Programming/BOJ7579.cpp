#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct App {
    int memory;
    int cost;
};

vector<App> apps;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; ++i) {
        int memory = 0;
        cin >> memory;
        apps.push_back({memory, 0});
    }

    int sumOfCosts = 0;
    for (int i = 0; i < N; ++i) {
        int cost = 0;
        cin >> cost;
        apps[i].cost = cost;

        sumOfCosts += cost;
    }

    int dp[sumOfCosts + 1];  // idx : cost, value : maximum memory
    fill(dp, dp + sumOfCosts + 1, 0);

    for (int i = 0; i < N; ++i) {
        for (int cost = sumOfCosts; cost >= apps[i].cost; --cost) {
            dp[cost] = max(dp[cost], dp[cost - apps[i].cost] + apps[i].memory);
        }
    }

    int result = 0;
    while (dp[result] < M) {
        result++;
    }
    cout << result;
}
