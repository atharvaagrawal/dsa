#include <iostream>
using namespace std;

void printBoard(int col[], int n, int q)
{
    int board[n][n] = {};

    for (int i = 0; i <= q; i++)
    {
        board[i][col[i]] = i + 1;
    }

    for (int i = 0; i < 2 * n; i++)
        cout << '-';
    cout << endl;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }

    for (int i = 0; i < 2 * n; i++)
        cout << '-';
    cout << endl;
}

bool safe(int r, int c, int col[])
{
    int j = 0;
    while (j < r)
    {
        if (col[j] == c || (abs(col[j] - c) == abs(j - r)))
        {
            return false;
        }
        j++;
    }
    return true;
}

bool nqueen(int r, int col[], int n)
{
    for (int c = 0; c < n; c++)
    {
        if (safe(r, c, col))
        {
            col[r] = c;

            printBoard(col, n, r);

            if (r == n - 1)
                return true;

            if (nqueen(r + 1, col, n))
                return true;

            col[r] = -1;
            cout << "UNABLE TO PLACE QUEEN " << r + 2 << endl;
        }
    }
    return false;
}

int main()
{
    int n;
    cout << "Enter the size of Chessboard: ";
    cin >> n;
    if (n <= 3)
    {
        cout << "Size should be greater than 3" << endl;
        return 0;
    }

    int col[n];
    for (int i = 0; i < n; i++)
        col[i] = -1;

    nqueen(0, col, n);

    // printBoard(col, n, n - 1);
    return 0;
}

/*OUTPUT -
Enter the size of Chessboard: 4
--------
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
--------
--------
1 0 0 0
0 0 2 0
0 0 0 0
0 0 0 0
--------
UNABLE TO PLACE QUEEN 3
--------
1 0 0 0
0 0 0 2
0 0 0 0
0 0 0 0
--------
--------
1 0 0 0
0 0 0 2
0 3 0 0
0 0 0 0
--------
UNABLE TO PLACE QUEEN 4
UNABLE TO PLACE QUEEN 3
UNABLE TO PLACE QUEEN 2
--------
0 1 0 0
0 0 0 0
0 0 0 0
0 0 0 0
--------
--------
0 1 0 0
0 0 0 2
0 0 0 0
0 0 0 0
--------
--------
0 1 0 0
0 0 0 2
3 0 0 0
0 0 0 0
--------
--------
0 1 0 0
0 0 0 2
3 0 0 0
0 0 4 0
--------
*/