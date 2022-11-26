#include <iostream>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;

void findMinMax(int *arr, int i, int j, int &max, int &min)
{
    if (i == j)
    {
        if (arr[i] < min)
            min = arr[i];

        if (arr[j] > max)
            max = arr[j];
        return;
    }
    else if (i == j - 1)
    {
        if (arr[i] < arr[j])
        {
            if (arr[i] < min)
                min = arr[i];
            if (arr[j] > max)
                max = arr[j];
        }
        else
        {
            if (arr[j] < min)
                min = arr[j];
            if (arr[i] > max)
                max = arr[i];
        }
    }
    else
    {
        int mid = (i + j) / 2;
        findMinMax(arr, i, mid, max, min);
        findMinMax(arr, mid + 1, j, max, min);
    }
}
int main()
{
    int arr[] = {10, 20, 30, 4, 23, 45, 46};
    int max = 0, min = 9999;
    findMinMax(arr, 0, 6, max, min);

    cout << max << " " << min;
    return 0;
}