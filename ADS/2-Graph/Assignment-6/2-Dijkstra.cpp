/*
	Dijkstra's Algorithm
	
8
0
0
1

0 1 3
0 3 2
1 2 1
1 6 2
2 4 4
4 5 3
3 5 2
5 7 1
6 7 3
-1 -1 -1

0	
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
		
		void dijkstra(int);
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

void Graph::dijkstra(int source)
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
	
	int min;
	int v;
	
	for(int k=0;k<n;k++)
	{
		// 1 Find Min Distance
		min = INF;	
		
		for(int i=0;i<n;i++)
		{
			if(visited[i] == 0 && distance[i] < min )
			{
				min = distance[i];
				v = i;
			}
		}
		
		visited[v] = 1;
		
		// 2. Update Remaning Unvisited Vertices
		for(int i=0;i<n;i++)
		{
			if(cost[v][i] == INF)
			{
				continue;
			}
			
			if(visited[i]==0 && distance[i] > (distance[v]+cost[v][i]) )
			{
				distance[i] = distance[v] + cost[v][i];
				from[i] = v;
			}
		}
	}
	
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
	
	cout<<"\n\n Displaying Path:";
	cout<<"\n Source Vertex:"<<source;
	
	for(int i=0;i<n;i++)
	{
		cout<<"\n Path of "<<i<<" Vertex:";
		v = i;
		
		while(from[v] != source )		
		{
			cout<<from[v]<<" ";
			v = from[v];
		}
		cout<<source;
	}
	
}
		
int main()
{
	freopen("inputGraph.txt","r",stdin);
	Graph g;
	
	g.readGraphByEdges();
	g.showGraphByMatrix();
	
	int s;
	cout<<"\n Enter source vertex for dijkstra:";
	cin>>s;
	
	g.dijkstra(s);
	
	return 0;
}
