#include <iostream>
#include <string>

using namespace std;

const int MAX_NUMBER_OF_CHAR = 10000 * 500;
const int NUMBER_OF_ALPHABET = 26;

int nextNode[MAX_NUMBER_OF_CHAR][NUMBER_OF_ALPHABET];
bool isEndOfWord[MAX_NUMBER_OF_CHAR];

const int ROOT = 1;
int unused = ROOT + 1;

void insert(const string &str) {
    int currentNode = ROOT;
    for (const char c: str) {
        int c_int = c - 'a';
        if (nextNode[currentNode][c_int] == -1) {
            nextNode[currentNode][c_int] = unused++;
        }
        currentNode = nextNode[currentNode][c_int];
    }
    isEndOfWord[currentNode] = true;
}

bool find(const string &str) {
    int currentNode = ROOT;
    for (const char c: str) {
        int c_int = c - 'a';
        if (nextNode[currentNode][c_int] == -1) {
            return false;
        }
        currentNode = nextNode[currentNode][c_int];
    }
    return isEndOfWord[currentNode];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int i = 0; i < MAX_NUMBER_OF_CHAR; ++i) {
        fill(nextNode[i], nextNode[i] + NUMBER_OF_ALPHABET, -1);
    }

    int N, M;
    cin >> N >> M;

    while (N--) {
        string str;
        cin >> str;
        insert(str);
    }

    int ans = 0;
    while (M--) {
        string str;
        cin >> str;
        ans += find(str);
    }
    cout << ans;
}
