#include <iostream>
#include <algorithm>
#include <map>

using namespace std;
using ll = long long;

const int MAX_ISLANDS = 75000;

pair<ll, ll> islands[MAX_ISLANDS + 1];
ll tree[MAX_ISLANDS + 1];

int n;

void update(ll idx) {
    while (idx <= n) {
        tree[idx] += 1;
        idx += (idx & -idx);
    }
}

ll query(ll idx) {
    ll answer = 0;
    while (idx > 0) {
        answer += tree[idx];
        idx -= (idx & -idx);
    }
    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        fill(tree, tree + MAX_ISLANDS + 1, 0);
        map<ll, ll> indexOfY;

        cin >> n;

        for (int i = 0; i < n; ++i) {
            ll x, y;
            cin >> x >> y;
            islands[i] = {x, -y};
            indexOfY.insert({-y, 0});
        }
        sort(islands, islands + n);

        ll idx = 0;
        for (auto &iter: indexOfY) {
            iter.second = ++idx;
        }

        ll answer = 0;
        for (int i = 0; i < n; ++i) {
            pair<ll, ll> pos = islands[i];
            ll y_id = indexOfY.find(pos.second)->second;

            answer += query(y_id);
            update(y_id);
        }
        cout << answer << "\n";
    }
}
