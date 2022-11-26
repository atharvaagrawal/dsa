/*
Q8.WAP to color your graph using given 4 colors(r,g,b,y).Print all the possible combinations of colors
which can be used to color vertices of graph. No 2 adjacent vertices can have same color.

6
0
0
0
0 1
0 4
1 2
1 5
1 4 
2 3
2 5
3 5 
4 5
-1 -1
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
		
		void readGraphByEdges();
		void showGraphByAdj();
		
		void graphColoring();
		void colorMyVertex(int v);
		bool canIColor(int c,int v);
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

int *color;

void Graph::graphColoring()
{
	color = new int[n];
	
	for(int i=0;i<n;i++)
		color[i] = 0;
		
	
	cout<<"\n\n Printing All Possiblities:"<<endl;
	colorMyVertex(0);	
}

void Graph::colorMyVertex(int v)
{
	if(v == n)
	{
		char colorarr[] = {'r','b','g','y'};
		
		for(int i=0;i<n;i++)
		{
			cout<<colorarr[color[i]-1]<<" ";
		}
		cout<<endl;
	}
	else
	{
		for(int c=1;c<=4;c++)
		{
			if(canIColor(c,v))
			{
				color[v] = c;
				colorMyVertex(v+1);
			}
		}
		
		color[v] = 0;
	}
}

bool Graph::canIColor(int c,int v)
{
	for(int i=0;i<n;i++)
	{
		if(g[v][i] != 0 && color[i] == c)	
		{
			return false;
		}
	}	
	
	return true;
}

int main()
{
	Graph g;	
	
	g.readGraphByEdges();
	g.showGraphByAdj();
	
	g.graphColoring();
	
	return 0;
}
