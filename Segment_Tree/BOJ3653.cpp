#include <iostream>
#include <cstring>

using namespace std;

const int MAX_NUMBERS = 100000;

int positionOfMovies[MAX_NUMBERS];
int tree[MAX_NUMBERS * 2 * 4];

void init(int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return;
    }
    if (start == end) {
        tree[node] = 1;
        return;
    }

    int mid = (start + end) / 2;
    init(node * 2, start, mid, left, right);
    init(node * 2 + 1, mid + 1, end, left, right);
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

int query(int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return 0;
    }
    if (left <= start && end <= right) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    int left_query = query(node * 2, start, mid, left, right);
    int right_query = query(node * 2 + 1, mid + 1, end, left, right);
    return left_query + right_query;
}

void update(int node, int start, int end, int idx, int diff) {
    if (idx < start || idx > end) {
        return;
    }
    tree[node] += diff;
    if (start == end) {
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, idx, diff);
    update(node * 2 + 1, mid + 1, end, idx, diff);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        memset(positionOfMovies, 0, sizeof(positionOfMovies));
        memset(tree, 0, sizeof(tree));

        int n, m;
        cin >> n >> m;
        for (int i = 0; i < n; ++i) {
            positionOfMovies[i] = i + m;
        }
        init(1, 0, m + n - 1, m, m + n - 1);

        for (int i = 0; i < m; ++i) {
            int movie;
            cin >> movie;

            cout << query(1, 0, m + n - 1, 0, positionOfMovies[movie - 1] - 1) << " ";
            update(1, 0, m + n - 1, positionOfMovies[movie - 1], -1);

            int idxToMove = m - i - 1;
            positionOfMovies[movie - 1] = idxToMove;
            update(1, 0, m + n - 1, positionOfMovies[movie - 1], 1);
        }
        cout << "\n";
    }
}
