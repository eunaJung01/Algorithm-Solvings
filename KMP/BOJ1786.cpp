#include <iostream>
#include <string>
#include <vector>

using namespace std;

string T, P;
int *pattern;
int returnPoint;

void findPattern() {
    pattern[0] = 0;
    for (int i = 1; i < P.size(); ++i) {
        if (P[i] == P[pattern[i - 1]]) {
            pattern[i] = pattern[i - 1] + 1;
            continue;
        }
        if (P[0] != P[i]) {
            pattern[i] = 0;
        } else {
            pattern[i] = 1;
        }
    }
}

void setReturnPoint() {
    returnPoint = 0;
    for (int i = 0; i < P.size(); ++i) {
        if (P[i] == P[P.size() - 1] && returnPoint < pattern[i]) {
            returnPoint = pattern[i];
        }
    }
}

void search() {
    int cnt = 0;
    vector<int> positions;

    int j = 0;
    for (int i = 0; i < T.size(); ++i) {
        while (j > 0 && T[i] != P[j]) {
            j = pattern[j - 1];
        }
        if (T[i] == P[j]) {
            j++;
            if (j == P.size()) {
                cnt += 1;
                positions.push_back(i - P.size() + 2);
                j = returnPoint;
            }
        }
    }

    cout << cnt << "\n";
    for (int pos: positions) {
        cout << pos << " ";
    }
}

int main() {
    getline(cin, T);
    getline(cin, P);
    pattern = new int[P.size()];

    findPattern();
    setReturnPoint();
    search();
}
