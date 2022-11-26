// Scan a string from user.
// Check if it is pallindrome or not  recursively.
#include<iostream>
#include<cstring>
using namespace std;

// Reverse String	
void rev_str(char *str,char *rev,int n)
{
	if(n==0)
		return;
	
	*rev = *str;
	rev_str(str-1,rev+1,n-1);
}

int palindrome_rec(char *str,char *rev,int n)
{
	if(n==0)
		return 1;
			
	if( *str != *rev)
		return 0;
	return palindrome_rec(str+1,rev+1,n-1);
}

// Another Method
int palindrome(char *str,int st,int end)
{
	if(st > end)
		return 1;
	if(str[st] != str[end])
		return 0;
		
	return palindrome(str,st+1,end-1);
}

int main()
{
	char str[100],rev[100];
	
	cout<<"\n\n Enter a String:";
	cin.getline(str,100);
	
	int len = strlen(str);
		
	rev_str(str+(len-1),rev,len);
	
//	int res = palindrome_rec(str,rev,len);	
	
	int res = palindrome(str,0,len-1);	
	
	if(res)
		cout<<"\n\n String is Palindrome";
	else
		cout<<"\n\n String is not Palindrome";
	return 0;
}
