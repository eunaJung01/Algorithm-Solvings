#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int N;
        cin >> N;

        int heights[N];
        for (int j = 0; j < N; ++j) {
            cin >> heights[j];
        }
        sort(heights, heights + N);

        deque<int> tongs;
        for (int j = 0; j < N; ++j) {
            if (j % 2 == 0) {
                tongs.push_back(heights[j]);
                continue;
            }
            tongs.push_front(heights[j]);
        }

        int level = -1;
        for (int j = 0; j < N - 1; ++j) {
            level = max(level, abs(tongs[j] - tongs[j + 1]));
        }
        cout << level << endl;
    }
}
