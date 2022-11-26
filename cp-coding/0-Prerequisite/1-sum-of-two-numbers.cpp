// https://orac.amt.edu.au/cgi-bin/train/problem.pl?set-simple1&problemid=333#statement

#include <bits/stdc++.h>
#include <iostream>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;

int main()
{
    int a, b;

    freopen("addin.txt", "r", stdin);
    freopen("addout.txt", "w", stdout);

    cin >> a >> b;

    cout << a + b;

    return 0;
}