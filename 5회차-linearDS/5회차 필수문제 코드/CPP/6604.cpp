#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    pair<int, int> arr[26];
    for (int i = 0; i < n; ++i) {
        char c; cin >> c;

        c -= 'A';
        cin >> arr[c].first >> arr[c].second;;
    }

    string s;
    while (cin >> s) {
        int ans = 0;
        bool error = false;
        stack<pair<int, int>> stk;

        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') 
                continue;
            else if (s[i] == ')') {
                pair<int, int> a = stk.top(); stk.pop();
                pair<int, int> b = stk.top(); stk.pop();
                if (b.second != a.first) {
                    error = true;
                    break;
                }
                ans += b.first * b.second * a.second;
                stk.push({b.first, a.second});
            }
            else 
                stk.push({arr[s[i] - 'A'].first, arr[s[i] - 'A'].second});
        }

        if (error) 
            cout << "error" << '\n';
        else 
            cout << ans << '\n';
    }
}