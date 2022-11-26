// nth fibonacci term  0 1 1 2 3 5 8
// n=5

#include<iostream>
using namespace std;

int main()
{
	int n;
	cout<<"\n\n Enter n value:";
	cin>>n;
	
	int fib0=0,fib1=1,fib2;
	
	for(int i=0;i<n;i++)
	{
		fib2 = fib0+fib1;
		fib0 = fib1;
		fib1 = fib2;
	}
	
	cout<<"\n The "<<n<<"th fibo term is:"<<fib2;
	return 0;
}
