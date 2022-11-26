#include <iostream>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;

struct Binary
{
    int ele;
    int count;
};

// int countOfEle(int ele)
// {
//    int count = 0;
//    while (ele != 0)
//    {
//       if (ele % 2 == 1)
//          count += 1;
//       ele = ele / 2;
//    }
//    return count;
// }

int countOfEle(int n)
{
    // Initialising a variable count to 0.
    int count = 0;
    while (n)
    {
        count += n & 1;

        n >>= 1;
    }
    return count;
}

void merge(int array[], int const left, int const mid,
           int const right)
{
    auto const subArrayOne = mid - left + 1;
    auto const subArrayTwo = right - mid;

    // Create temp arrays
    int *leftArray = new int[subArrayOne],
        *rightArray = new int[subArrayTwo];

    // Copy data to temp arrays leftArray[] and rightArray[]
    for (auto i = 0; i < subArrayOne; i++)
        leftArray[i] = array[left + i];
    for (auto j = 0; j < subArrayTwo; j++)
        rightArray[j] = array[mid + 1 + j];

    auto indexOfSubArrayOne = 0,   // Initial index of first sub-array
        indexOfSubArrayTwo = 0;    // Initial index of second sub-array
    int indexOfMergedArray = left; // Initial index of merged array

    // Merge the temp arrays back into array[left..right]
    while (indexOfSubArrayOne < subArrayOne && indexOfSubArrayTwo < subArrayTwo)
    {
        int count1 = countOfEle(leftArray[indexOfSubArrayOne]);
        int count2 = countOfEle(rightArray[indexOfSubArrayTwo]);
        if (count1 >= count2)
        {
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
            indexOfSubArrayOne++;
        }
        else
        {
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
            indexOfSubArrayTwo++;
        }
        indexOfMergedArray++;
    }
    // Copy the remaining elements of
    // left[], if there are any
    while (indexOfSubArrayOne < subArrayOne)
    {
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
        indexOfSubArrayOne++;
        indexOfMergedArray++;
    }
    // Copy the remaining elements of
    // right[], if there are any
    while (indexOfSubArrayTwo < subArrayTwo)
    {
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
        indexOfSubArrayTwo++;
        indexOfMergedArray++;
    }
    delete[] leftArray;
    delete[] rightArray;
}

// begin is for left index and end is
// right index of the sub-array
// of arr to be sorted */
void mergeSort(int array[], int const begin, int const end)
{
    if (begin >= end)
        return; // Returns recursively

    auto mid = begin + (end - begin) / 2;
    mergeSort(array, begin, mid);
    mergeSort(array, mid + 1, end);
    merge(array, begin, mid, end);
}

int main()
{
    int arr[] = {5, 2, 3, 9, 4, 6, 7, 15, 32};
    int n = sizeof(arr) / sizeof(arr[0]);
    Binary bin[n];
    int count = 0;

    for (int i = 0; i < n; i++)
    {
        int temp = arr[i];
        while (temp != 0)
        {
            if (temp % 2 == 1)
                count += 1;
            temp = temp / 2;
        }
        bin[i].count = count;
        bin[i].ele = arr[i];
        count = 0;
    }

    mergeSort(arr, 0, n - 1);
    // mergeSort(bin, 0, n - 1);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
}