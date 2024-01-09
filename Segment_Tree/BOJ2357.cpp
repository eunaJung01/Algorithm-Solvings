#include <iostream>
#include <climits>

using namespace std;

#define MAX_LEN 100001

struct Node {
    int min = 0;
    int max = 0;

    Node() = default;

    Node(int min, int max) : min(min), max(max) {}
};

int numbers[MAX_LEN];
Node tree[MAX_LEN * 4];

void init(int node, int start, int end) {
    if (start == end) {
        tree[node].min = numbers[start];
        tree[node].max = numbers[start];
        return;
    }

    int mid = (start + end) / 2;
    init(node * 2, start, mid);
    init(node * 2 + 1, mid + 1, end);

    tree[node].min = min(tree[node * 2].min, tree[node * 2 + 1].min);
    tree[node].max = max(tree[node * 2].max, tree[node * 2 + 1].max);
}

Node query(int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return {INT_MAX, INT_MIN};
    }
    if (left <= start && end <= right) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    Node left_node = query(node * 2, start, mid, left, right);
    Node right_node = query(node * 2 + 1, mid + 1, end, left, right);
    return {min(left_node.min, right_node.min), max(left_node.max, right_node.max)};
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

    int a, b;
    while (M--) {
        cin >> a >> b;
        if (b > N) {
            b = N;
        }
        Node node = query(1, 0, N - 1, a - 1, b - 1);
        cout << node.min << " " << node.max << "\n";
    }
}
