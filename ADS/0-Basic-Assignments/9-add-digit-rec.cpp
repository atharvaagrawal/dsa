//Scan a number from user.Print addition of its digits recursively.

#include<iostream>
using namespace std;

int addDigit(int n)
{
	if(n==0)
		return 0;
	
	int res= addDigit(n/10);
	return res+n%10;
}

int main()
{
	int n;
	cout<<"\n\n Enter any number:";
	cin>>n;
	
	cout<<"\n Addition of digits:"<<addDigit(n);
	return 0;
}

