#include <iostream>
#include <bits/stdc++.h>

using namespace std;

struct Node
{
    int source, destination, weight;
};

void bellmanFord(int vertices, int n, struct Node *graph)
{
    int distance[vertices], distance_check[vertices];

    distance[0] = 0;
    distance_check[0] = 0;

    // Step 1 : Assigning Max Distance
    for (int i = 1; i < vertices; i++)
    {
        distance[i] = INT_MAX;
        distance_check[i] = INT_MAX;
    }

    // Step 2 : Calculate Calculation
    // Number of Vertices -1
    int total_exection = vertices - 1;

    // Step 3 : Check the
    int flag_ans = 0;
    int flag = 1;
    for (int j = 0; j < total_exection; j++)
    {
        flag = 1;
        for (int i = 0; i < n; i++)
        {
            int check = distance[graph[i].source - 1] + graph[i].weight;

            // cout<<graph[i].source<<" "<< graph[i].destination<<endl;

            // cout<<check<<" "<<distance[graph[i].destination - 1]<<endl;

            if (check < distance[graph[i].destination - 1])
            {
                distance[graph[i].destination - 1] = check;
            }

            // cout<<check<<" "<<distance[graph[i].destination - 1]<<endl<<endl;
        }

        for (int i = 0; i < vertices; i++)
        {
            if (distance_check[i] != distance[i])
            {
                flag = 0;
                break;
            }
        }

        for (int i = 0; i < vertices; i++)
        {
            distance_check[i] = distance[i];
        }

        if (flag == 1)
        {
            flag_ans = 1;
            cout << "\n\n Distance:" << endl;
            for (int i = 0; i < vertices; i++)
            {
                cout << "d[" << i + 1 << "] =" << distance[i] << endl;
            }
            break;
        }
    }

    if (flag_ans == 0)
    {
        cout << "\n\n Negative Edge Cycle Present" << endl;
    }
}

int main()
{
    freopen("input.txt", "r", stdin);

    int n, vertices;

    cout << "\n\n Enter Number of Vertices:";
    cin >> vertices;

    cout << "\n\n Enter Number of Edge List:";
    cin >> n;

    struct Node graph[n];

    // Taking Input
    for (int i = 0; i < n; i++)
    {
        cout << "\n Enter " << i + 1 << " Source, Destination and Weight:";
        cin >> graph[i].source >> graph[i].destination >> graph[i].weight;
    }

    // Printing Data
    cout << "\n\n Input Data:";
    cout << "\n Source \t Dest \t Weight" << endl;
    for (int i = 0; i < n; i++)
    {
        cout << graph[i].source << "\t" << graph[i].destination << "\t" << graph[i].weight << endl;
    }

    bellmanFord(vertices, n, graph);

    return 0;
}

/*
OUTPUT:
-------
1) Negative Edge Cycle

 Enter Number of Vertices:

 Enter Number of Edge List:
 Enter 1 Source, Destination and Weight:
 Enter 2 Source, Destination and Weight:
 Enter 3 Source, Destination and Weight:
 Enter 4 Source, Destination and Weight:
 Enter 5 Source, Destination and Weight:

 Input Data:
Source Dest    Weight
1       2       4
1       4       5
2       4       5
4       3       3
3       2       -10


 Negative Edge Cycle Present

2) No Negative Edge Cycle:

 Enter Number of Vertices:

 Enter Number of Edge List:
 Enter 1 Source, Destination and Weight:
 Enter 2 Source, Destination and Weight:
 Enter 3 Source, Destination and Weight:
 Enter 4 Source, Destination and Weight:
 Enter 5 Source, Destination and Weight:
 Enter 6 Source, Destination and Weight:
 Enter 7 Source, Destination and Weight:
 Enter 8 Source, Destination and Weight:
 Enter 9 Source, Destination and Weight:
 Enter 10 Source, Destination and Weight:

 Input Data:
 Source Dest    Weight
1       2       6
1       3       5
1       4       5
2       5       -1
3       2       -2
3       5       1
4       3       -2
4       6       -1
5       7       3
6       7       3


 Distance:
d[1] =0
d[2] =1
d[3] =3
d[4] =5
d[5] =0
d[6] =4
d[7] =3
*/