/*
1.
Create BST of integers and implement following functions.
	-create() until user enters "STOP"
	-inser()
	-insertrec()
-Inorder recursive Traversals
-Postorder non-recursive traversal
-count leaf nodes	
-count nodes with degree 1
-count nodes with degree 2
-delete a node
-recursive findmin()
-nonrecursive findmin()
-recursive findmax()
-recursive findleaf()
*/
#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;

class Node
{
	public:
		int data;
		Node* left,*right;
		
		Node()
		{
			data=0;
			left=right=NULL;	
		}	
		Node(int x)
		{
			data=x;
			left=right=NULL;	
		}	
};


class BSTree
{
	Node *root;
	
	public:
		BSTree()
		{
			root = NULL;
		}
		
		Node* getRoot()
		{
			return root;
		}
		
		void create();	
		Node* insert_rec(Node*,char*);
		
		void inOrder_rec(Node*);
		
		int count0(Node*);
		int count1(Node*);
		int count2(Node*);
		
		void delete_(int);
		Node* delete_rec(Node*,int);
		Node* findmin(Node*);
		Node* findmax(Node*);
		Node* findleaf(Node*);			
};


void BSTree::create()
{
	char x[100];
	
	while(1)
	{
		cout<<"\n Enter Number to insert, enter STOP to stop:";
		cin>>x;
		
	  if(strcmp(x,"STOP") == 0)
	  {
	  	break;
	  }	
	  
		root = insert_rec(root,x);	
	}
}

Node* BSTree::insert_rec(Node* t,char* x)
{
	if( t == NULL)
	{
		t = new Node(atoi(x));
		return t;
	}
  	
  	if(atoi(x) > t->data)
  	{
  		t->right = insert_rec(t->right,x);	
		return t;
	}
	else if(atoi(x) < t->data)
	{
		t->left = insert_rec(t->left,x);
		return t;
	}
	else
	{
		cout<<"\n Value Already Present!";
		return NULL;
	}
}

	
void BSTree::inOrder_rec(Node* t)
{
	if(t != NULL)
	{
		inOrder_rec(t->left);
		cout<<t->data<<" ";
		inOrder_rec(t->right);
	}
}

int BSTree::count0(Node* t)
{
	if(t == NULL)
	{
		return 0;
	}
	
	if(t->left == NULL && t->right == NULL)
	{
		return 1;
	}
	
	if(t->left == NULL)
	{
		return 0+count0(t->right);
	}
	
	if(t->right == NULL)
	{
		return 0+count0(t->left);
	}
	
	return 0+count0(t->left)+count0(t->right);
}

int BSTree::count1(Node* t)
{
	if(t == NULL)
	{
		return 0;
	}
	
	if(t->left == NULL && t->right == NULL)
	{
		return 0;
	}
	
	if(t->left == NULL)
	{
		return 1+count1(t->right);
	}
	
	if(t->right == NULL)
	{
		return 1+count1(t->left);
	}
	
	return 0+count1(t->left)+count1(t->right);
	
}
int BSTree::count2(Node* t)
{
	if(t == NULL)
	{
		return 0;
	}
	
	if(t->left == NULL && t->right == NULL)
	{
		return 0;
	}
	
	if(t->left == NULL)
	{
		return 0+count2(t->right);
	}
	
	if(t->right == NULL)
	{
		return 0+count2(t->left);
	}
	
	return 1+count2(t->left)+count2(t->right);
	
}
		
void BSTree::delete_(int x)
{
	root = delete_rec(root,x);	
}

Node* BSTree::delete_rec(Node* t,int x)
{
	if(t == NULL)
	{
		cout<<"\n Data Not Found!";
		return NULL;
	}
	
	if(x > t->data)
	{
		t->right = delete_rec(t->right,x);
		return t;	
	}
	else if(x < t->data)
	{
		t->left = delete_rec(t->left, x);
		return t;
	}
	
	// Data Found
	
	// leaf node
	if(t->left == NULL && t->right == NULL)
	{
		delete t;
		cout<<"\n Data Deleted Successfully!";
		return NULL;
	}
	
	// Node with 1 child
	if(t->left == NULL)
	{
		Node *p = t->right;
		delete t;
		cout<<"\n Data Deleted Successfully!";
		return p;
	}
	
	if(t->right == NULL)
	{
		Node *p = t->left;
		delete t;
		cout<<"\n Data Deleted Successfully!";
		return p;
	}
	
	// Node with 2 child	
	Node*p = findleaf(t->right);
	
	t->data = p->data;
	
	t->right = delete_rec(t->right,p->data);
	
	return t;
}

Node* BSTree::findmin(Node* t)
{
	if(t == NULL)
	{
		return NULL;
	}
	
	if(t->left == NULL)
	{
		return t;
	}
	
	return findmin(t->left);
}

Node* BSTree::findmax(Node* t)
{
	if(t == NULL)
	{
		return NULL;
	}
	
	if(t->right == NULL)
	{
		return t;
	}
	
	return findmax(t->right);
}


Node* BSTree::findleaf(Node* t)
{
	if(t == NULL)
	{
		return NULL;	
	}	
	
	if(t->left == NULL && t->right == NULL)
	{
		return t;
	}
	
	if(t->left != NULL)
	{
		Node *p = findleaf(t->left);
		return p;
	}
	else
	{
		Node *p = findleaf(t->right);
		return p;
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	BSTree t;
	t.create();
	int x;
	
	Node *root = t.getRoot();
	Node *p;
	
	cout<<"\n\n Displaying Data:";
	t.inOrder_rec(root);
	
	cout<<"\n Leaf Node count:"<<t.count0(root);
	cout<<"\n Node with 1 Child count:"<<t.count1(root);
	cout<<"\n Node with 2 Child count:"<<t.count2(root);
	
	p = t.findmin(root);
	cout<<"\n Minimum:"<<p->data;

	p = t.findmax(root);
	cout<<"\n Maximum:"<<p->data;

	
	cout<<"\n\n Enter Element to de deleted:";
	cin>>x;
	t.delete_(x);

	cout<<"\n\n Displaying Data after delete:";
	t.inOrder_rec(root);
	
	return 0;
}



