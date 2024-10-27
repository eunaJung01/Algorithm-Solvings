#include <iostream>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 1000001;

ll numbers[MAX_NUMBERS];

ll tree[MAX_NUMBERS * 4];
ll lazy[MAX_NUMBERS * 4];

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

void update(int node, int start, int end, int left, int right, ll diff) {
    update_lazy(node, start, end);

    if (left > end || right < start) {
        return;
    }

    if (left <= start && right >= end) {
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

ll query(int node, int start, int end, int left, int right) {
    update_lazy(node, start, end);

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

    int N, M, K;
    cin >> N >> M >> K;

    for (int i = 0; i < N; ++i) {
        cin >> numbers[i];
    }
    init(1, 0, N - 1);

    for (int i = 0; i < M + K; ++i) {
        int a, b, c;
        ll d;

        cin >> a;
        if (a == 1) {
            cin >> b >> c >> d;
            update(1, 0, N - 1, b - 1, c - 1, d);
            continue;
        }
        cin >> b >> c;
        cout << query(1, 0, N - 1, b - 1, c - 1) << "\n";
    }
}
