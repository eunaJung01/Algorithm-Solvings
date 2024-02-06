#include <iostream>
#include <vector>
#include <climits>

using namespace std;

using ll = long long;

ll A[1000001];
int DP_A[1000001];

vector<ll> DP;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    DP.push_back(INT_MIN);

    for (int i = 0; i < N; ++i) {
        ll a;
        cin >> a;
        A[i] = a;

        if (DP.size() == 0 || a > DP.back()) {
            DP.push_back(a);
            DP_A[i] = DP.size() - 1;
            continue;
        }

        int dp = lower_bound(DP.begin(), DP.end(), a) - DP.begin();
        DP[dp] = a;
        DP_A[i] = dp;
    }

    int dp = DP.size() - 1;
    ll a = DP[dp];

    int max_i = N - 1;
    while (max_i >= 0) {
        if (A[max_i] == a) {
            break;
        }
        max_i--;
    }

    vector<ll> answer;
    answer.push_back(a);

    for (int i = max_i; i >= 0; --i) {
        if (A[i] < a && DP_A[i] == dp - 1) {
            a = A[i];
            dp = DP_A[i];
            answer.push_back(a);
        }
    }

    cout << DP.size() - 1 << "\n";
    for (int i = answer.size() - 1; i >= 0; --i) {
        cout << answer[i] << " ";
    }
}
