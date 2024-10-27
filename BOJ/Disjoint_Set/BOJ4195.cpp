#include <iostream>
#include <string>
#include <map>

using namespace std;

const int MAX_FRIENDS = 200001;

int parents[MAX_FRIENDS];

int idx = 1;

int getIdx(map<string, int> &friends, map<int, int> &numberOfFriends, string &nameOfFriend) {
    if (friends.find(nameOfFriend) == friends.end()) {
        friends.insert({nameOfFriend, idx});
        numberOfFriends.insert({idx, 1});
        parents[idx] = idx;
        return idx++;
    }
    return friends.find(nameOfFriend)->second;
}

int find(int i) {
    if (parents[i] == i) {
        return i;
    }
    return find(parents[i]);
}

void union_friends(int f1, int f2) {
    parents[max(f1, f2)] = min(f1, f2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        map<string, int> friends;
        map<int, int> numberOfFriends;
        idx = 1;

        int F;
        cin >> F;

        fill(parents, parents + F, 0);

        while (F--) {
            string f1, f2;
            cin >> f1 >> f2;

            int f1_idx = getIdx(friends, numberOfFriends, f1);
            int f2_idx = getIdx(friends, numberOfFriends, f2);

            int f1_parent = find(f1_idx);
            int f2_parent = find(f2_idx);

            if (f1_parent != f2_parent) {
                numberOfFriends.find(min(f1_parent, f2_parent))->second
                        += numberOfFriends.find(max(f1_parent, f2_parent))->second;

                numberOfFriends.erase(max(f1_parent, f2_parent));

                union_friends(f1_parent, f2_parent);
            }

            cout << numberOfFriends.find(min(f1_parent, f2_parent))->second << "\n";
        }
    }
}
