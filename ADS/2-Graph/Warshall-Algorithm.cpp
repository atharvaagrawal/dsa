/*
Warshall Algorithm
  
  directed:
4
0
1
0

0 1
1 0
1 2
2 3
-1 -1
*/

#include<iostream>
#define INF 9999
using namespace std;

class Graph
{
	int g[10][10];
	int weighted,dir,n,start;
	
	public:
		Graph()
		{
			cout<<"\n\n Enter number of vertices:";
			cin>>n;
			
			cout<<"\n Enter 0-Non-Weighted 1-Weighted:";
			cin>>weighted;
			
			cout<<"\n Enter 0-UnDirected 1-Directed:";
			cin>>dir;
			
			cout<<"\n Enter start vertice:";
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
		void degree();
		
		void indegree();
		void outdegree();
		
		void warshall();
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

void Graph::degree()
{
	if(dir == 0)
	{
		cout<<"\n Graph is UnDirected";
		outdegree();
	}
	else
	{
		cout<<"\n Graph is Directed";
		outdegree();
		indegree();
	}	
}
		
void Graph::indegree()
{
	cout<<"\n\n InDegree:";
	
	for(int i=0;i<n;i++)
	{
		cout<<"\n Indegree of "<<i+start<<":";
		for(int j=0;j<n;j++)
		{
			if(g[j][i] != 0)
			{
				cout<<j+start<<" ";
			}
		}
	}	
}

void Graph::outdegree()
{
	cout<<"\n\n OutDegree:";
	
	for(int i=0;i<n;i++)
	{
		cout<<"\n Outdegree of "<<i+start<<":";
		for(int j=0;j<n;j++)
		{
			if(g[i][j] != 0)
			{
				cout<<j+start<<" ";
			}
		}
	}
}

void Graph::warshall()
{
	cout<<"\n\n Transitive Closure using Warshall Algorithm:";
	int tc[10][10];
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(g[i][j] != 0)
			{
				tc[i][j] = 1; 	
			}
			else
			{
				tc[i][j] = 0;
			}		
		}
	}
	
	for(int k=0;k<n;k++)
	{
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(tc[i][j] == 0)
				{
					if(tc[i][k] == 1 && tc[k][j] == 1)
					{
						tc[i][j] = 1;				
					}
				}
			}
		}
	}
	
	for(int i=0;i<n;i++)
	{
		cout<<endl;
		for(int j=0;j<n;j++)
		{
			cout<<tc[i][j]<<" ";
		}
	}
	
}

int main()
{
	freopen("inputGraph.txt","r",stdin);
	
	Graph g;
	g.readGraphByEdge();
	g.showGraphByMatrix();
	g.degree();	
	
	g.warshall();
	
	return 0;
}

