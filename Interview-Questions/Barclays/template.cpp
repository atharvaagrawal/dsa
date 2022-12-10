// Header Files
#include <iostream>
#include <string>
#include <vector>
using namespace std;

/*
 * coordinates is a two-dimensional array representing the X and Y coordinates of the cities, respectively.
 */
int minimumStraightRoutes(vector<vector<int>> coordinates)
{
    int count = 0;
    for (int i = 0; i < coordinates.size(); i++)
    {
        for (int j = i + 1; j < coordinates.size(); j++)
        {
            if (coordinates[i][0] == coordinates[j][0] || coordinates[i][1] == coordinates[j][1])
            {
                count++;
            }
        }
    }
    return count;
}

int main()
{
    // input for coordinates
    freopen("input.txt", "r", stdin);
    int coordinates_row;
    int coordinates_col;
    cin >> coordinates_row;
    cin >> coordinates_col;

    vector<vector<int>> coordinates;
    for (int idx = 0; idx < coordinates_row; idx++)
    {
        vector<int> temp_vector;
        for (int jdx = 0; jdx < coordinates_col; jdx++)
        {
            int temp;
            cin >> temp;
            temp_vector.push_back(temp);
        }
        coordinates.push_back(temp_vector);
    }

    int result = minimumStraightRoutes(coordinates);
    cout << result;

    return 0;
}