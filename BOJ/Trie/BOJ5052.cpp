#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MAX_LENGTH = 10;

struct Trie {
    bool isEnd = false;
    Trie *nextNodes[MAX_LENGTH];

    Trie() {
        for (int i = 0; i < MAX_LENGTH; ++i) {
            nextNodes[i] = nullptr;
        }
    }

    void insert(const string &number) {
        if (number.empty()) {
            this->isEnd = true;
            return;
        }
        int n = number[0] - '0';
        if (nextNodes[n] == nullptr) {
            nextNodes[n] = new Trie();
        }
        nextNodes[n]->insert(number.substr(1));
    }

    bool containsOther(const string &number) {
        if (this->isEnd) {
            return true;
        }
        if (number.size() == 1) {
            return false;
        }
        int n = number[0] - '0';
        if (nextNodes[n] == nullptr) {
            return false;
        }
        return nextNodes[n]->containsOther(number.substr(1));
    }
};

Trie *root = new Trie();

void validate(vector<string> &numbers) {
    for (const string &number: numbers) {
        if (root->containsOther(number)) {
            cout << "NO" << "\n";
            return;
        }
    }
    cout << "YES" << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    int n;
    while (t--) {
        cin >> n;
        vector<string> numbers;
        for (int i = 0; i < n; ++i) {
            string number;
            cin >> number;
            numbers.push_back(number);

            root->insert(number);
        }
        validate(numbers);

        delete root;
        root = new Trie();
    }
}
