#include <iostream>
#include <climits>

using namespace std;

const int MAX_NUMBER = 100001;

struct Node {
    int idx = 0;
    int value = INT_MAX;
};

Node tree[MAX_NUMBER * 4];

void update(int node, int start, int end, int idx, int value) {
    if (idx < start || idx > end) {
        return;
    }

    if (start == end) {
        tree[node].idx = idx;
        tree[node].value = value;
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, idx, value);
    update(node * 2 + 1, mid + 1, end, idx, value);

    Node leftNode = tree[node * 2];
    Node rightNode = tree[node * 2 + 1];

    if (leftNode.value < rightNode.value) {
        tree[node].idx = leftNode.idx;
        tree[node].value = leftNode.value;
        return;
    }
    if (leftNode.value == rightNode.value) {
        if (leftNode.idx < rightNode.idx) {
            tree[node].idx = leftNode.idx;
            tree[node].value = leftNode.value;
            return;
        }
        tree[node].idx = rightNode.idx;
        tree[node].value = rightNode.value;
        return;
    }
    tree[node].idx = rightNode.idx;
    tree[node].value = rightNode.value;
}

Node query(int node, int start, int end, int first, int last) {
    if (first > end || last < start) {
        Node dummy;
        return dummy;
    }

    if (first <= start && end <= last) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    Node leftNode = query(node * 2, start, mid, first, last);
    Node rightNode = query(node * 2 + 1, mid + 1, end, first, last);

    if (leftNode.value < rightNode.value) {
        return leftNode;
    }
    if (leftNode.value == rightNode.value) {
        if (leftNode.idx < rightNode.idx) {
            return leftNode;
        }
    }
    return rightNode;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 1; i <= N; ++i) {
        int n;
        cin >> n;
        update(1, 1, N, i, n);
    }

    int M;
    cin >> M;

    while (M--) {
        int op;
        cin >> op;

        if (op == 1) {
            int i, v;
            cin >> i >> v;
            update(1, 1, N, i, v);

        } else if (op == 2) {
            int i, j;
            cin >> i >> j;
            cout << query(1, 1, N, i, j).idx << "\n";
        }
    }
}
