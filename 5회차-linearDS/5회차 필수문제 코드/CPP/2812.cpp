#include <bits/stdc++.h>
using namespace std;
using ll = long long;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;

    string s;
    cin >> s;

    deque<int> stk;
    int cnt = 0;
    for (int i = 0; i < (int)s.length(); ++i) {
        int now = s[i] - '0';
        if (stk.empty() || stk.back() >= now)
            stk.push_back(now);
        else {
            while (!stk.empty() && stk.back() < now && cnt < k) {
                stk.pop_back();
                cnt++;
            }
            stk.push_back(now);
        }
    }
    
    while (cnt < k) {
        stk.pop_back();
        cnt++;
    }

    for (auto it : stk)
        cout << it;
    cout << '\n';
}