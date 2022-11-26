/*
Q6.WAP to implement quick sort.
*/
#include<iostream>
using namespace std;

void printArray(int *arr,int start,int end)
{
	cout<<"\n\n Printing Array Elements:";
	for(int i=start;i<=end;i++)
		cout<<arr[i]<<" ";
	cout<<endl;
}

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high]; // pivot
    int i = (low - 1); // Index of smaller element and indicates 
	// the right position of pivot found so far

    for (int j = low; j <= high - 1; j++) {
        // If current element is smaller than the pivot
        if (arr[j] < pivot) {
            i++; // increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}
  
//int partition(int *arr,int start,int end)
//{
//	int pivot_index = start;
//	int pivot = arr[start];
//	
//	cout<<"\n Pivot:"<<pivot;
//	cout<<"\n Start:"<<start;
//	cout<<"\n End:"<<end;
//	
//	
//	while(start < end)
//	{
//		printArray(arr,start,end);
//		// finding element greater than pivot
//		while(start < 6 && arr[start] <= pivot)
//		{
//			start+=1;
//		}
//		
//		cout<<"\n Start:"<<start;
//		
//		// finding element smaller than pivot
//		while(arr[end] > pivot )
//		{
////			cout<<arr[end]<<" "<<pivot<<endl;
//			end-=1;
//		}
//		cout<<"\n End:"<<end;
//		if( start < end )
//		{
//			int temp = arr[start];
//			arr[start] = arr[end];
//			arr[end] = temp; 
//		}
//	}
//	
//	int temp = arr[end];
//	arr[end] = pivot;
//	arr[pivot_index] = arr[end];
//	
//	return end;
//}

void quickSort(int *arr,int low,int high)
{
	if( low < high)
	{
		int p = partition(arr,low,high);
		cout<<"\n\n Partion:"<<p;
		quickSort(arr,low,p-1);
		quickSort(arr,p+1,high);
	}
}

int main()
{
	int arr[] = {10,30,20,50,5,34};
	
	cout<<"\n\n Before Sorting:";
	for(int i=0;i<6;i++)
		cout<<arr[i]<<" ";
	
	quickSort(arr,0,5);
	cout<<"\n\n After Sorting:";
	for(int i=0;i<6;i++)
		cout<<arr[i]<<" ";	
	
	return 0;
}
