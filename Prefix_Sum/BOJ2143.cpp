#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 1000;

ll A[MAX_NUMBERS];
ll B[MAX_NUMBERS];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    int m;
    cin >> m;
    for (int i = 0; i < m; ++i) {
        cin >> B[i];
    }

    vector<ll> sumsOfA;
    for (int i = 0; i < n; ++i) {
        ll sum = A[i];
        sumsOfA.push_back(sum);

        for (int j = i + 1; j < n; ++j) {
            sum += A[j];
            sumsOfA.push_back(sum);
        }
    }

    vector<ll> sumsOfB;
    for (int i = 0; i < m; ++i) {
        ll sum = B[i];
        sumsOfB.push_back(sum);

        for (int j = i + 1; j < m; ++j) {
            sum += B[j];
            sumsOfB.push_back(sum);
        }
    }

    sort(sumsOfA.begin(), sumsOfA.end());

    ll answer = 0;
    for (ll sumOfB: sumsOfB) {
        ll target = T - sumOfB;
        int lo = lower_bound(sumsOfA.begin(), sumsOfA.end(), target) - sumsOfA.begin();
        int hi = upper_bound(sumsOfA.begin(), sumsOfA.end(), target) - sumsOfA.begin();
        answer += (hi - lo);
    }

    cout << answer;
}
