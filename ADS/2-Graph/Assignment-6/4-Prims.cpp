/*
	Prims Algorithm
	
6
0
0
1
0 1 1
0 2 4
0 3 3
1 4 4
4 3 6
4 5 1
3 5 5
2 5 2
-1 -1 -1

	
*/

#include<iostream>
#define INF INT_MAX

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
		
		void prims(int);
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

void Graph::prims(int source)
{
	int cost[20][20];
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(g[i][j] == 0)
			{
				cost[i][j] = INF;
			}
			else
			{
				cost[i][j] = g[i][j];
			}
		}
	}
	
	int visited[n];
	int distance[n];
	int from[n];
	
	for(int i=0;i<n;i++)
	{
		visited[i] = 0;
		distance[i] = cost[source][i];
		from[i] = source;
	}
	
	visited[source] = 1;
	distance[source] = 0;
	
	int min,min_cost = 0;
	int v;
	
	cout<<"\n\n MST Using Prims:";
	for(int k=0;k<n-1;k++)
	{
		// 1 Find Min Distance
		min = INF;	
		
		for(int i=0;i<n;i++)
		{
			if(visited[i] == 0 && distance[i] < min)
			{
				min = distance[i];
				v = i;
			}
		}
		
		visited[v] = 1;
		min_cost+=distance[v];
		cout<<"\n Add Edge ("<<from[v]<<","<<v<<")";
		
		// 2. Update Remaning Unvisited Vertices
		for(int i=0;i<n;i++)
		{	
			if(visited[i]==0 && distance[i] > cost[v][i] )
			{
				distance[i] = cost[v][i];
				from[i] = v;
			}
		}
	}
	
	cout<<"\n\n Minimum Cost:"<<min_cost;
	
	cout<<"\n\n Visited Array:";
	for(int i=0;i<n;i++)
	{
		cout<<visited[i]<<" ";
	}

	cout<<"\n\n Distance Array:";
	for(int i=0;i<n;i++)
	{
		cout<<distance[i]<<" ";
	}
	
	cout<<"\n\n From Array:";
	for(int i=0;i<n;i++)
	{
		cout<<from[i]<<" ";
	}	
}
		
int main()
{
	freopen("inputGraph.txt","r",stdin);
	Graph g;
	
	g.readGraphByEdges();
	g.showGraphByMatrix();
	
	
	g.prims(0);
	
	return 0;
}
