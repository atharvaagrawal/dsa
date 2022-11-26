/*
Q2-Scan edges from user.Create adj list.Check if given graph is connected or not.
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

		Node(int v,int w=1)
		{
			vertex = v;
			weight = w;
			next = NULL;
		}	
};

class Graph
{
	Node *head[15];
	int start,dir;
	int n,weighted;
	
	public:
		Graph()
		{
			cout<<"\n\n Enter Number of Vertices:";
			cin>>n;
			
			cout<<"\n Enter 0-Directed 1-Directed:";
			cin>>dir;
			
			cout<<"\n Enter 0-Weighted 1-Weighted:";
			cin>>weighted;
			
			cout<<"\n Enter Starting Vertices:";
			cin>>start;
			
			for(int i=0;i<n;i++)
			{
				head[i] = NULL;
			}
		}
		
		void readGraphByEdges();
		void showGraphByEdges();
		
		void insert(int u,int v,int w);	
		
		void dfs(int *visited,int ver);
		void connected();
};

void Graph::dfs(int *visited,int ver)
{
	visited[ver] = 1;
	
	Node *t;
	
	t = head[ver];
		
	while(t != NULL)
	{		
		if( visited[t->vertex] == 0)
		{
			dfs(visited , t->vertex);
		}
		t = t->next;
	}
}		


void Graph::connected()
{
	int visited[n];
	int i;
	
	for(i=0;i<n;i++)
	{
		visited[i] = 0;
	}			
	
	dfs(visited,start);
	
	for(i=0;i<n;i++)
	{
		if(visited[i] == 0)
		{
			break;
		}
	}
	
	if(i == n)
	{
		cout<<"\n\n Graph is Connected!";
	}
	else
	{
		cout<<"\n\n Graph is not Connected!";
	}
}

void Graph::readGraphByEdges()
{
	cout<<"\n\n Enter "<<n<<" Edges:";
	int u,v,w;
	
	while(1)
	{
		if(weighted == 0)
		{
			cout<<"\n Enter u,v edges:";
			cin>>u>>v;
			
			if(u == -1)
			{
				break;
			}
			
			insert(u,v,1);
					
			if(dir == 0)
			{
				insert(v,u,1);
			}	
		}
		else
		{
			cout<<"\n Enter u,v,w edges:";
			cin>>u>>v>>w;
			
			if(u == -1)
			{
				break;
			}
						
			insert(u,v,w);
	
			if(dir == 0)
			{
				insert(v,u,w);
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
		if(t->vertex == v)
		{
			return;
		}
		t = t->next;
	}
	
	t->next = new Node(v,w); 
}

void Graph::showGraphByEdges()
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


int main()
{
	freopen("inputGraph.txt","r",stdin);
	
	Graph g;
	g.readGraphByEdges();
	
	cout<<"\n\n Displaying Graph:";
	g.showGraphByEdges();
	
	g.connected();
	return 0;
}

