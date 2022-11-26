// Scan a string from user.Remove all extra spaces from string.
// There must be only one space between 2 words of a string.

#include <iostream>
#include <string.h>

using namespace std;

char *removeSpace(char *str)
{
	int i = 0, j = 0;

	// for empty string only
	if (str[i] == '\0')
	{
		return str;
	}

	// check for empty space
	while (str[i] != '\0')
	{
		if (str[i] == ' ')
			break;
		i++;
	}

	j = i;
	j--;

	while (str[i] == ' ')
	{
		i++;
	}

	// base condition
	if (str[i] == '\0')
	{
		cout << "\n\n 2nd:" << str;
		return str;
	}

	// i = pointing to next word start
	// j = pointint to prev word last

	char res1[100];
	int ind = 0;

	while (j > -1)
	{
		res1[ind] = str[ind];
		ind++;
		j--;
	}

	char *res = removeSpace(str + i);

	i = 0;
	j = strlen(res);

	res1[ind++] = ' ';

	while (j > -1)
	{
		res1[ind] = res[i];
		i++;
		j--;
		ind++;
	}

	cout << "\n res1:" << res1 << endl;

	return res1;
}

int main()
{
	char str[100];
	cout << "\n\n Enter any string:";
	cin.getline(str, 100);

	cout << "\n String with single space:" << removeSpace(str);
	
	for(int i=0;i<strlen(str);i++)
	{
		if(str[i]  )
	}
	
	//	cout<<"str:"<<str;
	//	int arr[100];
	//	int idx = 0;
	//
	//	for(int i=0;i<str.length();i++)
	//	{
	//		if(str[i] == ' ')
	//		{
	//			arr[idx++] = i;
	//		}
	//	}
	//
	//	cout<<"\n Index with zero space:";
	//	for(int i=0;i<idx;i++)
	//	{
	//		cout<<arr[i]<<" ";
	//	}
	return 0;
}
