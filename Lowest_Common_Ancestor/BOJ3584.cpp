#include <iostream>
#include <vector>

using namespace std;

const int MAX_NUMBERS = 10001;

int N;
int parents[MAX_NUMBERS];
vector<int> children[MAX_NUMBERS];
int depth[MAX_NUMBERS];

int setRoot() {
    for (int i = 1; i <= N; ++i) {
        if (parents[i] == 0) {
            return i;
        }
    }
    return 0;
}

void setDepthByDFS(int parent) {
    for (int child: children[parent]) {
        depth[child] = depth[parent] + 1;
        setDepthByDFS(child);
    }
}

int LCA(int a, int b) {
    if (depth[a] < depth[b]) {
        swap(a, b);
    }

    while (depth[a] > depth[b]) {
        a = parents[a];
    }

    while (a != b) {
        a = parents[a];
        b = parents[b];
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        cin >> N;

        fill(parents, parents + N + 1, 0);
        for (int i = 1; i < N + 1; ++i) {
            children[i].clear();
        }

        for (int i = 0; i < N - 1; ++i) {
            int parent, child;
            cin >> parent >> child;

            parents[child] = parent;
            children[parent].push_back(child);
        }
        int root = setRoot();
        setDepthByDFS(root);

        int node1, node2;
        cin >> node1 >> node2;

        cout << LCA(node1, node2) << "\n";
    }
}
