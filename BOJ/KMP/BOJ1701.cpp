#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void findPattern(const string &input, vector<int> &pattern) {
    int j = 0;
    for (int i = 1; i < input.size(); ++i) {
        while (j > 0 && input[i] != input[j]) {
            j = pattern[j - 1];
        }
        if (input[i] == input[j]) {
            pattern[i] = ++j;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string input;
    cin >> input;

    int ans = 0;
    for (int i = 0; i < input.size(); ++i) {
        vector<int> pattern(input.size(), 0);
        findPattern(input.substr(i), pattern);
        ans = max(ans, *max_element(pattern.begin(), pattern.end()));
    }
    cout << ans;
}
