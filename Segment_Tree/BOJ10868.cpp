#include <iostream>
#include <climits>

using namespace std;

#define MAX_NUMBERS 100000

int numbers[MAX_NUMBERS];
int tree[MAX_NUMBERS * 4];

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

int query(int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return INT_MAX;
    }
    if (left <= start && end <= right) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    int left_min = query(node * 2, start, mid, left, right);
    int right_min = query(node * 2 + 1, mid + 1, end, left, right);
    return min(left_min, right_min);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; ++i) {
        cin >> numbers[i];
    }
    init(1, 0, N - 1);

    while (M--) {
        int a, b;
        cin >> a >> b;
        cout << query(1, 0, N - 1, a - 1, b - 1) << "\n";
    }
}
