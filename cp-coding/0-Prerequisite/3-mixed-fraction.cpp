// https://orac.amt.edu.au/cgi-bin/train/problem.pl?problemid=362&set=simple1

#include <iostream>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;

int main()
{
    /*
    22/6 = 3 4/6
    49/7 = 7
    */

    freopen("mixin.txt", "r", stdin);
    freopen("mixout.txt", "w", stdout);

    int n, d;
    cin >> n >> d;

    int cal = n / d;

    if (cal == d)
    {
        cout << cal;
    }
    else
    {
        cout << cal << " " << n - (cal * d) << "/" << d;
    }

    return 0;
}