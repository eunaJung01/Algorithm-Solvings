#include <iostream>
#include <string>
#include <map>

using namespace std;

const string MARK_OF_FLOOR = "--";

struct Trie {
    bool isEnd = false;
    map<string, Trie *> nextRooms;

    void insert(const string *line, int length) {
        if (length == 0) {
            isEnd = true;
            return;
        }
        string food = line[0];
        auto iter = nextRooms.find(food);
        if (iter == nextRooms.end()) {
            nextRooms.insert({food, new Trie()});
        }
        nextRooms.find(food)->second->insert(line + 1, length - 1);
    }

    void print(int floor) {
        if (isEnd) {
            return;
        }
        map<string, Trie *>::iterator iter;
        for (iter = nextRooms.begin(); iter != nextRooms.end(); iter++) {
            for (int j = 0; j < floor; ++j) {
                cout << MARK_OF_FLOOR;
            }
            cout << iter->first << "\n";
            iter->second->print(floor + 1);
        }
    }
};

int N, K;
Trie *root = new Trie();

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;

    string *line;
    while (N--) {
        cin >> K;
        line = new string[K];
        for (int i = 0; i < K; ++i) {
            cin >> line[i];
        }
        root->insert(line, K);
        delete[] line;
    }

    root->print(0);
}
