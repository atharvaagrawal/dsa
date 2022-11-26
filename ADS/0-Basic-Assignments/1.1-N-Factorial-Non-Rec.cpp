// Find nth fibonacci term non recursively.

#include<iostream>
using namespace std;

int main()
{
	int n;
	cout<<"\n\n Non-Rec Enter value of n:";
	cin>>n;
	
	int res=1;
	
	for(int i=1;i<=n;i++)
		res = res*i;
	
	cout<<"\n\n Factorial is "<<res;
	return 0;
}

