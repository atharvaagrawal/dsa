#include <bits/stdc++.h>
using namespace std;

// max xor value by rearranging the array
int max_xor(vector<int> arr)
{
   int max_xor = 0;
   for (int i = 0; i < arr.size(); i++)
   {
      for (int j = i + 1; j < arr.size(); j++)
      {
         max_xor = max(max_xor, arr[i] ^ arr[j]);
      }
   }
   return max_xor;
}

int main()
{
   // maximum xor value by rearranging the 2 binary string
   string s1 = "10101";
   string s2 = "01010";
   int count = 0;
   for (int i = 0; i < s1.length(); i++)
   {
      if (s1[i] != s2[i])
      {
         count++;
      }
   }

   cout << count << endl;
   return 0;
}