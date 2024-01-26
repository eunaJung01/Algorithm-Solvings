#include <iostream>
#include <algorithm>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 500005;

pair<ll, int> A[MAX_NUMBERS];
ll tree[MAX_NUMBERS * 4];

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

void update(int node, int start, int end, int idx) {
    if (start == end) {
        tree[node] = 1;
        return;
    }
    if (idx < start || idx > end) {
        return;
    }

    int mid = (start + end) / 2;
    if (idx <= mid) {
        update(node * 2, start, mid, idx);
    } else {
        update(node * 2 + 1, mid + 1, end, idx);
    }
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        ll a;
        cin >> a;
        A[i] = {a, i};
    }
    sort(A, A + N);

    ll answer = 0;
    for (int i = 0; i < N; ++i) {
        int idx = A[i].second;
        answer += query(1, 0, N - 1, idx + 1, N - 1);
        update(1, 0, N - 1, idx);
    }
    cout << answer;
}
