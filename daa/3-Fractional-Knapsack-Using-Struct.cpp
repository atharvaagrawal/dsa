#include <bits/stdc++.h>
using namespace std;

struct Item
{
    int value;
    int weight;
};

class Solution
{
public:
    void printArr(Item arr[], int n, double ra[])
    {
        cout << "\n\nElements:\nProfit\tWeight\tPWRatio\n";

        for (int i = 0; i < n; i++)
        {
            cout << arr[i].value << "\t" << arr[i].weight << "\t" << ra[i] << endl;
        }
    }

    // Function to get the maximum total value in the knapsack.
    double fractionalKnapsack(int W, Item arr[], int n)
    {
        double pwratio[n], profitGain = 0;
        int itemList[n];

        // Calculating Profit Weight Ratio
        for (int i = 0; i < n; i++)
        {
            itemList[i] = i + 1;
            pwratio[i] = arr[i].value / arr[i].weight;
        }

        cout << "\n Input Data and Profit Weight Ratio:";
        printArr(arr, n, pwratio);

        // Bubble Sort
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n - 1; j++)
            {
                if (pwratio[j] < pwratio[j + 1])
                {
                    // swap(arr[j], arr[j + 1]);
                    swap(itemList[j], itemList[j + 1]);
                    swap(pwratio[j], pwratio[j + 1]);
                }
            }
        }

        mergeSort(arr, 0, n - 1);

        cout << "\n Sorting by Profit Weight Ratio:";
        printArr(arr, n, pwratio);

        float itemSelected[n];

        for (int i = 0; i < n; i++)
        {
            itemSelected[i] = 0;
        }

        // printArr(arr, n, pwratio);
        // Calculating Max Profit
        // cout << "Value Weight W " << endl;
        for (int i = 0; i < n; i++)
        {

            // cout << arr[i].value << " " << arr[i].weight << "  " << W << endl;
            if (W >= arr[i].weight)
            {
                profitGain += arr[i].value;
                W -= arr[i].weight;
                itemSelected[i] = 1;
            }
            else
            {
                // cout << "\n\n Weight:" << W << " arr:" << arr[i].weight << " " << arr[i].value << endl;
                double re = (double)W / arr[i].weight;
                profitGain += re * arr[i].value;
                itemSelected[i] = re;
                W = 0;
                break;
            }
        }

        cout << "\n\n Item Selected:";
        cout << "\nItemNumber SelectedPortion" << endl;
        for (int i = 0; i < n; i++)
        {
            cout << itemList[i] << "\t\t" << itemSelected[i] << endl;
        }

        return profitGain;
    }

    void mergeSort(Item array[], int const begin, int const end);
    void merge(Item array[], int const left, int const mid, int const right);
};

void Solution::merge(Item array[], int const left, int const mid, int const right)
{
    auto const subArrayOne = mid - left + 1;
    auto const subArrayTwo = right - mid;

    // Create temp arrays
    auto *leftArray = new Item[subArrayOne],
         *rightArray = new Item[subArrayTwo];

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

        if ((float)leftArray[indexOfSubArrayOne].value / leftArray[indexOfSubArrayOne].weight >= (float)rightArray[indexOfSubArrayTwo].value / rightArray[indexOfSubArrayTwo].weight)
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

void Solution::mergeSort(Item array[], int const begin, int const end)
{
    if (begin >= end)
        return; // Returns recursively

    auto mid = begin + (end - begin) / 2;

    mergeSort(array, begin, mid);
    mergeSort(array, mid + 1, end);
    merge(array, begin, mid, end);
}

//{ Driver Code Starts.
int main()
{
    int t;
    freopen("input.txt", "r", stdin);
    // taking testcases
    cin >> t;
    cout << setprecision(2) << fixed;
    while (t--)
    {
        // size of array and weight
        int n, W;
        cin >> n >> W;

        Item arr[n];
        // value and weight of each item
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i].value >> arr[i].weight;
        }

        // function call
        Solution ob;
        int res;
        res = ob.fractionalKnapsack(W, arr, n);
        cout << "\n\n Max Profit:" << res << endl;
    }
    return 0;
}
