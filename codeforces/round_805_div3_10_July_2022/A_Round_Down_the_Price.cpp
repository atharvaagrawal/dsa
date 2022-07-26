#include <iostream>
#include <cmath>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;
long int checkar[10];

void func(long int m)
{
    if (m == 1 || m < 0)
    {
        cout << 0 << endl;
        return;
    }

    for (int i = 0; i < 10; i++)
    {
        if (m < checkar[i])
        {
            // deb(m);
            // deb(checkar[i - 1]);
            // deb(m - checkar[i - 1]);
            cout << m - checkar[i - 1] << endl;
            return;
        }
    }
    cout << 0 << endl;
    return;
}

int main()
{
    int t, a;
    long int arr[t];
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> a;
        arr[i] = a;
    }

    //[1,10,100,1000]
    // 0 1   2   3

    for (int i = 0; i < 10; i++)
    {
        checkar[i] = pow(10, i);
        // deb(checkar[i]);
    }

    for (int i = 0; i < t; i++)
        func(arr[i]);

    return 0;
}