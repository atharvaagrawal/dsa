#include <iostream>
#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int solve(string s)
    {

        int count = 1;

        unordered_map<char, int> map;

        for (int i = 0; i < s.length(); i++)
        {
            if (map.find(s[i]) == map.end())
            {
                map[s[i]] = count;
                count *= 2;
            }
            else if (map.find(s[i]) != map.end())
            {
                int temp = map[s[i]];
                map[s[i]] = count;
                count = count * 2;
                count = count - temp;
            }
        }

        return count;
    }

    string betterString(string str1, string str2)
    {
        int first = solve(str1);

        int second = solve(str2);

        // cout<<first<<" "<<second;

        if (first > second)
        {
            return str1;
        }
        else if (second > first)
        {
            return str2;
        }
        else if (first == second)
        {
            return str1;
        }

        return str1;
    }
};