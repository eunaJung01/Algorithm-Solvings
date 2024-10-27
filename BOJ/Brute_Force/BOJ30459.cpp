#include <iostream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int malDuk[2000];
int gitDae[40000];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, R;
    cin >> N >> M >> R;

    for (int i = 0; i < N; ++i) {
        cin >> malDuk[i];
    }
    for (int i = 0; i < M; ++i) {
        cin >> gitDae[i];
    }
    sort(malDuk, malDuk + N);
    sort(gitDae, gitDae + M);

    set<int> setOfBottoms;
    for (int i = 0; i < N - 1; ++i) {
        for (int j = i + 1; j < N; ++j) {
            setOfBottoms.insert(malDuk[j] - malDuk[i]);
        }
    }

    vector<int> bottoms;
    bottoms.reserve(setOfBottoms.size());
    for (int setOfBottom: setOfBottoms) {
        bottoms.push_back(setOfBottom);
    }

    double answer = 0;
    for (int gitDae_i = 0; gitDae_i < M; ++gitDae_i) {
        int bottom_left = 0;
        int bottom_right = bottoms.size() - 1;

        while (bottom_left <= bottom_right) {
            int bottom_mid = (bottom_left + bottom_right) / 2;
            double temp = bottoms[bottom_mid] * gitDae[gitDae_i] * 0.5;

            if (temp <= R) {
                answer = max(answer, temp);
                bottom_left = bottom_mid + 1;
                continue;
            }
            bottom_right = bottom_mid - 1;
        }
    }

    if (answer == 0) {
        cout << "-1";
    } else {
        cout << fixed;
        cout.precision(1);
        cout << answer;
    }
}
