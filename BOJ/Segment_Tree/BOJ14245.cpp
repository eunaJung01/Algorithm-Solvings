#include <iostream>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 500000;

ll numbers[MAX_NUMBERS];

ll tree[MAX_NUMBERS * 4];
// inner nodes : space for lazy propagation
// leaf nodes  : store calculated numbers

void init(int node, int start, int end) {
    if (start == end) {
        tree[node] = numbers[start];
        return;
    }

    int mid = (start + end) / 2;
    init(node * 2, start, mid);
    init(node * 2 + 1, mid + 1, end);
}

void update_lazy(int node, int start, int end) {
    if (start == end || tree[node] == 0) {
        return;
    }

    tree[node * 2] ^= tree[node];
    tree[node * 2 + 1] ^= tree[node];
    tree[node] = 0;
}

void update(int node, int start, int end, int left, int right, int val) {
    update_lazy(node, start, end);

    if (left > end || right < start) {
        return;
    }

    if (start == end) {
        tree[node] ^= val;
        return;
    }

    if (left <= start && right >= end) {
        tree[node] = val;
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, left, right, val);
    update(node * 2 + 1, mid + 1, end, left, right, val);
}

ll query(int node, int start, int end, int i) {
    update_lazy(node, start, end);

    if (start == end) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    if (i <= mid) {
        return query(node * 2, start, mid, i);
    }
    return query(node * 2 + 1, mid + 1, end, i);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }
    init(1, 0, n - 1);

    int m;
    cin >> m;

    while (m--) {
        int t;
        cin >> t;

        if (t == 1) {
            int a, b, c;
            cin >> a >> b >> c;
            update(1, 0, n - 1, a, b, c);
            continue;
        }

        if (t == 2) {
            int a;
            cin >> a;
            cout << query(1, 0, n - 1, a) << "\n";
            continue;
        }
    }
}
