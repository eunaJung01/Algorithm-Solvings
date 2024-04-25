#include <iostream>

using namespace std;

const int MAX_NUMBERS = 500000;

int tree[MAX_NUMBERS * 4];
int lazy[MAX_NUMBERS * 4];

void updateLazy(int node, int start, int end) {
    if (lazy[node] == 0) {
        return;
    }

    if ((end - start + 1) % 2) {
        tree[node] ^= lazy[node];
    }

    if (start == end) {
        lazy[node] = 0;
        return;
    }

    lazy[node * 2] ^= lazy[node];
    lazy[node * 2 + 1] ^= lazy[node];
    lazy[node] = 0;
}

void update(int node, int start, int end, int first, int last, int value) {
    updateLazy(node, start, end);

    if (first > end || last < start) {
        return;
    }

    if (first <= start && end <= last) {
        if ((end - start + 1) % 2) {
            tree[node] ^= value;
        }
        if (start == end) {
            return;
        }
        lazy[node * 2] ^= value;
        lazy[node * 2 + 1] ^= value;
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, first, last, value);
    update(node * 2 + 1, mid + 1, end, first, last, value);
    tree[node] = tree[node * 2] ^ tree[node * 2 + 1];
}

int query(int node, int start, int end, int first, int last) {
    updateLazy(node, start, end);

    if (first > end || last < start) {
        return 0;
    }

    if (first <= start && end <= last) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    int left_query = query(node * 2, start, mid, first, last);
    int right_query = query(node * 2 + 1, mid + 1, end, first, last);
    return left_query ^ right_query;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        int number;
        cin >> number;
        update(1, 0, N - 1, i, i, number);
    }

    int M;
    cin >> M;

    int n, i, j, k;
    while (M--) {
        cin >> n;

        if (n == 1) {
            cin >> i >> j >> k;
            update(1, 0, N - 1, i, j, k);
            continue;
        }
        if (n == 2) {
            cin >> i >> j;
            cout << query(1, 0, N - 1, i, j) << "\n";
        }
    }
}
