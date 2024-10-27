#include <iostream>

using namespace std;

const int MAX_NUMBERS = 1000000;

int N, M;
int tree[MAX_NUMBERS * 4];

void update(int node, int start, int end, int idx, int light) {
    if (idx < start || idx > end) {
        return;
    }

    if (start == end) {
        tree[node] = light;
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, idx, light);
    update(node * 2 + 1, mid + 1, end, idx, light);
    tree[node] = max(tree[node * 2], tree[node * 2 + 1]);
}

int query(int node, int start, int end, int first, int last) {
    if (first > end || last < start) {
        return 0;
    }

    if (first <= start && end <= last) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    return max(query(node * 2, start, mid, first, last),
               query(node * 2 + 1, mid + 1, end, first, last));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;

    for (int i = 0; i < N; ++i) {
        int light;
        cin >> light;
        update(1, 0, N - 1, i, light);
    }

    for (int i = M - 1; i < N - M + 1; ++i) {
        int start = i - M + 1;
        int end = i + M - 1;
        cout << query(1, 0, N - 1, start, end) << " ";
    }
}
