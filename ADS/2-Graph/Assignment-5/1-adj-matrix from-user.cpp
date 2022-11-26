/*
Q1-Scan adj matrix from user.Create an adjacency list from it.
Check the possibilities of directed,undirected,weighted,nonweighted.
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
			weight = 1;
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
	int g[10][10];
	int dir, n, wt, start;
	
	Node* head[15];
		
	public:
		Graph()
		{
			cout<<"\n\n Enter number of vertices:";
			cin>>n;
			
			cout<<"\n Enter 1-Directed 0-UnDirected:";
			cin>>dir;
			
			cout<<"\n Enter 1-Weighted 0-UnWeighted:";
			cin>>wt;
			
			cout<<"\n Enter Start Vertice:";
			cin>>start;	
			
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

		void readGraphByAdjMatrix();
		
		void showGraphByAdjMatrix();
		
		void showGraphByAdjList();
		
		void insert(int u,int v,int w);
};

void Graph::readGraphByAdjMatrix()
{
	cout<<"\n\n Enter Adjacency Matrix for "<<n<<" vertices:";
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			cin>>g[i][j];
		}
	}	
}

void Graph::showGraphByAdjMatrix()
{
	cout<<"\n\n Adjacency Matrix for "<<n<<" vertices:\n";
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			cout<<g[i][j]<<" ";
		}
		cout<<"\n";
	}		
	
	// creating adjacency list
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

void Graph::insert(int u,int v,int w)
{
	Node *t = head[u];
	
	if(t == NULL)
	{
		head[u] = new Node(v,w);
		return;
	}
	
	while(t->next != NULL)
	{	
		t = t->next;
	}
	
	t->next = new Node(v,w);
}



void Graph::showGraphByAdjList()
{
	Node *t;
	
	for(int i=0;i<n;i++)
	{
		t = head[i];
		
		cout<<"\n Vertex of "<<i+start<<" :\n";
		
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
	
	g.readGraphByAdjMatrix();
	
	cout<<"\n\n Show graph by Adjancency Matrix:";
	g.showGraphByAdjMatrix();
	
	cout<<"\n\n Show graph by Adjancency List:";
	g.showGraphByAdjList();
	return 0;
}
