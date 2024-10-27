#include <iostream>
#include <algorithm>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = (2000 * 1999) / 2 + 1;

pair<int, int> lines[MAX_NUMBERS];
int tree[MAX_NUMBERS * 4];

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

void update(int node, int left, int right, int idx) {
    if (idx < left || idx > right) {
        return;
    }

    tree[node] += 1;
    if (left == right) {
        return;
    }

    int mid = (left + right) / 2;
    update(node * 2, left, mid, idx);
    update(node * 2 + 1, mid + 1, right, idx);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    for (int idx = 0; idx < M; ++idx) {
        int i, j;
        cin >> i >> j;
        lines[idx] = {i, j};
    }
    sort(lines, lines + M);

    ll answer = 0;
    for (int idx = 0; idx < M; ++idx) {
        int j = lines[idx].second;
        answer += query(1, 1, N, j + 1, N);
        update(1, 1, N, j);
    }
    cout << answer;
}
