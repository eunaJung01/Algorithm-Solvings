#include <iostream>

using namespace std;
using ll = long long;

const int MOD = 1000000007;

ll power(ll n, ll exp) {
    ll result = 1;
    while (exp) {
        if (exp & 1) {
            result = (result * n) % MOD;
        }
        exp /= 2;
        n = (n * n) % MOD;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M;
    cin >> M;

    ll answer = 0;
    for (int i = 0; i < M; ++i) {
        ll n, s;
        cin >> n >> s;

        answer += (s * power(n, MOD - 2)) % MOD;
    }
    cout << answer % MOD;
}
