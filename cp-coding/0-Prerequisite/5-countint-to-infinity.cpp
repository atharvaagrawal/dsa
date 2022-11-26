// https://orac.amt.edu.au/cgi-bin/train/problem.pl?problemid=383&set=simple2
#include <iostream>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;

int main()
{
    freopen("coutin.txt", "r", stdin);
    freopen("coutout.txt", "w", stdout);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cout << i + 1 << endl;
    }

    return 0;
}