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

int query(int node, int start, int end, int first, int last, int value) {
    if (first > end || last < start) {
        return 0;
    }

    if (first <= start && end <= last) {
        return tree[node].end() - upper_bound(all(tree[node]), value);
    }

    int mid = (start + end) / 2;
    return query(node * 2, start, mid, first, last, value) +
           query(node * 2 + 1, mid + 1, end, first, last, value);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int n;
    for (int i = 1; i <= N; ++i) {
        cin >> n;
        update(1, 1, N, i, n);
    }
    for (int i = 1; i < MAX_NUMBERS * 4; ++i) {
        sort(all(tree[i]));
    }

    int M;
    cin >> M;

    int i, j, k;
    while (M--) {
        cin >> i >> j >> k;
        cout << query(1, 1, N, i, j, k) << "\n";
    }
}

/*
// code by JusticeHui (https://justicehui.github.io/medium-algorithm/2020/02/25/merge-sort-tree/)
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define all(v) v.begin(), v.end()

const int SIZE = 1 << 17;

int N;
int numbers[100001];
vector<int> tree[1 << 18];

void add(int i, int value) {
    i |= SIZE;
    tree[i].push_back(value);
}

void init() {
    for (int i = 1; i <= N; ++i) {
        add(i, numbers[i]);
    }

    for (int i = SIZE - 1; i; --i) {
        tree[i].resize(tree[i * 2].size() + tree[i * 2 + 1].size());
        merge(all(tree[i * 2]), all(tree[i * 2 + 1]), tree[i].begin());
    }
}

int query(int left, int right, int value) {
    left |= SIZE;
    right |= SIZE;

    int result = 0;
    while (left <= right) {
        if (left & 1) {
            result += tree[left].end() - upper_bound(all(tree[left]), value);
            left++;
        }
        if (~right & 1) {
            result += tree[right].end() - upper_bound(all(tree[right]), value);
            right--;
        }
        left >>= 1;
        right >>= 1;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;

    for (int i = 1; i <= N; ++i) {
        int n;
        cin >> n;
        numbers[i] = n;
    }
    init();

    int M;
    cin >> M;

    while (M--) {
        int i, j, k;
        cin >> i >> j >> k;
        cout << query(i, j, k) << "\n";
    }
}
//*/
