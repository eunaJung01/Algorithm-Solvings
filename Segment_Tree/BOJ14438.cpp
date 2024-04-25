#include <iostream>
#include <climits>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 100001;

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
    tree[node] = min(tree[node * 2], tree[node * 2 + 1]);
}

void update(int node, int start, int end, int updatedIdx) {
    if (updatedIdx < start || updatedIdx > end) {
        return;
    }

    if (start == end) {
        tree[node] = numbers[updatedIdx];
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, updatedIdx);
    update(node * 2 + 1, mid + 1, end, updatedIdx);
    tree[node] = min(tree[node * 2], tree[node * 2 + 1]);
}

ll query(int node, int start, int end, int first, int last) {
    if (first > end || start > last) {
        return INT_MAX;
    }

    if (first <= start && end <= last) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    ll left_query = query(node * 2, start, mid, first, last);
    ll right_query = query(node * 2 + 1, mid + 1, end, first, last);
    return min(left_query, right_query);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 1; i <= N; ++i) {
        cin >> numbers[i];
    }

    init(1, 1, N);

    int M;
    cin >> M;

    for (int k = 0; k < M; ++k) {
        int n;
        cin >> n;

        if (n == 1) {
            int i;
            ll v;

            cin >> i >> v;
            numbers[i] = v;
            update(1, 1, N, i);
            continue;
        }

        if (n == 2) {
            int i, j;

            cin >> i >> j;
            cout << query(1, 1, N, i, j) << "\n";
        }
    }
}
