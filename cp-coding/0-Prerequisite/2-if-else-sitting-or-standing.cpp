// https://orac.amt.edu.au/cgi-bin/train/problem.pl?set-simple1&problemid=342#statement

#include <iostream>
#include <cstdio>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;

int main()
{
    freopen("sitin.txt", "r", stdin);
    freopen("sitout.txt", "w", stdout);

    int row, seat, ticket;
    cin >> row >> seat >> ticket;

    if ((row * seat) < ticket)
    {
        cout << (row * seat) << " " << ticket - (row * seat);
    }
    else
    //((row * seat) == ticket)
    {
        cout << ticket << " 0";
    }

    return 0;
}