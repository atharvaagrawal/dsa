/*
Q3.Scan adj matrix for a directed graph.Check if graph is cyclic or not.

4
1
0
0
0 1 0 0
0 0 1 0
0 0 0 1
0 0 0 0
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

		int isCyclic();
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

int Graph::isCyclic()
{
	int *component = new int[n];
	
	for(int i=0;i<n;i++)
	{
		component[i] = i;
	}
	
	int i,j,cu,cv,u,v,k;
	
	for(i=0;i<=n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(g[i][j] != 0)
			{
				u = i;
				v = j;
				cu = component[u];
				cv = component[v];
				
				if(cu != cv)
				{
					// add edge
					
					// update component
					for(k = 0;k<n;k++)
					{
						if(component[k] == u)
						{
							component[k] = v;
						}
					}
				}
				else
				{
					return 0;
				}
			}
		}
	}
	
	return 1;
}

int main()
{
	Graph g;
	
	g.readGraphByAdj();
	
	g.showGraphByAdj();
	
	if(g.isCyclic())
	{
		cout<<"\n\n Graph is Not Cyclic";
	}
	else
	{
		cout<<"\n\n Graph is Cyclic";		
	}
	
	return 0;
}
