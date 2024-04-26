#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<int> numbers;

bool isGoodNumber(int idx, int number) {
    int left = 0;
    int right = N - 1;

    while (left < right) {
        if (left == idx) {
            left++;
            continue;
        }
        if (right == idx) {
            right--;
            continue;
        }

        int sum = numbers[left] + numbers[right];
        if (sum == number) {
            return true;
        }

        if (sum < number) {
            left++;
            continue;
        }
        right--;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;

    for (int i = 0; i < N; ++i) {
        int n;
        cin >> n;
        numbers.push_back(n);
    }
    sort(numbers.begin(), numbers.end());

    int goodNumbers = 0;
    for (int i = 0; i < N; ++i) {
        if (isGoodNumber(i, numbers[i])) {
            goodNumbers++;
        }
    }
    cout << goodNumbers << endl;
}
