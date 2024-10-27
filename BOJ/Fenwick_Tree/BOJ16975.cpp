#include <iostream>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 1000001;

ll A[MAX_NUMBERS];
ll tree[MAX_NUMBERS];

int N;

void update(int idx, ll diff) {
    while (idx <= N) {
        tree[idx] += diff;
        idx += (idx & -idx);
    }
}

ll query(int idx) {
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

    cin >> N;

    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
        update(i, A[i] - A[i - 1]);
    }

    int M;
    cin >> M;

    while (M--) {
        int flag, i, j, k, x;
        cin >> flag;

        if (flag == 1) {
            cin >> i >> j >> k;
            update(i, k);
            update(j + 1, -k);
            continue;
        }
        cin >> x;
        cout << query(x) << "\n";
    }
}
