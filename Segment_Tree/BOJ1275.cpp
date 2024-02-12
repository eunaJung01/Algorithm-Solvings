#include <iostream>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 100000;

ll numbers[MAX_NUMBERS];
ll tree[MAX_NUMBERS * 4];

void init(int node, int start, int end) {
    if (start == end) {
        tree[node] = numbers[start];
        return;
    }

    int mid = (start + end) / 2;
    init(node * 2, start, mid);
    init(node * 2 + 1, mid + 1, end);
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

void update(int node, int start, int end, int idx, ll diff) {
    if (idx < start || idx > end) {
        return;
    }

    tree[node] += diff;
    if (start == end) {
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, idx, diff);
    update(node * 2 + 1, mid + 1, end, idx, diff);
}

ll query(int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return 0;
    }

    if (left <= start && right >= end) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    ll left_query = query(node * 2, start, mid, left, right);
    ll right_query = query(node * 2 + 1, mid + 1, end, left, right);
    return left_query + right_query;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    for (int i = 0; i < N; ++i) {
        cin >> numbers[i];
    }
    init(1, 0, N - 1);

    while (Q--) {
        int x, y, a, b;
        cin >> x >> y >> a >> b;

        if (x > y) {
            swap(x, y);
        }
        cout << query(1, 0, N - 1, x - 1, y - 1) << "\n";

        ll diff = b - numbers[a - 1];
        numbers[a - 1] = b;
        update(1, 0, N - 1, a - 1, diff);
    }
}
