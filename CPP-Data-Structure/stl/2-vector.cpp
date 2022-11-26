#include <iostream>
#include <vector>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;

void printVector(vector<int> v)
{
    cout << "\n\n Size of Vector:" << v.size() << endl;
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
}

void printVectorPair(vector<pair<int, int>> v)
{
    cout << "\n\n Vector Pairs are: \n";
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i].first << " " << v[i].second << endl;
    }
    cout << endl;
}

int main()
{
    vector<int> v;
    cout << v.size() << endl;

    for (int i = 0; i < 5; i++)
    {
        v.push_back(i + 1);
    }

    printVector(v);

    cout << "\n\n Vectors Important Operation:";

    vector<int> v1(10, 3);
    v1.push_back(39);
    printVector(v1);

    cout << "\n\n Popback Operation:";
    v1.pop_back();
    printVector(v1);

    // Vector of Pair

    vector<pair<int, int>> v2 = {{1, 2}, {3, 4}, {5, 6}};

    for (int i = 0; i < 5; i++)
    {
        v2.push_back({i + 2, i + 1});
    }

    printVectorPair(v2);

    // Array of Vectors
    cout << "\n\n Array of Vectors:\n";
    vector<int> varr[3]; // Here Row is Fixed

    for (int i = 0; i < 3; i++)
    {
        for (int j = i; j < 9; j++)
            varr[i].push_back(j + i);
    }

    for (int i = 0; i < 3; i++)
        printVector(varr[i]);

    cout << "\n\n Dynamic Vector ";
    // To Make Vector Dynamic
    vector<vector<int>> varr2;
    for (int i = 0; i < 5; i++)
    {
        vector<int> temp;
        for (int j = i; j < 9; j++)
        {
            temp.push_back(i + j);
        }
        varr2.push_back(temp);
    }

    for (int i = 0; i < v.size(); i++)
        printVector(varr2[i]);

    return 0;
}