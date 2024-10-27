#include <iostream>

#define MAX_CANDIES 1000000

using namespace std;

int tree[MAX_CANDIES * 4];

int query(int node, int start, int end, int privilege) {
    if (start == end) {
        return start;
    }
    int mid = (start + end) / 2;
    if (tree[node * 2] >= privilege) {
        return query(node * 2, start, mid, privilege);
    }
    return query(node * 2 + 1, mid + 1, end, privilege - tree[node * 2]);
}

void update(int node, int start, int end, int index, int diff) {
    if (index < start || index > end) {
        return;
    }
    tree[node] += diff;
    if (start != end) {
        int mid = (start + end) / 2;
        update(node * 2, start, mid, index, diff);
        update(node * 2 + 1, mid + 1, end, index, diff);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    while (n--) {
        int A, B, C;
        cin >> A;

        if (A == 1) {
            cin >> B;
            int num = query(1, 0, MAX_CANDIES, B);
            cout << num << "\n";
            update(1, 0, MAX_CANDIES, num, -1);
            continue;
        }
        cin >> B >> C;
        update(1, 0, MAX_CANDIES, B, C);
    }
}
