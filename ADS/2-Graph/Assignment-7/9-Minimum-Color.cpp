/* Q9.Scan adj matrix for graph from user.Scan number of colors from user.Check if these colors 
are enough to color the graph such that no 2 adj vertices can have same colors.If colors are enough 
print all the possible combinations of colors.If given colors are not enough,tell him
minimum number of colors required to color his graph.
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

