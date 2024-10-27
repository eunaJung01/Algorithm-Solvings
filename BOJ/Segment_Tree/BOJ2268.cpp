#include <iostream>

using namespace std;

const int MAX_NUMBERS = 1000001;

long long A[MAX_NUMBERS];
long long tree[MAX_NUMBERS * 4];

long long sum(int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return 0;
    }
    if (left <= start && end <= right) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    long long left_sum = sum(node * 2, start, mid, left, right);
    long long right_sum = sum(node * 2 + 1, mid + 1, end, left, right);
    return left_sum + right_sum;
}

void modify(int node, int start, int end, int index, long long diff) {
    if (index < start || index > end) {
        return;
    }

    tree[node] += diff;
    if (start == end) {
        return;
    }

    int mid = (start + end) / 2;
    modify(node * 2, start, mid, index, diff);
    modify(node * 2 + 1, mid + 1, end, index, diff);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    int op, i;
    while (M--) {
        cin >> op;

        if (op == 0) {
            int j;
            cin >> i >> j;
            if (i > j) {
                swap(i, j);
            }

            cout << sum(1, 0, N - 1, i - 1, j - 1) << "\n";
            continue;
        }

        long long j;
        cin >> i >> j;

        long long diff = j - A[i - 1];
        A[i - 1] = j;
        modify(1, 0, N - 1, i - 1, diff);
    }
}
