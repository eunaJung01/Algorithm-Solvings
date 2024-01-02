#include "iostream"

using namespace std;

void move(int currentPosition, int positionToMove, int n) {
    if (n == 1) {
        cout << currentPosition << " " << positionToMove << "\n";
        return;
    }

    int leftPosition_betweenThree = 6 - currentPosition - positionToMove;
    move(currentPosition, leftPosition_betweenThree, n - 1);
    cout << currentPosition << " " << positionToMove << "\n";
    move(leftPosition_betweenThree, positionToMove, n - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int K = (1 << N) - 1;
    cout << K << "\n";

    move(1, 3, N);
}
