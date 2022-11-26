/*
Q5.Create an adj matrix for directed graph.Check if there is a path between any 2 vertices of graph. 
*/
#include<iostream>
using namespace std;

class Graph
{
	int g[15][15];
	int start, n,dir,weighted;
	
	public:
		Graph()
		{
			cout<<"\n\n Enter number of vertices:";
			cin>>n;
			
			cout<<"\n Enter start vertices:";
			cin>>start;
			
			cout<<"\n Enter 0-Non-Directed 1-Directed:";
			cin>>dir;
			
			cout<<"\n Enter 0-Non-Weighted 1-Weighted:";
			cin>>weighted;
			
			for(int i=0;i<n;i++)
			{
				for(int j=0;j<n;j++)
				{
					g[i][j] = 0;	
				}	
			}	
		}	
		
		void readGraphByMatrix();
		void showGraphByMatrix();		
		void checkPath(int u,int v);
		void dfs(int*visited,int u);
};
void Graph::readGraphByMatrix()
{
	cout<<"\n\n Enter Graph Matrix:";
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			cout<<"\n Enter "<<i<<","<<j<<" vertex:";
			cin>>g[i][j];
		}
	}
}

void Graph::showGraphByMatrix()
{
	cout<<"\n\n Graph by Matrix:\n";
	
	for(int i=0;i<n;i++)
	{
		cout<<endl;
		for(int j=0;j<n;j++)
		{
			cout<<g[i][j]<<" ";
		}
	}
}

void Graph::checkPath(int u,int v)
{
	int visited[n];
	
	for(int i=0;i<n;i++)
		visited[i] = 0;
	
	dfs(visited,u);
	
	if(visited[u] == 1 && visited[v] == 1)
	{
		cout<<"\n\n Path Exists between "<<u<<" and "<<v;
	}
	else
	{
		cout<<"\n\n Path Doesn't Exists! between "<<u<<" and "<<v;
	}
}

void Graph::dfs(int *visited,int u)
{
	visited[u] = 1;
	
	for(int i=0;i<n;i++)
	{
		if( g[u][i] != 0 && visited[i] == 0 )
		{
			dfs(visited,i);	
		}
	}
}

int main()
{
	freopen("inputGraph.txt","r",stdin);
	Graph g;
	
	g.readGraphByMatrix();
	g.showGraphByMatrix();
	
	int u,v;
	cout<<"\n\n Enter path u,v to check:";
	cin>>u>>v;
	
	g.checkPath(u,v);
	
	return 0;
}
