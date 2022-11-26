/*
	Warshall's Algorithm
*/

#include<iostream>

using namespace std;

class Graph
{
	int g[20][20];
	int n;
	int start,dir,weighted;
	
	public:
		Graph()
		{
			cout<<"\n Enter number of vertices:";
			cin>>n;
			
			cout<<"\n Enter start vertex:";
			cin>>start;
			
			cout<<"\n Enter 0-UnDirected 1-Directed:";
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
		
		void readGraphByEdges();
		void showGraphByMatrix();
		
		void insert(int u,int v,int w);
		
		void warshall();
};

void Graph::readGraphByEdges()
{
	cout<<"\n Enter Edges of the Graph: ";
	
	int u,v,w;
	
	while(1)
	{
		if(weighted == 1)
		{
			cout<<"\n Enter u,v,w -1 to Stop:";
			cin>>u>>v>>w;
			
			if(u == -1 || v == -1 || w == -1)
			{
				break;
			}
				
			insert(u,v,w);
		}
		else
		{
			cout<<"\n Enter u,v -1 to Stop:";
			cin>>u>>v;
			
			if(u == -1 || v == -1 )
			{
				break;
			}
				
			insert(u,v,1);			
		}
	}
}

void Graph::insert(int u,int v,int w = 1)
{
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
	cout<<"\n\n";
}

void Graph::warshall()
{
	cout<<"\n Warshall Algorithm";
	
	// transitive closure
	int tc[20][20];
	
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
				if( tc[i][k] != 0 && tc[k][j] != 0)
				{
					tc[i][j] = 1;	
				}			
			}
		}
	}
	
	cout<<"\n\n Transitive Closure:";
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
	
	g.readGraphByEdges();
	g.showGraphByMatrix();
	
	g.warshall();
	return 0;
}
