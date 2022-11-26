#include <iostream>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;

int main()
{
    int n;
    freopen("input.txt", "r", stdin);

    cin >> n;

    int arr[n][n];

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> arr[i][j];
        }
    }

    // Printing in Zig Zag Fashion

    int row = 0, col = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << arr[row][col] << " ";
            if (col % 2 == 0)
                row++;
            else
                row--;
        }
        if (col % 2 == 0)
            row--;
        else
            row++;

        col++;
    }

    return 0;
}