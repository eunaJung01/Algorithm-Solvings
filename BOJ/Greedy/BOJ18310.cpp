#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    int houses[N];
    for (int i = 0; i < N; ++i) {
        cin >> houses[i];
    }
    sort(houses, houses + N);

    cout << houses[(N - 1) / 2] << endl;
}
