/*
Q2.WAP to implement BST with following functions.
-nonrecursive create()
-recursive delete()
-recursive search()
-recursive count to count nodes of degree 1.
*/

#include<iostream>
#define MAX 100
using namespace std;

class Node
{
	public:
		int data;
		Node* left,*right;
		
		Node()
		{
			data = 0;
			left = right = NULL;	
		}	
		Node(int x)
		{
			data = x;
			left = right = NULL;	
		}	
};

class BST
{
	Node* root;
	
	public:
		BST()
		{
			root = NULL;
		}
		Node* getRoot()
		{
			return root;
		}
		
		void create();
		void inorder(Node*);
		
		void delete_(int);
		Node* delete_rec(Node*,int);
		
		Node* findMin(Node*);
		
		int search(Node*,int );
		
		int count1(Node*);
};

void BST::create()
{
	int x;
	cout<<"\n Enter data, 0 to Stop:";
	cin>>x;
	
	root = new Node(x);
	Node *t = root;
	Node *q;
	
	while(1)
	{
		t = root;
		cin>>x;
		if(x == 0)
		{
			break;
		}
		
		while(t != NULL)	
		{
			q = t;
				
			if( x < t->data)
			{
				t = t->left;
			}	
			else if(x > t->data)
			{
				t = t->right;
			}
			else
			{
				cout<<"\n Duplicate Data";
			}	
		}	
		
		t = new Node(x);
		if( x < q->data)
			q->left = t;
		else if(x > q->data)
			q->right = t;
	}
}

void BST::delete_(int x)
{
	root = delete_rec(root,x);	
}

Node* BST::findMin(Node* t)
{
	if(t == NULL)
	{
		return NULL;
	}
	
	while(t->left != NULL)
	{
		t = t->left;
	}
	
	return t;
}
	

Node* BST::delete_rec(Node* t,int x)
{
	if( t == NULL)
	{
		cout<<"\n Element Not found";
		return NULL;
	}
	
	if(x < t->data)
	{
		t->left =delete_rec(t->left,x);
		return t;
	}
	else if(x > t->data)
	{
		t->right = delete_rec(t->right,x);
		return t;
	}
	
	cout<<t->data;
	// Element found
	if( t->left == NULL && t->right == NULL)
	{
		delete t;
		cout<<"\n Element Deleted Successfully!";
		return NULL;
	}
	
	if( t->left == NULL)
	{
		Node *p = t->right;
		cout<<"\n Element Deleted Successfully!";
		delete t;
		return p;
	}
	
	if( t->right == NULL)
	{
		Node *p = t->left;
		cout<<"\n Element Deleted Successfully!";
		delete t;
		return p;
	}
	
	// Node having 2 child
	Node *p = findMin(t->right);
	
	cout<<t->data<<" ";
	t->data = p->data;
	cout<<p->data<<" ";
	t->right = delete_rec(t->right,p->data);
	
	return t;
}



void BST::inorder(Node *t)
{
	if(t != NULL)
	{
		inorder(t->left);
		cout<<t->data<<" ";
		inorder(t->right);
	}
}

int BST::search(Node* t,int x)
{
	if(t == NULL)
	{
		return 0;
	}	
	
	if( x < t->data )
	{
		return search(t->left,x);
	}
	else if (x > t->data)
	{
		return search(t->right,x);
	}
	return 1;
}

int BST::count1(Node* t)
{
	if(t == NULL)
		return 0;
	
	if( t->left == NULL && t->right == NULL)
	{
		return 0;	
	}	
	
	if( t->left == NULL)
		return 1+count1(t->right);
	if( t->right == NULL)
		return 1+count1(t->left);	
	
	return 0+count1(t->left)+count1(t->right);
}

int main()
{
	freopen("input.txt","r",stdin);
	BST t;
	t.create();
	
	cout<<"\n\n Inorder traversal:";
	t.inorder(t.getRoot());
	
	int x;
	cout<<"\n\n Enter element to be deleted:";
	cin>>x;
	t.delete_(x);
	
	cout<<"\n\n Inorder traversal:";
	t.inorder(t.getRoot());
	
	cout<<"\n\n Enter element to search:";
	cin>>x;
	cout<<"\n Element to search is "<<x;
	if(t.search(t.getRoot(),x))
	{
		cout<<"\n Element found!";
	}
	else
	{
		cout<<"\n Element Not found!";
	}
	
	cout<<"\n\n Count1:"<<t.count1(t.getRoot());
	
	return 0;
}

