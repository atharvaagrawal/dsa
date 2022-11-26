/*
Q3-Scan adj matrix of a graph from user.Perform DFS on it.
*/
#include<iostream>

using namespace std;

class Graph
{
	int g[10][10];
	int start,n;
	int dir,weighted;
	
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
		
		
		void scanAdjMatrix();
		
		void showGraphByMatrix();
		
		void dfs(int start);
		
		void dfs_rec(int ver,int *visited);
};
	
void Graph::scanAdjMatrix()
{
	cout<<"\n\n Enter "<<n<<" Vertex Matrix:";
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			cout<<"\n\n Enter "<<i<<","<<j<<" vertex:";
			cin>>g[i][j];
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

void Graph::dfs(int start)
{
	int visited[n];
	
	for(int i=0;i<n;i++)
		visited[i] = 0;
		
	dfs_rec(start,visited);
}	
	
void Graph::dfs_rec(int ver,int *visited)
{
	cout<<"\n Visited "<<ver+start;
	visited[ver] = 1;
	
	for(int i=0;i<n;i++)
	{
		if( g[ver][i] != 0 && visited[i] == 0)
		{
			dfs_rec(i,visited);
		}
	}	
}

int main()
{
	freopen("inputGraph.txt","r",stdin);
	Graph g;
	
	g.scanAdjMatrix();
	
	g.showGraphByMatrix();
	
	g.dfs(0);
	return 0;
}
