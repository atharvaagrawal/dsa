// nth fibonacci term  0 1 1 2 3 5 8
// n=5
#include<iostream>
using namespace std;

int fibo_rec(int n,int fib1,int fib2)
{
	if(n==1)
		return fib1+fib2;
	
	int res;
	res = fibo_rec(n-1,fib2,fib1+fib2);
	
	return res;
}

int main()
{
	int n;
	cout<<"\n\n Enter value of n:";
	cin>>n;
	
	cout<<"\n The "<<n<<"th Fibonacci Term:"<<fibo_rec(n,0,1);
	
	return 0;
}
