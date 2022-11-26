#include <iostream>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;
int a;

void solve()
{
    int n, j, test, start, end;
    cin >> n >> test;

    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a;
        arr[i] = a;
    }

    for (int i = 0; i < test; i++)
    {
        cin >> start >> end;

        // solve
        int flag1 = 0, flag2 = 0;

        for (j = 0; j < n; j++)
        {
            if (start == arr[j])
            {
                flag1 = 1;
                break;
            }
        }
        while (j < n)
        {
            if (end == arr[j])
            {
                flag2 = 1;
                break;
            }
            j++;
        }

        if (flag1 == 1 && flag2 == 1)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}

int main()
{
    int t;
    cin >> t;

    for (int z = 0; z < t; z++)
    {
        solve();
    }

    return 0;
}