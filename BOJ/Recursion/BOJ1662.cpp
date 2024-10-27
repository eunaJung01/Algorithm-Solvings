#include "iostream"
#include "string"

using namespace std;

bool hasVisited[51];

int unzip(string &s, int idx) {
    int strLen = 0;
    for (int i = idx; i < s.size(); ++i) {
        if (s[i] == ')' && !hasVisited[i]) {
            hasVisited[i] = true;
            return strLen;
        }
        if (s[i] == '(' && !hasVisited[i]) {
            hasVisited[i] = true;
            int K = s[i - 1] - '0';
            strLen += K * unzip(s, i + 1) - 1;
            continue;
        }
        if (!hasVisited[i]) {
            hasVisited[i] = true;
            strLen++;
        }
    }
    return strLen;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    cin >> S;

    cout << unzip(S, 0);
}
