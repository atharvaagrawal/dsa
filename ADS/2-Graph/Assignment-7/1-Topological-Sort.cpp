/*
	Q1.WAP to implement topological sort.

6
1
0
0
0 1
0 2
1 3
2 3
1 4
3 5
5 4
-1 -1 


3
1
0
0
0 1
1 2 
2 0
-1 -1
*/

#include<iostream>

using namespace std;

class Graph
{
	int **g;
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
			
			g = new int*[n];
				
			for(int i=0;i<n;i++)
			{
				g[i] = new int[n];
				
				for(int j=0;j<n;j++)
				{	
					g[i][j] = 0;	
				}	
			}	
		}		
		
		void readGraphByEdges();
		void showGraphByAdj();
		void topology();
};

void Graph::readGraphByEdges()
{
	cout<<"\n\n Enter "<<n<<" Vertices:";
	
	int u,v,w;
	
	while(1)
	{
		if(weighted == 1)
		{
			cout<<"\n Enter u,v,w -1 to stop:";
			cin>>u>>v>>w;
			if(v == -1 || u == -1 )
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
		else
		{
			cout<<"\n Enter u,v -1 to stop:";
			cin>>u>>v;
			if(v == -1 || u == -1 )
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
	}
}

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


void Graph::topology()
{
	int *visited = new int[n];
	int *indegree = new int[n];
	int i,j,c;
	
	// 1. initialize
	
	for(i=0;i<n;i++)
	{
		visited[i] = 0;
		indegree[i] = 0;
	}
	
	// 2. find indegree
	
	for(i=0;i<n;i++)
	{
		c = 0;
		
		for(j=0;j<n;j++)
		{
			if(g[j][i] != 0)
			{
				c++;
			}
		}
		
		indegree[i] = c;
	}
	
	cout<<"\n Topological Sort: ";
	
	int v, ne;
	
	ne = n;
	
	// 3. find indegree 0
	while(ne > 0)
	{
		int flag = 0;
		for(i=0;i<n;i++)
		{
			if(indegree[i] == 0 && visited[i] == 0)
			{
				cout<<i<<" ";	
				flag = 1;
				break;
			}	
		}
				
		if(flag == 0)
		{
			cout<<"\n Topological Sort not possible!";
			break;
		}
		
		// Update 
		v = i;
		visited[v] = 1;
		
		for(i = 0;i<n;i++)
		{
			if(g[v][i] != 0)
			{
				indegree[i]--;
			}
		}
		
		ne--;
	}
}

int main()
{
	Graph g;
	
	g.readGraphByEdges();
	g.showGraphByAdj();
	
	g.topology();
	
	return 0;	
}	
