#include <iostream>

#define MAX_NUMBERS 1000001
#define MOD 1000000007

using namespace std;

long long numbers[MAX_NUMBERS];
long long tree[MAX_NUMBERS * 4];

void init(int node, int start, int end) {
    if (start == end) {
        tree[node] = numbers[start] % MOD;
        return;
    }

    int mid = (start + end) / 2;
    init(node * 2, start, mid);
    init(node * 2 + 1, mid + 1, end);

    tree[node] = ((tree[node * 2] % MOD) * (tree[node * 2 + 1] % MOD)) % MOD;
}

void update(int node, int start, int end, int index, int value) {
    if (index < start || index > end) {
        return;
    }
    if (start == end) {
        tree[node] = value;
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, index, value);
    update(node * 2 + 1, mid + 1, end, index, value);

    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD;
}

long long query(int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return 1;
    }
    if (left <= start && right >= end) {
        return tree[node] % MOD;
    }

    int mid = (start + end) / 2;
    long long left_mul = query(node * 2, start, mid, left, right) % MOD;
    long long right_mul = query(node * 2 + 1, mid + 1, end, left, right) % MOD;
    return (left_mul * right_mul) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, K;
    cin >> N >> M >> K;

    for (int i = 0; i < N; ++i) {
        cin >> numbers[i];
    }

    init(1, 0, N - 1);

    for (int i = 0; i < M + K; ++i) {
        int a, b, c;
        cin >> a >> b >> c;

        if (a == 1) {
            update(1, 0, N - 1, b - 1, c);
            continue;
        }
        cout << query(1, 0, N - 1, b - 1, c - 1) << "\n";
    }
}
