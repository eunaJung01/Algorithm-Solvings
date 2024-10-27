#include <iostream>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 1000001;

ll A[MAX_NUMBERS];

ll tree[MAX_NUMBERS * 4];
ll lazy[MAX_NUMBERS * 4];

void init(int node, int start, int end) {
    if (start == end) {
        tree[node] = A[start];
        return;
    }

    int mid = (start + end) / 2;
    init(node * 2, start, mid);
    init(node * 2 + 1, mid + 1, end);
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

void update_lazy(int node, int start, int end) {
    if (lazy[node] != 0) {
        tree[node] += (end - start + 1) * lazy[node];

        if (start != end) {
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }
        lazy[node] = 0;
    }
}

void update(int node, int start, int end, int left, int right, int diff) {
    update_lazy(node, start, end);

    if (left > end || right < start) {
        return;
    }
    if (left <= start && end <= right) {
        tree[node] += (end - start + 1) * diff;

        if (start != end) {
            lazy[node * 2] += diff;
            lazy[node * 2 + 1] += diff;
        }
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, left, right, diff);
    update(node * 2 + 1, mid + 1, end, left, right, diff);
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

ll query(int node, int start, int end, int idx) {
    update_lazy(node, start, end);

    if (start == end) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    if (idx <= mid) {
        return query(node * 2, start, mid, idx);
    }
    return query(node * 2 + 1, mid + 1, end, idx);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }
    init(1, 0, N - 1);

    int M;
    cin >> M;

    while (M--) {
        int flag, i, j, k, x;
        cin >> flag;

        if (flag == 1) {
            cin >> i >> j >> k;
            update(1, 0, N - 1, i - 1, j - 1, k);
            continue;
        }
        cin >> x;
        cout << query(1, 0, N - 1, x - 1) << "\n";
    }
}
