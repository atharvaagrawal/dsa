// N Factorial
// 4! = 4*3*2*1
#include<iostream>
using namespace std;

int factorial(int n)
{
	if(n==0)
		return 1;
	int res;
	res = factorial(n-1);
	return res*n;
}

int main()
{
	int n;
	cout<<"\n\n Enter value of n:";
	cin>>n;
	
	cout<<"\n\n Factorial:"<<factorial(n);	
	return 0;
}
