#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const pair<int, int> &p1, const pair<int, int> &p2) {
    return p1.first < p2.first;
}

vector<pair<int, int>> lines;
int lines_B_to_A[500001];

vector<int> dp;
int dpOfEachLine[100001];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        int a, b;
        cin >> a >> b;
        lines.emplace_back(a, b);
        lines_B_to_A[b] = a;
    }
    sort(lines.begin(), lines.end(), compare);

    dp.push_back(lines[0].second);
    dpOfEachLine[0] = dp.size() - 1;

    for (int i = 1; i < N; ++i) {
        int b = lines[i].second;
        if (b > dp.back()) {
            dp.push_back(b);
            dpOfEachLine[i] = dp.size() - 1;
            continue;
        }
        int idx = lower_bound(dp.begin(), dp.end(), b) - dp.begin();
        dp[idx] = b;
        dpOfEachLine[i] = idx;
    }
    cout << N - dp.size() << "\n";

    vector<int> notInDP;
    int d = dp.size() - 1;
    for (int i = N - 1; i >= 0; --i) {
        if (dpOfEachLine[i] == d) {
            d--;
            continue;
        }
        notInDP.push_back(lines_B_to_A[lines[i].second]);
    }

    sort(notInDP.begin(), notInDP.end());
    for (int a: notInDP) {
        cout << a << "\n";
    }
}
