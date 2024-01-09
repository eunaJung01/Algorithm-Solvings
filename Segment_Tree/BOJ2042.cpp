#include <iostream>

using namespace std;

long long *numbers = nullptr;
long long *tree = nullptr;

void init_tree(int node, int start, int end) {
    if (start == end) {
        tree[node] = numbers[start];
        return;
    }
    init_tree(2 * node, start, (start + end) / 2);
    init_tree(2 * node + 1, (start + end) / 2 + 1, end);
    tree[node] = tree[2 * node] + tree[2 * node + 1];
}

long long query(int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return 0;
    }
    if (left <= start && end <= right) {
        return tree[node];
    }
    long long leftSum = query(2 * node, start, (start + end) / 2, left, right);
    long long rightSum = query(2 * node + 1, (start + end) / 2 + 1, end, left, right);
    return leftSum + rightSum;
}

void update(int node, int start, int end, int index, long long difference) {
    if (index < start || index > end) {
        return;
    }
    tree[node] += difference;
    if (start != end) {
        update(2 * node, start, (start + end) / 2, index, difference);
        update(2 * node + 1, (start + end) / 2 + 1, end, index, difference);
    }
}

int N, M, K;

long long a, b, c;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M >> K;

    numbers = new long long[N];
    for (int i = 0; i < N; ++i) {
        cin >> numbers[i];
    }
    tree = new long long[4 * N];

    init_tree(1, 0, N - 1);

    int numberOfOperations = M + K;
    while (numberOfOperations--) {
        cin >> a >> b >> c;
        if (a == 1) {
            long long difference = c - numbers[b - 1];
            numbers[b - 1] = c;
            update(1, 0, N - 1, b - 1, difference);
            continue;
        }
        cout << query(1, 0, N - 1, b - 1, c - 1) << "\n";
    }
}
