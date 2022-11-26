/*
	Kruskal's Algorithm
	
	
6

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

using namespace std;

class Edge
{
	public:
		int u,v,w;	
};

		
void kruskals()
{
	// steps: 1) take input edges
	cout<<"\n Enter number of vertices:";
	int n;
	cin>>n;
	
	Edge list[n];
	
	cout<<"\n\n Enter Edges:";
	int u,v,w,i=0;
	
	while(1)
	{
		cout<<"\n Enter u,v,w -1 to stop:";
		cin>>u>>v>>w;
		
		if(u == -1 || v == -1 || w == -1)
			break;
		
		list[i].u = u;
		list[i].v = v;
		list[i].w = w;
		
		i++;
	}
	
	// 2) sort edges according to weight
	
	int edge_count = i;
	
	for(i = 0;i< edge_count-1;i++)
	{
		for(int j=0;j<edge_count-1-i;j++)
		{
			if(list[j].w > list[j+1].w)
			{
				Edge temp = list[j];
				
				list[j] = list[j+1];
				
				list[j+1] = temp;
			}
		}
	}
	
	cout<<"\n\n Displaying Edge list after sort:";
	cout<<"\n U \t V \t W"<<endl;
	for(i = 0;i<edge_count;i++)
	{
		cout<<list[i].u<<"\t"<<list[i].v<<"\t"<<list[i].w<<endl;
	}
	
	
	// 3) Add edge one by one without creating cycle
	
	int component[n];
	
	for(i=0;i<n;i++)
		component[i] = i;
	
	i = 0;
	int cu,cv; 
	cout<<"\n\n Minimum Cost Spanning Tree:";
	int mincost = 0;	
	
	i = 0;
	int ne = n-1;
	
	while(ne > 0)
	{
		u = list[i].u;
		v = list[i].v;
		w = list[i].w;
		
		cu = component[u];
		cv = component[v];
		
		if( cu != cv )
		{
			mincost += w; 
			cout<<"\n Add Edge ("<<u<<","<<v<<")";
			
			for(int j=0;j<n;j++)
			{
				if( component[j] == cu )
				{
					component[j] = cv;
				}
			}
		}
		
		i++;
		ne--;	
	}
	
	cout<<"\n\n Minimum Cost:"<<mincost;
}


int main()
{
	freopen("inputGraph.txt","r",stdin);
	
	kruskals();
	
	return 0;
}
