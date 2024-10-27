#include <iostream>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 1000001;

ll numbers[MAX_NUMBERS];
ll tree[MAX_NUMBERS];

int N, M, K;

void update(int idx, ll diff) {
    while (idx <= N) {
        tree[idx] += diff;
        idx += (idx & -idx);
    }
}

ll sum(int idx) {
    ll answer = 0;
    while (idx > 0) {
        answer += tree[idx];
        idx -= (idx & -idx);
    }
    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M >> K;

    for (int i = 1; i <= N; ++i) {
        cin >> numbers[i];
        update(i, numbers[i]);
    }

    int numberOfOperations = M + K;
    while (numberOfOperations--) {
        int a;
        cin >> a;

        if (a == 1) {
            int b;
            ll c;
            cin >> b >> c;

            ll diff = c - numbers[b];
            numbers[b] = c;
            update(b, diff);
            continue;
        }

        int b, c;
        cin >> b >> c;
        cout << sum(c) - sum(b - 1) << "\n";
    }
}
