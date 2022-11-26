// Scan 6 strings from user.Sort them in ascending order.
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	freopen("inputstr.txt", "r", stdin);
	char s[6][100];

	cout << "\n Enter 6 strings:";
	for (int i = 0; i < 6; i++)
		cin.getline(&s[i][0], 100);

	cout << "\n\n Strings Before Sorting:";
	for (int i = 0; i < 6; i++)
	{
		for (int j = 0; j < strlen(s[i]); j++)
			cout << s[i][j];
		cout << endl;
	}
	for (int i = 0; i < 6; i++)
	{
		char temp[50];
		for (int j = 0; j < strlen(s[i]) - 1; j++)
		{
			// cout << s[i][j] << " " << int(s[i][j]) << endl;

			// if (int(s[i][j + 1]) < int(s[i][j]))
			// {
			// 	char temp = s[i][j];
			// 	s[i][j] = s[i][j + 1];
			// 	s[i][j + 1] = temp;
			// 	// cout << temp << " ";
			// }

			if (strcmp(&s[j][0], &s[j + 1][0]) == 1)
			{
				strcpy(temp, &s[j + 1][0]);
				strcpy(&s[j + 1][0], &s[j][0]);
				strcpy(&s[j][0], temp);
			}
		}
		// cout << endl;
	}

	cout << "\n\n Strings After Sorting:";
	for (int i = 0; i < 6; i++)
	{
		for (int j = 0; j < strlen(s[i]); j++)
			cout << s[i][j];
		cout << endl;
	}
	return 0;
}
