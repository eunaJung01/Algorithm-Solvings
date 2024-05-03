#include <iostream>
#include <vector>

using namespace std;

const int ROOT = 1;
const int MAX_NUMBER = 50001;


int N;
vector<int> tree[MAX_NUMBER];
int parents[MAX_NUMBER];

int depths[MAX_NUMBER];
bool hasVisited[MAX_NUMBER];

void setDepthsByDFS(int parent, int depth) {
    hasVisited[parent] = true;
    depths[parent] = depth;

    for (int child: tree[parent]) {
        if (!hasVisited[child]) {
            parents[child] = parent;
            setDepthsByDFS(child, depth + 1);
        }
    }
}

int LCA(int node1, int node2) {
    if (depths[node1] < depths[node2]) {
        swap(node1, node2);
    }

    while (depths[node1] > depths[node2]) {
        node1 = parents[node1];
    }

    while (node1 != node2) {
        node1 = parents[node1];
        node2 = parents[node2];
    }
    return node1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;

    for (int i = 0; i < N - 1; ++i) {
        int node1, node2;
        cin >> node1 >> node2;

        tree[node1].push_back(node2);
        tree[node2].push_back(node1);
    }

    setDepthsByDFS(ROOT, 0);

    int M;
    cin >> M;

    while (M--) {
        int node1, node2;
        cin >> node1 >> node2;

        cout << LCA(node1, node2) << "\n";
    }
}
