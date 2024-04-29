#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define all(v) v.begin(), v.end()

const int MAX_NUMBERS = 100001;

vector<int> tree[MAX_NUMBERS * 4];

void update(int node, int start, int end, int idx, int value) {
    if (idx < start || idx > end) {
        return;
    }

    tree[node].push_back(value);
    if (start == end) {
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, idx, value);
    update(node * 2 + 1, mid + 1, end, idx, value);
}

int query(int node, int start, int end, int first, int last, int k) {
    if (first > end || last < start) {
        return 0;
    }

    if (first <= start && end <= last) {
        return tree[node].end() - upper_bound(all(tree[node]), k);
    }

    int mid = (start + end) / 2;
    return query(node * 2, start, mid, first, last, k) +
           query(node * 2 + 1, mid + 1, end, first, last, k);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int number;
    for (int i = 0; i < N; ++i) {
        cin >> number;
        update(1, 0, N - 1, i, number);
    }

    for (auto &i: tree) {
        sort(all(i));
    }

    int M;
    cin >> M;

    int i, j, k;
    int lastAnswer = 0;
    for (int l = 0; l < M; ++l) {
        cin >> i >> j >> k;

        i ^= lastAnswer;
        j ^= lastAnswer;
        k ^= lastAnswer;

        int answer = query(1, 0, N - 1, i - 1, j - 1, k);
        cout << answer << "\n";

        lastAnswer = answer;
    }
}
