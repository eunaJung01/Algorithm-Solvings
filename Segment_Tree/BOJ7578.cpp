#include <iostream>
#include <map>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 500001;

map<int, int> machines_in_A;
int machines_in_B[MAX_NUMBERS];

ll tree[MAX_NUMBERS * 4];

ll query(int node, int start, int end, int left, int right) {
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

void update(int node, int start, int end, int idx) {
    if (idx < start || idx > end) {
        return;
    }

    tree[node] += 1;
    if (start == end) {
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, idx);
    update(node * 2 + 1, mid + 1, end, idx);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        int machine_A;
        cin >> machine_A;
        machines_in_A.insert(make_pair(machine_A, i));
    }
    for (int j = 0; j < N; ++j) {
        int machine_B;
        cin >> machine_B;
        machines_in_B[machines_in_A.find(machine_B)->second] = j;
    }

    ll answer = 0;
    for (int i = 0; i < N; ++i) {
        int j = machines_in_B[i];
        answer += query(1, 0, N - 1, j + 1, N - 1);
        update(1, 0, N - 1, j);
    }
    cout << answer;
}
