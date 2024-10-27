#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 500001;

ll players[MAX_NUMBERS];
vector<pair<ll, int>> sortPlayersByRank;

ll tree[MAX_NUMBERS * 4];

ll answer[MAX_NUMBERS];

void update(int node, int start, int end, ll idx) {
    if (idx < start || idx > end) {
        return;
    }

    tree[node] += 1;
    if (start == end) {
        return;
    }

    int mid = (start + end) / 2;
    if (idx <= mid) {
        update(node * 2, start, mid, idx);
    } else {
        update(node * 2 + 1, mid + 1, end, idx);
    }
}

ll query(int node, int start, int end, ll left, ll right) {
    if (left > end || right < start) {
        return 0;
    }
    if (left <= start && end <= right) {
        return tree[node];
    }

    int mid = (start + end) / 2;
    ll left_query = query(node * 2, start, mid, left, right);
    ll right_query = query(node * 2 + 1, mid + 1, end, left, right);
    return left_query + right_query;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        cin >> players[i];
        sortPlayersByRank.emplace_back(players[i], i);
    }

    sort(sortPlayersByRank.begin(), sortPlayersByRank.end());
    for (int i = 0; i < N; ++i) {
        players[sortPlayersByRank[i].second] = i;
    }

    answer[0] = 1;
    update(1, 0, N - 1, players[0]);

    for (int i = 1; i < N; ++i) {
        answer[i] = i + 1 - query(1, 0, N - 1, 0, players[i]);
        update(1, 0, N - 1, players[i]);
    }

    for (int i = 0; i < N; ++i) {
        cout << answer[i] << "\n";
    }
}
