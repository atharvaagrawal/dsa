#include <iostream>
#include <string>
#include <math.h>
using namespace std;

void solveTestCase()
{
   int n, x, y;
   cin >> n >> x >> y;

   int ans = INT32_MAX;

   for (int bus = 0; bus <= ceil(n / 100.0); bus++)
   {
      cout << "a";
      int cars = max((double)0, ceil((n - bus * 100) / 4.0));
      int smoke = bus * x + cars * y;
      ans = min(ans, smoke);
   }

   cout << ans << endl;
}

int main()
{
   int t = 1;

   cout<<"Helloo";
   return 0;
}