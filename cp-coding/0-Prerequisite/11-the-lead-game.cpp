// https://www.codechef.com/problems/TLG

#include <iostream>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;

int main()
{
    // freopen("input.txt", "r", stdin);
    int n;
    cin >> n;

    int arr[n][3], max, min;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cin >> arr[i][j];
        }
        if (i > 0)
        {
            arr[i][0] += arr[i - 1][0];
            arr[i][1] += arr[i - 1][1];
        }

        arr[i][2] = arr[i][0] - arr[i][1];
    }

    min = max = arr[0][2];

    for (int i = 0; i < n; i++)
    {
        if (max < arr[i][2])
        {
            max = arr[i][2];
        }

        if (min > arr[i][2])
        {
            min = arr[i][2];
        }
    }

    if (max > (-1 * min))
    {
        cout << "1 " << max;
    }
    else
    {
        cout << "2 " << (-1 * min);
    }

    return 0;
}