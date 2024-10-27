#include <iostream>
#include <string>

using namespace std;

int L;
string str;
int *pattern;

void findPattern() {
    pattern[0] = 0;
    int j = 0;
    for (int i = 1; i < L; ++i) {
        while (j > 0 && str[i] != str[j]) {
            j = pattern[j - 1];
        }
        if (str[i] == str[j]) {
            pattern[i] = ++j;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> L;
    cin >> str;
    pattern = new int[L];

    findPattern();
    cout << L - pattern[L - 1];
}
