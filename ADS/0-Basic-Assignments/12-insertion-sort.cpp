//WAP to implement insertion sort.
#include<iostream>
using namespace std;

int main()
{
	int n;
	cout<<"\n\n Enter number of elements:";
	cin>>n;
	
	int arr[n];
	cout<<"\n\n Enter "<<n<<" Elements";
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	
	for(int i=1;i<n;i++)
	{
		int j = i-1;
		int key = arr[i];
		while(j>=0 && key<arr[j])
		{
			arr[j+1] = arr[j];
			j--;
		}
		arr[j+1] = key;
	}
	
	cout<<"\n\n Element After Sort:";
	for(int i=0;i<n;i++)
	{
		cout<<arr[i]<<" ";
	}
	
	return 0;
}
