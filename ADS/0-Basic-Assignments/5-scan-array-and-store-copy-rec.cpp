//Scan array of 10 integers recursively.
//Copy it in another array in reverse order recursively.

#include<iostream>
using namespace std;

void scan_rec(int *p,int n)
{
	if(n==0)
		return;

	cout<<"\n Enter an element:";
	cin>>*p;
	scan_rec(p+1,n-1);	
}

void store_rev_rec(int *arr,int *copy,int n)
{
	if(n==0)
		return;
		
	*copy = *arr;
	store_rev_rec(arr-1,copy+1,n-1);
}	

int main()
{
	freopen("input.txt","r",stdin);

	int arr[10],copy[10];

	scan_rec(arr,10);
	
	store_rev_rec(arr+9,copy,10);
		
	cout<<"\n\n Array Element:";
	for(int i=0;i<10;i++)
		cout<<arr[i]<<" ";
	
	cout<<"\n\n Copied Array Element:";
	for(int i=0;i<10;i++)
		cout<<copy[i]<<" ";
	
	return 0;
}
