/*
Q10.Scan adjacency matrix of graph.Find transitive closure by using matrix multiplication.
Use operator overloading to find powers of matrix and addition of matrix.

5
1
0
0
0 1
0 3
1 2
3 2
2 4
1 4
-1 -1

0 1 0 1 0
0 0 1 0 1
0 0 0 0 1
0 0 1 0 0
0 0 0 0 0

7
1
0
0
0 0 1 0 0 1 0 
0 0 0 0 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 0 0 1 0 0
0 0 0 1 0 0 0

*/

#include <iostream>
using namespace std;

// Matrix addition
int** matrixAddition(int **num1, int **num2, int n)
{
	int **res = new int*[n];

	for (int i = 0; i < n; i++)
	{
		res[i] = new int[n];
		for (int j = 0; j < n; j++)
		{
			res[i][j] = num1[i][j] + num2[i][j];
		}
	}
	return res;
}

// matrixMultiplication
//n : size of matrix
int** matrixMultiplication(int **num1, int **num2, int n)
{
	int **res = new int*[n];

	for (int i = 0; i < n; i++)
	{
		res[i] = new int[n];
		for (int j = 0; j < n; j++)
		{
			res[i][j] = 0;
			for (int k = 0; k < n; k++)
			{
				res[i][j] += num1[i][k] * num2[k][j];
			}
		}
	}
	return res;
}


class Graph
{
	int g[10][10];
	int n, dir, weighted;
	int start;

public:
	Graph()
	{
		cout << "\n\n Enter number of vertices:";
		cin >> n;

		cout << "\n Enter 0-Un-Directed 1-Directed:";
		cin >> dir;

		cout << "\n Enter 0-Non-Weighted 1-Weighted:";
		cin >> weighted;

		cout << "\n Enter Start Vertex:";
		cin >> start;

		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				g[i][j] = 0;
			}
		}
	}

	void readGraphByAdj();
	void showGraphByAdj();
	void transitiveClosure();

	// matrix addition
	//		int** operator+(int **num2)
	//		{
	//			int res[n][n];
	//
	//			for(int i=0;i<n;i++)
	//			{
	//				for(int j=0;j<n;j++)
	//				{
	//					res[i][j] = num[i][j];
	//				}
	//			}
	//		}

};

void Graph::showGraphByAdj()
{
	cout << "\n\n Displaying Graph:";

	for (int i = 0; i < n; i++)
	{
		cout << endl;
		for (int j = 0; j < n; j++)
		{
			cout << g[i][j] << " ";
		}
	}
	cout << endl;
}

void Graph::readGraphByAdj()
{
	cout << "\n Enter Matrix" << n << " Vertices:";

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << "\n Enter " << i+j << ":";
			cin >> g[i][j];
		}
	}
}

// transitive closure a + a2 + a3 + an
void Graph::transitiveClosure()
{
	int a[n][n][n];

	int **org_g = new int*[n];
	int **a1 = new int*[n];
	int **res = new int*[n];

	// Getting a
	for (int i = 0; i < n; i++)
	{
		a1[i] = new int[n];
		res[i] = new int[n];
		org_g[i] = new int[n];

		for (int j = 0; j < n; j++)
		{
			org_g[i][j] = g[i][j];
			res[i][j] = g[i][j];
			a[0][i][j] = res[i][j];
		}
	}

	// matrix multiplication a2,a3,a4
	for (int i = 1; i < n; i++)
	{
		res = matrixMultiplication(res, org_g,n);

		// to copy the result obtain
		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < n; k++)
			{
				a[i][j][k] = res[j][k];
			}
		}
	}

	// Getting a
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			res[i][j] = g[i][j];
		}
	}

	// matrix addition
	for (int i = 1; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < n; k++)
			{
				a1[j][k] = a[i][j][k];
			}
		}
		res = matrixAddition(res, a1,n);
	}

	cout << "\n\n Transitive Closure:";
	for (int i = 0; i < n; i++)
	{
		cout << endl;	
		for (int j = 0; j < n; j++)
		{
			cout << res[i][j] << " ";
		}
	}
}


int main()
{
	Graph g;

	g.readGraphByAdj();
	g.showGraphByAdj();

	g.transitiveClosure();

	return 0;
}
