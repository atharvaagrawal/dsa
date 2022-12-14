// heap sort//
// Do with both maxheap and minheap
#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;
void printArray(int *heap);

void upAdjust(int *heap, int i)
{
    while (i / 2 >= 1)
    {
        if (heap[i / 2] < heap[i])
        {
            swap(heap[i / 2], heap[i]);
            // cout << "\n swap : " << i / 2 << " " << i << endl;
            i = i / 2;
            // printArray(heap);
        }
        else
        {
            break;
        }
    }
}

void downAdjust(int *heap, int i)
{
    int j;
    int n = heap[0];
    while (2 * i <= n)
    {
        j = 2 * i;
        if ((j + 1) <= n)
        {
            if (heap[j] < heap[j + 1])
            {
                j = j + 1;
            }
        }
        if (heap[i] < heap[j])
        {
            swap(heap[i], heap[j]);
            i = j;
        }
        else
        {
            break;
        }
    }
}

void printArray(int *heap)
{
    int n = heap[0];
    cout << "\nArray elements are : ";
    for (int i = 1; i <= n; i++)
    {
        cout << "  " << heap[i];
    }
    cout << "\n";
}

int main()
{
    int n;
    cout << "\nEnter no of elements : ";
    cin >> n;
    cout << "\nEnter elements ";
    int *heap = new int[n + 1];
    heap[0] = 0;
    int x = 0;
    for (int i = 1; i <= n; i++)
    {
        cin >> x;
        heap[i] = x;
        heap[0]++;
        upAdjust(heap, i);
    }
    cout << "\nMAXHEAP is :";
    printArray(heap);

    // downAdjust
    int last, max;
    while (heap[0] > 1)
    {
        max = heap[1];
        last = heap[0];
        heap[1] = heap[last];
        heap[0]--;
        heap[last] = max;
        downAdjust(heap, 1);
    }
    heap[0] = n;
    cout << "\nSORTED ARRAY USING DOWN ADJUST :- ";
    printArray(heap);
    upAdjust(heap, 1);
    //                        LAST ELEMENT NOT SORTED ??

    while (heap[0] >= 1)
    {
        max = heap[1];
        last = heap[0];

        // cout << "\n last heap[0]: " << last << " max heap[1]:" << max << endl;

        heap[1] = heap[last];
        heap[last] = max;
        heap[0]--;

        // cout << "\n heap[0]: " << heap[0] << " heap[1]:" << heap[last] << " heap[last]:" << max << endl;

        // cout << "\n\n Before:";
        // printArray(heap);

        upAdjust(heap, last);

        // cout << "\n\n After:";
        // printArray(heap);
    }

    heap[0] = n;
    // cout << "\nSORTED ARRAY USING UP ADJUST :- ";
    printArray(heap);

    return 0;
}

/*
Enter no of elements : 5

Enter elements 10 2 5 50 30

MAXHEAP is :
Array elements are :   50  30  5  2  10

SORTED ARRAY USING DOWN ADJUST :-
Array elements are :   2  5  10  30  50

Array elements are :   50  30  10  5  2

*/