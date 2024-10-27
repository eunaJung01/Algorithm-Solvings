#include <iostream>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int A[N];
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    int floor[N];
    for (int i = 0; i < N; ++i) {
        floor[i] = i + 1;
    }

    deque<int> answer;
    for (int i = 0; i < N; ++i) {
        int card = floor[i];

        if (A[N - i - 1] == 1) {
            answer.push_front(card);
            continue;
        }
        if (A[N - i - 1] == 2) {
            int temp = answer.front();
            answer.pop_front();

            answer.push_front(card);
            answer.push_front(temp);
            continue;
        }
        answer.push_back(card);
    }

    for (int a: answer) {
        cout << a << " ";
    }
}
