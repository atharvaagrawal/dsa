#include <iostream>

using namespace std;

class Fractional
{
    float items, profit;

public:
    Fractional()
    {
    }
    Fractional(float items, float profit)
    {
        this->items = items;
        this->profit = profit;
    }
};

int main()
{
    Fractional arr[5] = Fractional();

    float profit[] = {1, 2};

    return 0;
}