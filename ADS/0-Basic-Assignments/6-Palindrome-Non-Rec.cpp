// Scan a string from user.
// Check if it is pallindrome or not non-recursively.
#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	char str[100],rev[100];
	
	cout<<"\n\n Enter any String:";
	cin.getline(str,100);
	
	int n=strlen(str);
	int  k=0;
	
	for(int i=n-1;i>=0;i--)
	{
		rev[k] = str[i];
		k++;
	}
	
	int flag = 0;
		
	// Checking if palindrome
	for(int i=0;i<n;i++)
	{
		if(rev[i] != str[i])
		{
			flag=1;
			break;			
		}
	}
	
	if(flag)
		cout<<"\n\n String is Not Palindrome";
	else
		cout<<"\n\n String is Palindrome";

	return 0;
}
