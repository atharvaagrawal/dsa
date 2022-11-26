/*
Q2.Scan adjacency matrix for directed graph.
Check if this graph is connected or not from given source vertex

5
1
0
0
0 1 0 0 0
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 0 
0 1 0 0 0

*/

#include<iostream>

using namespace std;

class Graph
{
	int g[10][10];
	int n,dir,weighted;
	int start;
	
	public:
		Graph()
		{
			cout<<"\n\n Enter number of vertices:";
			cin>>n;
			
			cout<<"\n Enter 0-Un-Directed 1-Directed:";
			cin>>dir;
			
			cout<<"\n Enter 0-Non-Weighted 1-Weighted:";
			cin>>weighted;
			
			cout<<"\n Enter Start Vertex:";
			cin>>start;
			
			for(int i=0;i<n;i++)
			{
				for(int j=0;j<n;j++)
				{
					g[i][j] = 0;	
				}	
			}	
		}	
		
		void readGraphByAdj();
		
		void showGraphByAdj();
		void dfs(int*,int);
		void isConnected();
};

void Graph::showGraphByAdj()
{
	cout<<"\n\n Displaying Graph:";
	
	for(int i=0;i<n;i++)
	{
		cout<<endl;
		for(int j=0;j<n;j++)
		{
			cout<<g[i][j]<<" ";
		}
	}
	cout<<endl;
}

void Graph::readGraphByAdj()
{
	cout<<"\n Enter Matrix"<<n<<" Vertices:";
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			cout<<"\n Enter "<<g[i][j]<<":";
			cin>>g[i][j];
		}
	}
}

void Graph::dfs(int *visited,int v)
{
	visited[v] = 1;
	
	for(int i=0;i<n;i++)
	{
		if(visited[i] == 0 && g[v][i] != 0)
		{
			dfs(visited,i);	
		}		
	}
}


void Graph::isConnected()
{
	int *visited = new int[n];
	int i,j;
	
	for(i=0;i<n;i++)
	{
		visited[i] = 0;
	}
	
	int source;
	cout<<"\n\n Enter Source Vertex:";
	cin>>source;
	
	dfs(visited,source);
	
	int flag = 0;
	
	for(i=0;i<n;i++)
	{
		if(visited[i] == 0)
		{
			flag = 1;
			break;
		}
	}
	
	if(flag == 1)
	{
		cout<<"\n\n Graph is Not Connected!";
	}
	else
	{
		cout<<"\n\n Graph is Connected!";
	}
}


int main()
{
	Graph g;
	
	g.readGraphByAdj();
	g.showGraphByAdj();
	
	g.isConnected();
	
	
	return 0;
}
