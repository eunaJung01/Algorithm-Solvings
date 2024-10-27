#include <iostream>

using namespace std;

const int MAX_NUMBERS = 100001;

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
    tree[node] = tree[node * 2] * tree[node * 2 + 1];
}

int query(int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return 1;
    }
    if (left <= start && right >= end) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    int left_mul = query(node * 2, start, mid, left, right);
    int right_mul = query(node * 2 + 1, mid + 1, end, left, right);
    return left_mul * right_mul;
}

void update(int node, int start, int end, int idx) {
    if (start == idx && end == idx) {
        tree[node] = numbers[idx];
        return;
    }
    if (idx < start || idx > end) {
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, idx);
    update(node * 2 + 1, mid + 1, end, idx);
    tree[node] = tree[node * 2] * tree[node * 2 + 1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    while (cin >> N >> K) {

        for (int i = 0; i < N; ++i) {
            cin >> numbers[i];
            if (numbers[i] > 0) {
                numbers[i] = 1;
            } else if (numbers[i] < 0) {
                numbers[i] = -1;
            } else {
                numbers[i] = 0;
            }
        }

        init(1, 0, N - 1);

        while (K--) {
            char op;
            cin >> op;

            if (op == 'C') {
                int i, V;
                cin >> i >> V;

                numbers[i - 1] = V;
                if (numbers[i - 1] > 0) {
                    numbers[i - 1] = 1;
                } else if (numbers[i - 1] < 0) {
                    numbers[i - 1] = -1;
                } else {
                    numbers[i - 1] = 0;
                }

                update(1, 0, N - 1, i - 1);
                continue;
            }

            int i, j;
            cin >> i >> j;

            int answer = query(1, 0, N - 1, i - 1, j - 1);
            if (answer > 0) {
                cout << "+";
            } else if (answer < 0) {
                cout << "-";
            } else {
                cout << "0";
            }
        }
        cout << "\n";
    }
}
