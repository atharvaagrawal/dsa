// https://orac.amt.edu.au/cgi-bin/train/problem.pl?problemid=382&set=simple2

#include <iostream>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;

int main()
{
    // freopen("taktakin.txt", "r", stdout);
    // freopen("taktakout.txt", "w", stdout);

    int n, count = 0;
    cin >> n;

    while (n % 11 != 0 and n % 11 != 1)
    {
        n = n * 2; // 14 28  56
        count++;
    }

    cout << count << " " << n;

    return 0;
}