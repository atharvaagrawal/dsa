/*
BFS

6
0
0
0

0 1
0 2
1 3
1 4
2 3
2 5
4 3
4 5
5 3
-1 -1
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
			vertex = weight = -1;
			next = NULL;
		}

		Node(int v,int w=1)
		{
			vertex = v;
			weight = w;
			next = NULL;
		}			
};

class Queue
{
	int front,rear;
	int data[100];
	int n;
	
	public:
		Queue()
		{
			front=rear=-1;
			n = 100;
		}
		
		int isEmpty()
		{
			if(front == -1 || front > rear)
			{
				return 1;	
			}	
			return 0;
		}
		
		int isFull()
		{
			if( rear == n-1 )
			{
				return 1;
			}
			return 0;
		}
		
		void enqueue(int val)
		{
			if( isFull() )
			{
				cout<<"\n\n Queue is Full !";	
				return;
			}
			else
			{
				if(front == -1)
					front++;
				
				rear++;
				data[rear] = val;			
			}
		}	
		
		int dequeue()
		{
			if(isEmpty())
			{
				cout<<"\n\n Queue is Underflow! ";
				return -1;
			}
			else
			{
				int res = data[front];
				front++;
				return res;
			}
		}			
};

class Graph
{
	Node *head[15];
	int dir,weighted,n;
	int start;
	
	public:
		Graph()
		{
			cout<<"\n\n Enter Number of vertices:";
			cin>>n;
			
			cout<<"\n Enter start vertices:";
			cin>>start;
			
			cout<<"\n Enter 1-Directed 0-Non-Directed:";
			cin>>dir;
			
			cout<<"\n Enter 1-Weighted 0-Non-Weighted:";
			cin>>weighted;		
			
			for(int i=0;i<n;i++)
			{
				head[i] = NULL;
			}
		}
		
		
		void bfs(int v);	
		void readGraphByEdges();
		void insert(int u,int v,int w);
};

void Graph::bfs(int v)
{
	int visited[n];
	
	for(int i=0;i<n;i++)
		visited[i] = 0;
	
	Queue q;
	
	cout<<"\n\n BFS:";
	cout<<"\n Visit: "<<v;
	q.enqueue(v);
	
	visited[v] = 1;
	
	while( !q.isEmpty())
	{
		v = q.dequeue();
		
		Node *p = head[v];
		
		while(p != NULL)
		{
			if(visited[p->vertex] == 0 )
			{
				cout<<"\n Visit: "<<p->vertex;
				q.enqueue(p->vertex);
				visited[p->vertex] = 1;
			}
			
			p = p->next;
		}
	}
}

void Graph::readGraphByEdges()
{
	cout<<"\n\n Enter "<<n<<" vertices Edges:";
	int u,v,w;
	
	while(1)
	{
		if(weighted == 0)
		{
			cout<<"\n Enter u,v Edges:";
			cin>>u>>v;
			
			if(u == -1 || v == -1)
				return;
			
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
		else
		{
			cout<<"\n Enter u,v,w Edges:";
			cin>>u>>v>>w;
			
			if(u == -1 || v == -1)
				return;
			
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
	}
}

void Graph::insert(int u,int v,int w=1)
{
	Node *p = head[u];
	
	if( p == NULL)
	{
		head[u] = new Node(v,w);
	}
	else
	{
		while(p->next != NULL)
		{
			if(p->vertex == v)
			{
				cout<<"\n\n Vertex Already Present!";
				return;
			}
			p = p->next;
		}
		
		p->next = new Node(v,w);
	}
}


int main()
{
	Graph g;
	g.readGraphByEdges();
	g.bfs(0);

	return 0;
}
