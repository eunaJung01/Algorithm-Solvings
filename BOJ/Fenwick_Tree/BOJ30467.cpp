#include <iostream>
#include <algorithm>

using namespace std;
using ll = long long;

const int MAX_NUMBERS = 100001;

int lights[MAX_NUMBERS];
int idx[MAX_NUMBERS];
int tree[MAX_NUMBERS];

int N, S;

void update(int i, int diff) {
    while (i <= N) {
        tree[i] += diff;
        i += (i & -i);
    }
}

int query(int i) {
    int answer = 0;
    while (i > 0) {
        answer += tree[i];
        i -= (i & -i);
    }
    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> S;

    for (int i = 0; i < N; ++i) {
        cin >> lights[i];
        idx[i] = lights[i];
    }
    sort(idx, idx + N);

    for (int i = 0; i < N; ++i) {
        lights[i] = lower_bound(idx, idx + N, lights[i]) - idx + 1;
    }

    ll answer = 0;
    ll temp = 0;
    for (int i = 0; i < S; ++i) {
        temp += query(lights[i] - 1);
        update(lights[i], 1);
    }
    answer = temp;

    for (int i = S; i < N; ++i) {
        temp -= query(N) - query(lights[i - S]);
        update(lights[i - S], -1);

        temp += query(lights[i] - 1);
        update(lights[i], 1);

        answer = max(answer, temp);
    }

    cout << answer;
}
