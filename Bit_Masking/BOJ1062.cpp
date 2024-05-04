#include <iostream>
#include <string>

using namespace std;

const int MAX_WORDS = 50;
const int NUMBER_OF_ALPHABETS = 26;

// bit masks
int alphasToLearn;
int words[MAX_WORDS];

int N, K;

int DFS(int alpha, int numberOfLearnedAlphas) {
    if (numberOfLearnedAlphas == K) {
        int readable = 0;
        for (int i = 0; i < N; ++i) {
            if ((words[i] & alphasToLearn) == words[i]) {
                readable++;
            }
        }
        return readable;
    }

    int result = 0;
    for (int i = alpha; i < NUMBER_OF_ALPHABETS; ++i) {
        if ((alphasToLearn & (1 << i)) == 0) {
            alphasToLearn |= (1 << i);
            result = max(result, DFS(i + 1, numberOfLearnedAlphas + 1));
            alphasToLearn &= ~(1 << i);
        }
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K;

    if (K < 5) {
        cout << "0";
        return 0;
    }
    if (K >= NUMBER_OF_ALPHABETS) {
        cout << N;
        return 0;
    }

    alphasToLearn |= (1 << ('a' - 'a'));
    alphasToLearn |= (1 << ('c' - 'a'));
    alphasToLearn |= (1 << ('i' - 'a'));
    alphasToLearn |= (1 << ('n' - 'a'));
    alphasToLearn |= (1 << ('t' - 'a'));

    for (int i = 0; i < N; ++i) {
        string word;
        cin >> word;

        for (int j = 0; j < word.length(); ++j) {
            words[i] |= (1 << (word[j] - 'a'));
        }
    }

    cout << DFS(0, 5);
}
