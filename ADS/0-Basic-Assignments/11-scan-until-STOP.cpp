//Keep scannning a string from user until user enters STOP recursively.
//Print length of each string.
#include<iostream>
#include<cstring>
using namespace std;

void scanStr()
{
	char str[100];
	cout<<"\n Enter a String:";
	cin.getline(str,100);
	
	if(strcmp(str,"STOP") == 0)
		return;
	
	cout<<" Length:"<<strlen(str);
	
	scanStr();
}

int main()
{
	scanStr();
	return 0;
}
