// Scan array of 10 integers recursively.
// Count how many times 10 is present in the array recursively.
#include<iostream>
using namespace std;

void rec_scan(int n,int *p,int *count)
{
	if(n==0)
		return ;
	
	int x;
	cout<<"\n Enter Element value:";
	cin>>x;
	
	if(x==10)
	 	*count=*count+1;
	
	*p = x;
	rec_scan(n-1,p+1,count);
}

int main()
{
	int arr[10];
	int count=0;
	 
	rec_scan(10,arr,&count);
	
	cout<<"\n\n Array Elements:";
	for(int i=0;i<10;i++)
	{
		cout<<arr[i]<<" ";
	}
	
	cout<<"\n\n Count of 10:"<<count;
	return 0;
}

