/*
Q5.Scan edges from user for an undirected graph.Create adjacency list.Perform nonrecursive 
DFS to check if graph is connected or not.Print number of components of a graph.

4
0
0
0
0 1
1 2 
2 3 
3 0
-1 -1

6
1
0
0
0 1
0 3
1 0
1 4
2 5
3 4
4 1
4 3
4 5
5 2
-1 -1

8
0
0
0
0 1
0 2
1 2
1 4
1 3
2 3
2 4
3 4
5 6 
5 7
-1 -1

*/

#include<iostream>
#define MAX 100
using namespace std;

class Stack
{
	int top;
	int data[MAX];
	
	public:
		Stack()
		{
			top = -1;
		}
		
		int isEmpty()
		{
			if(top == -1)
				return 1;
			return 0;
		}
		
		int isFull()
		{
			if( top == MAX)
				return 1;
			return 0;
		}
		int pop()
		{
			if(!isEmpty())
				return data[top--];
			return -1;
		}
		void push(int val)
		{
			if(!isFull())
			{
				top++;
				data[top] = val;
			}
			else
			{
				cout<<"\n\n Stack is Full";
			}
		}
};

class Node
{
	public:
		int weight,vertex;
		Node *next;
		
		Node()
		{
			weight = vertex = -1;
			next = NULL;	
		}	
		
		Node(int v,int w =1)
		{
			vertex = v;
			weight = w;
			next = NULL;	
		}		
};

class Graph
{
	Node* head[15];
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
				head[i] = NULL;
			}	
		}		
		
		void readGraphByEdges();
		void showGraphByAdjList();
		void insert(int,int,int);
		void dfs_non_rec(int source,int *visited);
		
		void isConnected();		
		void numComponents();
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
				insert(u,v,w);
				insert(v,u,w);
			}
			else
			{
				insert(u,v,w);
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
				insert(u,v,1);
				insert(v,u,1);
			}
			else
			{
				insert(u,v,1);
			}			
		}	
	}
}

void Graph::insert(int u,int v,int w=1)
{
	Node* temp = head[u];
	
	if(temp == NULL)
	{
		head[u] = new Node(v,w);
	}
	else
	{
		while(temp->next != NULL)
		{
			temp = temp->next;
			
			if(temp->vertex == v)
			{
				cout<<"\n\n Vertex Already Present!";
				return;
			}
		}
		
		temp->next = new Node(v,w);
	}
}

void Graph::showGraphByAdjList()
{
	cout<<"\n\n Displaying Graph:";
	
	Node *temp;

	for(int i=0;i<n;i++)
	{
		cout<<"\n Vertex "<<i<<":";
		temp = head[i];
		
		while(temp != NULL)
		{
			cout<<temp->vertex<<" ";
			temp = temp->next;			
		}
	}

}

// to check graph connected or not
void Graph::dfs_non_rec(int source,int *visited)
{
	Stack s;
	Node *temp;
	int i;
	
	s.push(source);
	
	temp = head[source];
	
	while(temp != NULL)
	{
		s.push(temp->vertex);
		temp = temp->next;
	}
	
//	cout<<"\n\n Non-Recursive DFS: ";
//	cout<<source<<" ";
	
	visited[source] = 1;
	int v;
	
	while( !s.isEmpty() )
	{
		v = s.pop();
		
		if(visited[v] == 0)
		{
//			cout<<v<<" ";	
			visited[v] = 1;		
			
			temp = head[v];
	
			while(temp != NULL)
			{
				if(visited[temp->vertex] == 0)
				{
					s.push(temp->vertex);
				}			
				temp = temp->next;
			}
		}	 
	}

}

void Graph::isConnected()
{
	int *visited = new int[n];
	int i;
	for(i=0;i<n;i++)
		visited[i] = 0;
	
	dfs_non_rec(0,visited);
	
	int flag = 0;
	
	for(int i=0;i<n;i++)
	{
		if(visited[i] == 0)
		{
			flag = 1;
			break;
		}	
	}
	
	if(flag)
	{
		cout<<"\n\n Graph is Not Connected!";
	}
	else
	{
		cout<<"\n\n Graph is Connected!";
	}
}

void Graph::numComponents()
{
	int *visited = new int[n];
	int c = 0;
	int i;
	
	for(i=0;i<n;i++)
		visited[i] = 0;
	
	dfs_non_rec(0,visited);
	c++;
	
	int flag = 0;
	for(int i=0;i<n;i++)
	{
		if(visited[i] == 0)
		{
			dfs_non_rec(i,visited);
			c++;
		}	
	}
	
	cout<<"\n\n Number of Componenets:"<<c;
}

int main()
{
	Graph g;	
	
	g.readGraphByEdges();
	g.showGraphByAdjList();	
	
	g.isConnected();
	
	g.numComponents();
	
	return 0;
}
