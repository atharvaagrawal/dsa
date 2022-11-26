#include <iostream>
using namespace std;

int main() 
{
    string str;
    cout << "Enter a string: ";
    getline(cin, str);
        
    string nstr;
    int i=0;
 
 	while(i<str.length())
	{
        if(str[i] == ' ')
		{
            if(i==0 || i==str.length()-1)
			{
                i++;
                continue;
            }
            
            while(str[i+1] == ' ')
                i++;
        }
        
        nstr += str[i++];
    }
    
    cout << "New String: " << nstr;
    
    return 0;
}
