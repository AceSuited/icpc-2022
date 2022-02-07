#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n; cin >> n;
    cin.ignore();

    stack<string> stk[105];
    for (int i = 0; i <= n; ++i) {
        string s;
        getline(cin, s);

        int pos = 0;
        for (int j = 0; j < s.length(); ++j) {
            if (s[j] == ' ') {
                stk[i].push(s.substr(pos, j - pos));
                pos = j + 1;
            }
        }
        stk[i].push(s.substr(pos));
    }

    bool flag = true;

    while (!stk[n].empty()) {
        string now = stk[n].top();
        stk[n].pop();

        bool find = false;
        for (int i = 0; i < n; ++i) {
            if (stk[i].empty()) continue;
            if (stk[i].top() != now) 
                continue;

            stk[i].pop();
            find = true;
        }

        if (find == false) {
            flag = false;
            break;
        }
    }

    if (flag == true)
        cout << "Possible" << '\n';
    else
        cout << "Impossible" << '\n';
}