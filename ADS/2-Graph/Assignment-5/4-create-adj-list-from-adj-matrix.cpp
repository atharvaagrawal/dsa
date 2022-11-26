/*
Q4-Create adj list from adj matrix.Check if graph is connected or not.
Print number of components.
*/

#include<iostream>
using namespace std;

class Node
{
	public:
		int vertex;
		int weight;
		Node *next;
		
		Node()
		{
			vertex = -1;
			weight = 0;
			next = NULL;
		}

		Node(int v,int w)
		{
			vertex = v;
			weight = w;
			next = NULL;
		}
};

class Graph
{
	Node *head[15];
	
	int g[15][15];
	
	int start,dir,n,weighted;
	
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
			
			for(int i=0;i<n;i++)
				head[i] = NULL;	
		}	
		
		void readGraphByMatrix();
		
		void showAdjList();
		
		void isConnected();
		
		void noComponent();
		
		void dfs(int ver,int *visited);
		
		void insert(int u,int v,int w);
};

void Graph::readGraphByMatrix()
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
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(g[i][j] != 0)
			{
				insert(i,j,g[i][j]);	
			}		
		}	
	}
}
		
void Graph::insert(int u,int v,int w=1)
{
	Node *t;
	t = head[u];
	
	if(t == NULL)
	{
		head[u] = new Node(v,w);	
		return;
	}	
	
	while(t->next != NULL)
	{
		t =  t->next;
	}
	
	t->next = new Node(v,w);
}

void Graph::showAdjList()
{
	Node *t;
	
	for(int i=0;i<n;i++)
	{
		t = head[i];
		
		cout<<"\n\n Vertex "<<i+start<<" Edges:"<<endl;
		
		while(t!=NULL)
		{
			cout<<t->vertex<<"="<<t->weight<<endl;
			t = t->next;
		}
	}
}
		
void Graph::isConnected()
{
	int visited[n];
	int i;
	
	for(i=0;i<n;i++)
		visited[i] = 0;
	
	
	dfs(start,visited);
	
	for(i=0;i<n;i++)
	{
		if(visited[i] == 0)
		{
			break;
		}
	}
	
	if(i == n)
		cout<<"\n\n Graph is Connected!";
	else
		cout<<"\n\n Graph is not Connected!";
}
		
void Graph::noComponent()
{
	int c = 0;
	
	int visited[n];
	
	for(int i=0;i<n;i++)
		visited[i] = 0;
	
	for(int i=0;i<n;i++)
	{
		if(visited[i] == 0)
		{
			dfs(i,visited);
			c++;
		}	
	}
	
	cout<<"\n\n Number of Components:"<<c;
}
		
void Graph::dfs(int ver,int *visited)
{
	visited[ver] = 1;
	
	Node *t;
	t = head[ver];
	
	while(t != NULL)
	{
		if(visited[t->vertex] == 0)
		{
			dfs(t->vertex,visited);
		}	
		
		t = t->next;
	}
}
		
int main()
{
	freopen("inputGraph.txt","r",stdin);
	
	Graph g;
	
	g.readGraphByMatrix();
	
	g.showAdjList();
	
	g.isConnected();
	
	g.noComponent();
	return 0;
}
