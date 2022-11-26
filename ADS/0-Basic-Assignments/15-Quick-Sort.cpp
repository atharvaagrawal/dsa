// Quick Sort
#include <iostream>
using namespace std;
void quickSort(int arr[], int start, int end);
int main()
{
    freopen("input.txt", "r", stdin);
    int n;

    cout << "\n\n Enter number of Elements:";
    cin >> n;

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        cout << "\n Enter " << i + 1 << " element:";
        cin >> arr[i];
    }

    cout << "\n\n Element Before Sort:";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }

    quickSort(arr, 0, n - 1);

    cout << "\n\n Element After Sort:";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }

    return 0;
}

void quickSort(int arr[], int n)
{
    if (n < 2)
        return;

    int pos = 0;

    for (int i = 1; i < n; i++)
    {
        if (arr[i] < arr[0])
        {
            pos++;
            swap(arr[i], arr[pos]);
        }
    }

    swap(arr[0], arr[pos]);

    int *left = new int[pos];
    int *right = new int[pos + 1 - n];
}