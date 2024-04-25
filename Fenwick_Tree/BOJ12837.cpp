#include <iostream>

using namespace std;

using ll = long long;

const int MAX_NUMBERS = 1000001;

int N, Q;

ll tree[MAX_NUMBERS];

void update(int idx, int value) {
    while (idx <= N) {
        tree[idx] += value;
        idx += (idx & -idx);
    }
}

ll query(int idx) {
    ll result = 0;
    while (idx > 0) {
        result += tree[idx];
        idx -= (idx & -idx);
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> Q;

    while (Q--) {
        int i;
        cin >> i;

        if (i == 1) {
            int p, x;
            cin >> p >> x;
            update(p, x);
            continue;
        }

        if (i == 2) {
            int p, q;
            cin >> p >> q;
            cout << query(q) - query(p - 1) << "\n";
        }
    }
}
