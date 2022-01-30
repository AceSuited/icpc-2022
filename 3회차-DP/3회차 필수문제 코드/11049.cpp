#include <bits/stdc++.h>
using namespace std;

string s;
int ans = 0;
int dp[505][505];
int a[505], b[505];

int solve(int s, int e) {
    if (dp[s][e] != -1)
        return dp[s][e];


    int& ret = dp[s][e];
    if (s == e) 
        return ret = 0;
    

    ret = INT_MAX;
    for (int i = s; i < e; ++i)
        ret = min(ret, a[s] * b[i] * b[e] + solve(s, i) + solve(i+1, e));

    return ret;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    memset(dp, -1, sizeof(dp));

    for (int i = 0; i < n; ++i)
        cin >> a[i] >> b[i];

    cout << solve(0, n-1) << '\n';
}
