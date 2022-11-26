#include <iostream>
#include <vector>
using namespace std;

int no_item;

void display(vector<vector<float>> v)
{
    cout << "\n\n Vector's Element:\n\n";

    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < v[i].size(); j++)
        {
            cout << v[i][j] << "\t";
        }
        cout << "\n";
    }
    cout << "\n\n";
}

int main()
{
    vector<float> items = {1, 2, 3, 4, 5, 6};
    vector<float> profit = {30, 50, 40, 25, 100, 45};
    vector<float> weight = {10, 40, 50, 90, 120, 200};
    vector<float> pwratio;

    vector<vector<float>> v;

    float profitGain = 0, capacity = 200, capcal = 0;

    no_item = sizeof(items) / sizeof(items[0]);

    cout << "\n\n No Of Items:" << no_item;

    // Calculation Profit-Weight Ratio
    for (int i = 0; i <= no_item; i++)
    {
        pwratio.push_back(profit[i] / weight[i]);
    }

    v.push_back(items);   // Row No: 0 - Item
    v.push_back(profit);  // Row No: 1 - Profit
    v.push_back(weight);  // Row No: 2 - Weight
    v.push_back(pwratio); // Row No: 3 - ProfitWeight Ratio

    cout << "\n\n Vector Before Sort:";
    display(v);

    // Bubble Sort
    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < no_item; j++)
        {
            if (v[3][j] < v[3][j + 1])
            {
                swap(v[3][j], v[3][j + 1]);
                swap(v[0][j], v[0][j + 1]);
                swap(v[1][j], v[1][j + 1]);
                swap(v[2][j], v[2][j + 1]);
            }
        }
    }

    cout << "\n\n Vector After Sort:";
    display(v);

    for (int i = 0; i < v[3].size(); i++)
    {
        if (capacity == 0)
        {
            break;
        }

        if (v[2][i] <= capacity)
        {
            profitGain += v[1][i];
            capacity -= v[2][i];
        }
        else
        {
            profitGain += (v[3][i] * capacity);
            break;
        }
    }

    cout << "\n\n Profit Gain: " << profitGain << endl;

    return 0;
}