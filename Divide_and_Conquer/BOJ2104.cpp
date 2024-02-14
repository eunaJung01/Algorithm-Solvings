#include <iostream>
#include <climits>
#include <algorithm>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 100000;

struct Node {
    ll sum;
    ll minimum;
    int idxOfMinimum;
};

int N;

ll numbers[MAX_NUMBERS];
Node tree[MAX_NUMBERS * 4];

void init(int node, int start, int end) {
    if (start == end) {
        tree[node] = {numbers[start], numbers[start], start};
        return;
    }

    int mid = (start + end) / 2;
    init(node * 2, start, mid);
    init(node * 2 + 1, mid + 1, end);

    tree[node].sum = tree[node * 2].sum + tree[node * 2 + 1].sum;
    tree[node].minimum = min(tree[node * 2].minimum, tree[node * 2 + 1].minimum);

    if (tree[node].minimum == tree[node * 2].minimum) {
        tree[node].idxOfMinimum = tree[node * 2].idxOfMinimum;
    } else {
        tree[node].idxOfMinimum = tree[node * 2 + 1].idxOfMinimum;
    }
}

Node query(int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return {0, INT_MAX};
    }

    if (left <= start && end <= right) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    Node left_query = query(node * 2, start, mid, left, right);
    Node right_query = query(node * 2 + 1, mid + 1, end, left, right);

    Node q{};
    q.sum = left_query.sum + right_query.sum;
    q.minimum = min(left_query.minimum, right_query.minimum);

    if (q.minimum == left_query.minimum) {
        q.idxOfMinimum = left_query.idxOfMinimum;
    } else {
        q.idxOfMinimum = right_query.idxOfMinimum;
    }

    return q;
}

ll findMaxScore(int start, int end) {
    if (start > end) {
        return 0;
    }

    Node q = query(1, 0, N - 1, start, end);
    int idx = q.idxOfMinimum;

    if (idx < start || idx > end) {
        return 0;
    }

    ll maxScore = max(findMaxScore(start, idx - 1), findMaxScore(idx + 1, end));
    return max(maxScore, q.sum * q.minimum);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> numbers[i];
    }
    init(1, 0, N - 1);

    cout << findMaxScore(0, N - 1);
}
