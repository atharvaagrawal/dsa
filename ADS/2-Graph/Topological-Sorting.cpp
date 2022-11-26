/*
	Topological Sorting
	
6
1
0
0
0 1
1 3
2 3
2 5
3 5
3 4
-1 -1

topology not possible:
6
1
0
0
0 1
0 2
1 2
2 3
3 1
3 4
3 5
5 4
-1 -1
*/
#include<iostream>
#define INF 9999

using namespace std;

class Graph
{
	int g[10][10];
	int dir,weighted,start,n;
	
	public:
		Graph()
		{
			cout<<"\n\n Enter number of vertices:";
			cin>>n;
			
			cout<<"\n Enter 0-UnDirected 1-Directed:";
			cin>>dir;
			
			cout<<"\n Enter 0-Non-Weighted 1-Weighted:";
			cin>>weighted;
			
			cout<<"\n Enter start vertex:";
			cin>>start;
			
			for(int i=0;i<n;i++)
			{
				for(int j=0;j<n;j++)
				{
					g[i][j] = 0;
				}
			}
		}	
		
		void readGraphByEdge();
		void showGraphByMatrix();
		
		void topology();
};

void Graph::readGraphByEdge()
{
	cout<<"\n\n Enter Edges of the Graph:";
	int u,v,w;
	
	while(1)
	{
		if(weighted == 0)
		{
			cout<<"\n Enter u,v -1 to stop:";
			cin>>u>>v;
			
			if(u == -1 || v == -1)
			{
				break;
			}
			
			if(dir == 0)
			{
				g[u][v] = 1;
				g[v][u] = 1;
			}
			else
			{
				g[u][v] = 1;
			}			
		}
		else
		{
			cout<<"\n Enter u,v,w -1 to stop:";
			cin>>u>>v>>w;
			
			if(u == -1 || v == -1)
			{
				break;
			}
			
			if(dir == 0)
			{
				g[u][v] = w;
				g[v][u] = w;
			}
			else
			{
				g[u][v] = w;
			}			
		}
	}
}

void Graph::showGraphByMatrix()
{
	cout<<"\n\n Displaying Graph by Matrix:";
	
	for(int i=0;i<n;i++)
	{
		cout<<endl;
		for(int j=0;j<n;j++)
		{
			cout<<g[i][j]<<" ";
		}
	}
}

void Graph::topology()
{
	int visited[n];
	int indegree[n];
	
	for(int i=0;i<n;i++)
	{
		visited[i] = 0;
		indegree[i] = 0;
		
		for(int j=0;j<n;j++)
		{
			if(g[j][i] != 0)
			{
				indegree[i]++;
			}	
		}
	}
	
	int j;
	
	cout<<"\n\n Topology of Graph:";	
	
	for(int i=0;i<n;i++)
	{
		j = 0;
		
		while(j < n)
		{
			if(indegree[j] == 0 && visited[j] == 0)
			{
				cout<<"\n Vertex "<<j<<" visited";
				
				visited[j] = 1;
				
				for(int k=0;k<n;k++)
				{
					if(g[j][k] != 0 && visited[k] == 0)
					{
						indegree[k]--;
					}
				}
				break;
			}	
			
			j++;
		}	
		
		if(j == n)
		{
			cout<<"\n Cyclic graph So no Topolopology!";
			break;
		}
	}
}

int main()
{
	freopen("inputGraph.txt","r",stdin);
	
	Graph g;
	g.readGraphByEdge();
	g.showGraphByMatrix();
	g.topology();
	
	return 0;
}
