/*
Q1.WAP to create a simple binary tree and implement following functions.
-create() (using 0 as a terminating value)
-create() (using STOP as a terminating condition)
-show()
	-3 recursive()
	-3 nonrecursive
-search()
-count()
*/

#include<iostream>
#include<string.h>
#include<stdlib.h>
#define MAX 100

using namespace std;

class Node
{
	public:
		int data;
		Node* left;
		Node* right;
		
		Node()
		{
			data=0;
			left=right=NULL;
		}		
		
		Node(int x)
		{
			data = x;
			left=right=NULL;			
		}		
};


class Tree
{
	Node* root;

	public:		
		// Constructor
		Tree()
		{
			root=NULL;
		}
		
		Node* getRoot()
		{
			return root;
		}
		
		Node* create_stop();			
		
		void create()
		{
			root = create_stop();	
		}
		
		// Recursive Call Def
		void preorder(Node*);
		void inorder(Node*);
		void postorder(Node*);
					
		int search(Node*,int);
		int count(Node*);		
};

// Create 0
Node* Tree::create_stop()
{
	char x[100];
	cout<<"\nEnter Data:";
	cin.getline(x,100);
	
	if(strcmp(x,"STOP") == 0)
		return NULL;
	
	Node *p;
	p = new Node(atoi(x));
	
	cout<<"\n Enter"<<x<<" of Left:";
	p->left = create_stop();
	
	cout<<"\n Enter "<<x<<" of Right:";
	p->right = create_stop();
	
	return p;
}

// Recursive Traversal
void Tree::preorder(Node* p)
{
	if(p==NULL)
		return;
	
	cout<<p->data<<" ";
	preorder(p->left);
	preorder(p->right);
}

void Tree::inorder(Node* p)
{
	if(p==NULL)
		return;
		
	inorder(p->left);
	cout<<p->data<<" ";
	inorder(p->right);
}

void Tree::postorder(Node* p)
{
	if(p==NULL)
		return;
	
	postorder(p->left);
	postorder(p->right);
	cout<<p->data<<" ";
}


// Count Function
int Tree::count(Node* t)
{
	int res1=0,res2=0;

	if( t == NULL )
		return 0;
	
	
	res1=count(t->left);
	res1++;
	res2=count(t->right);
	
	return res1+res2;
}


// Search Function
int Tree::search(Node* p,int s)
{
	if(p == NULL)
	{
		return 0;
	}
	
	if(p->data == s)
	{
		return 1;
	}
	
	int res;
	
	res = search(p->left,s);
	
	if(res == 1)
	{
		return res;
	}
	
	res = search(p->right,s);	
		
	return res;
}

		
int main()
{
	freopen("inputstr.txt","r",stdin);
	
	Tree t;
	t.create();
	
	cout<<"\n-------------------------------";
	cout<<"\n\n Recursive Traversal ";
	
	cout<<"\n\n Preorder Traversal:";
	t.preorder(t.getRoot());	
	
	cout<<"\n\n Inorder Traversal:";
	t.inorder(t.getRoot());	
	
	cout<<"\n\n Postorder Traversal:";
	t.postorder(t.getRoot());	
	
	int i=5,s;
	
	while( i != 0)
	{
		cout<<"\n\n Enter Search Key:";
		cin>>s;
		
		if(t.search(t.getRoot(),s))
			cout<<"\n Data "<<s<<" Found!";
		else
			cout<<"\n Data "<<s<<" Not Found!";
		i--;
	}
	
	cout<<"\n\n Count:"<<t.count(t.getRoot());
	
	return 0;
}

