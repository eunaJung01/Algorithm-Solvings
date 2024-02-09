#include <iostream>
#include <vector>

using namespace std;

vector<int> dp;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    dp.push_back(0);

    for (int i = 0; i < N; ++i) {
        int a;
        cin >> a;

        if (a > dp.back()) {
            dp.push_back(a);
            continue;
        }

        int idx = lower_bound(dp.begin(), dp.end(), a) - dp.begin();
        dp[idx] = a;
    }

    cout << dp.size() - 1;
}
