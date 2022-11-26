#include <iostream>
using namespace std;

void mergeSort(int arr[], int start, int end);
void merge(int arr[], int start, int mid, int end);

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

	mergeSort(arr, 0, n - 1);

	cout << "\n\n Element After Sort:";
	for (int i = 0; i < n; i++)
	{
		cout << arr[i] << " ";
	}

	return 0;
}

void mergeSort(int arr[], int start, int end)
{
	if (start >= end)
		return;

	int mid = start + ((end - start) / 2);

	mergeSort(arr, start, mid);
	mergeSort(arr, mid + 1, end);
	merge(arr, start, mid, end);
}

// 0 2 5
void merge(int arr[], int start, int mid, int end)
{
	int left = mid - start + 1;
	int right = end - mid;

	int *leftArray = new int[left];
	int *rightArray = new int[right];

	for (int i = 0; i < left; i++)
		leftArray[i] = arr[start + i];
	for (int i = 0; i < right; i++)
		rightArray[i] = arr[mid + 1 + i];

	int indexLeft = 0, indexRight = 0, indexMerge = start;

	while (indexLeft < left && indexRight < right)
	{
		if (leftArray[indexLeft] < rightArray[indexRight])
		{
			arr[indexMerge] = leftArray[indexLeft];
			indexLeft++;
		}
		else
		{
			arr[indexMerge] = rightArray[indexRight];
			indexRight++;
		}
		indexMerge++;
	}

	while (indexLeft < left)
	{
		arr[indexMerge] = leftArray[indexLeft];
		indexLeft++;
		indexMerge++;
	}

	while (indexRight < right)
	{
		arr[indexMerge] = rightArray[indexRight];
		indexRight++;
		indexMerge++;
	}

	delete[] leftArray;
	delete[] rightArray;
}