// https://orac.amt.edu.au/cgi-bin/train/problem.pl?problemid=372&set=simple1#previous

#include <iostream>
#define deb(x) cout << #x << '=' << x << endl

using namespace std;

int main()
{
    freopen("bendin.txt", "r", stdin);
    freopen("bendout.txt", "w", stdout);

    int x1, y1, x2, y2;
    int x3, y3, x4, y4;

    cin >> x1 >> y1 >> x2 >> y2;
    cin >> x3 >> y3 >> x4 >> y4;

    // Area of Rectangle: Length * breadth
    int l1 = x2 - x1, b1 = y2 - y1;
    int l2 = x4 - x3, b2 = y4 - y3;

    int total_area = (l1 * b1) + (l2 * b2);

    // Intersection Points
    int left_intr = max(x1, x3);
    int right_intr = min(x2, x4);
    int bottom_intr = max(y1, y3);
    int top_intr = min(y2, y4);

    int area_of_interection = 0;

    if (left_intr < right_intr and bottom_intr < top_intr)
    {
        area_of_interection = (right_intr - left_intr) * (top_intr - bottom_intr)
    }

    cout << total_area - area_of_interection;

    // Completely Inside
    // if (x1 > x3 and y1 > y3 and x2 < x4 and y2 < y4)
    // {
    //     cout << l1 * b1;
    // }
    // else if (x3 > x1 and y3 > y1 and x3 < x2 and y3 < y2)
    // {
    //     int repeat_area = (x2 - x3) * (y2 - y3);

    //     total_area -= repeat_area;
    //     cout << total_area;
    // }
    // else
    // {
    //     cout << total_area;
    // }
    return 0;
}