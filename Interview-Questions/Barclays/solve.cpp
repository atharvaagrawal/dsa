#include <iostream>
#include <algorithm>

using namespace std;

struct Point
{
    int x, y;
};

bool cmp(Point a, Point b)
{
    return a.x < b.x;
}

int main()
{
    freopen("input.txt", "r", stdin);

    int N;
    cin >> N;

    // Create an array of N points
    Point points[N];
    for (int i = 0; i < N; i++)
    {
        cin >> points[i].x >> points[i].y;
    }

    // Sort the points in ascending order by their X coordinate
    sort(points, points + N, cmp);

    // Count the minimum number of straight routes needed
    int counter = 0;
    for (int i = 1; i < N; i++)
    {
        if (points[i].y != points[i - 1].y)
        {
            counter++;
        }
    }

    cout << counter << endl;

    return 0;
}
