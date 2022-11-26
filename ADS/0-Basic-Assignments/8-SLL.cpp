/*
Q8.Create an SLL.Implement following functions.
-createrec()
-showrec()
-showrevrec()
-countrec()
-searchrec()
-makeemptyrec()
-deleteatendrec()
*/
#include<iostream>
using namespace std;

class Node
{
	public:
		int data;
		Node *next;
	
	Node()
	{
		data =0;
		next = NULL;
	}
	
	Node(int data)
	{
		this->data = data;
		next = NULL;	
	}	
};

class SLL
{
	Node *head;
	public:
		// Constructor
		SLL()
		{
			head = NULL;	
		}	
		void create()
		{
			head = createrec();
		}
			
		// Create Recursively
		Node* createrec()
		{
			int x;
			cout<<"\n\n Enter any Number:";
			cin>>x;
			
			if(x == -1)
				return NULL;
			
			Node *temp = new Node(x);	
			temp->next = createrec();
			return temp;
		}		
		
		Node* getHead()
		{
			return head;
		}
		
		void showrec(Node *p)
		{
			if(p == NULL)
				return;
			
			cout<<p->data<<" ";
			showrec(p->next);
		}		
		
		void showrevrec(Node *p)
		{
			if(p==NULL)
				return;
			
			showrevrec(p->next);
			cout<<p->data<<" ";
		}
		
		// Count 
		int countrec(Node *p)
		{	
			if(p == NULL)
				return 0;
			
			int res = countrec(p->next);
			return res+1;
		}
		
		// Search
		int searchrec(Node *p,int s)
		{
			if(p==NULL)
				return 0;
			
			if(p->data == s)
				return 1;
			
			int res = searchrec(p->next,s);
			return res;
		}
		
		void makeempty()
		{
			head = makeemptyrec(head);
		}
		
	 	Node* makeemptyrec(Node *p)
	 	{
	 		if(p == NULL)
	 		  return NULL;
			
	 		p->next = makeemptyrec(p->next);
			delete p;
			p = NULL;
			return p;
		}
		
		void deleteatend()
		{
			head = deleteatendrec(head);
		}
		
		Node* deleteatendrec(Node *p)
		{
			if(p->next == NULL )
			{
				delete p;
				p = NULL;
				return p;
			}
			p->next = deleteatendrec(p->next);	
			return p;
		}
};

int main()
{
	SLL ll;
	
	ll.create();
	
	cout<<"\n\n SLL Data:";
	ll.showrec(ll.getHead());
	
	cout<<"\n\n SLL Data Reverse:";
	ll.showrevrec(ll.getHead());
	
	cout<<"\n\n Total Elements in LL:"<<ll.countrec(ll.getHead());
	
	int s,res;
	cout<<"\n\n Enter Search Element:";
	cin>>s;
	res = ll.searchrec(ll.getHead(),s);
	
	if(res)
		cout<<"\n Element Found";
	else
		cout<<"\n Element Not Found";
	
	cout<<"\n Deleteing at end";
	ll.deleteatend();
	
	cout<<"\n\n After Delete SLL Data:";
	ll.showrec(ll.getHead());
	
	cout<<"\n\n Making List Empty";
	ll.makeempty();
	cout<<"\n\n After Making Empty SLL Data:";
	ll.showrec(ll.getHead());
		
	return 0;
}
