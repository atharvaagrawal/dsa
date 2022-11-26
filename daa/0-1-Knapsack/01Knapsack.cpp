/*
N = 3
W = 4 // Bag Capacity
values[] = {1,2,3}
weight[] = {4,5,1}

Output: 3
Sort weight asending order
*/

#include <iostream>

using namespace std;

void tabular01Knapsack(int n, int w, int **v, int values[], int weight[])
{
    int k = 0;

    // Row i.e Index  0 to All Elements
    for (int i = 1; i <= n; i++)
    {
        // Column i.e Weight  0 to Bag Capacity
        for (int j = 1; j <= w; j++)
        {
            // if weight is less than current weight
            if (weight[k] <= j)
            {
                // compare previous row
                if (values[k] + v[i - 1][abs(j - weight[k])] > v[i - 1][j])
                {
                    v[i][j] = values[k] + v[i - 1][abs(j - weight[k])];
                }
                else
                {
                    v[i][j] = v[i - 1][j];
                }
            }
            else
            {
                v[i][j] = v[i - 1][j];
            }
        }
        k++;
    }

    // Backtraking Checking Which Item is selected
    k = w;
    int arr[n];

    for (int i = n; i > 0; i--)
    {
        if (v[i][k] != v[i - 1][k])
        {
            arr[i - 1] = 1;
            k = k - weight[i - 1];
        }
        else
        {
            arr[i - 1] = 0;
        }
    }

    cout << "\n\n Item Selected:";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}

int main()
{
    freopen("input.txt", "r", stdin);

    int n, w;
    cout << "\n\n Enter the Number of Elements:";
    cin >> n; // 3 = 0 1 2 3

    cout << "\n\n Enter Capacity of the Bag:";
    cin >> w;

    int values[n], weight[n];

    cout << "\n\n Enter " << n << " values:";
    for (int i = 0; i < n; i++)
        cin >> values[i];

    cout << "\n\n Enter " << n << " weight:";
    for (int i = 0; i < n; i++)
        cin >> weight[i];

    // int v[n+1][w+1];
    // row column

    int **v;
    v = new int *[n + 1];

    for (int i = 0; i < n + 1; i++)
        v[i] = new int[w + 1];

    // Making 0th row 0
    for (int i = 0; i <= w; i++)
    {
        v[0][i] = 0;
    }
    // Making 0th column 0
    for (int i = 0; i <= n; i++)
    {
        v[i][0] = 0;
    }

    cout << "\n\n Input Values:" << endl;
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= w; j++)
        {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }

    tabular01Knapsack(n, w, v, values, weight);

    cout << "\n\n Tabular Values:" << endl;
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= w; j++)
        {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }

    cout << "\n\n Max Profit: " << v[n][w] << endl;

    return 0;
}

/*
Output:
Enter the Number of Elements:6


 Enter Capacity of the Bag:10


 Enter 6 values:20
5
10
25
15
40


 Enter 6 weight:1
2
3
4
7
8


 Input Values:
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0


 Item Selected:1 1 1 1 0 0

 Tabular Values:
0 0 0 0 0 0 0 0 0 0 0
0 20 20 20 20 20 20 20 20 20 20
0 20 20 25 25 25 25 25 25 25 25
0 20 20 25 30 30 35 35 35 35 35
0 20 20 25 30 45 45 50 55 55 60
0 20 20 25 30 45 45 50 55 55 60
0 20 20 25 30 45 45 50 55 60 60


 Max Profit: 60
*/