#include <bits/stdc++.h>
using namespace std;
using ll = long long;


bool dp[300][300];
bool visited[300][300];
string a, b, c;
int alen, blen, clen;

bool makeString(int apos, int bpos, int cpos) {
    if (visited[apos][bpos]) 
        return dp[apos][bpos];

    if (apos == alen) 
        return b.substr(bpos) == c.substr(cpos);
    else if (bpos == blen) 
        return a.substr(apos) == c.substr(cpos);

    bool &ret = dp[apos][bpos];

    if (!ret && a[apos] == c[cpos]) 
        ret = ret || makeString(apos+1, bpos, cpos+1);

    if (!ret && b[bpos] == c[cpos]) 
        ret = ret || makeString(apos, bpos+1, cpos+1);

    visited[apos][bpos] = true;
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        memset(dp, false, sizeof(dp));
        memset(visited, false, sizeof(visited));

        cin >> a >> b >> c;
        alen = a.length(), blen = b.length(), clen = c.length();

        cout << "Data set " << i << ": ";
        if (makeString(0, 0, 0))
            cout << "yes" << '\n';
        else 
            cout << "no" << '\n';
    }
}