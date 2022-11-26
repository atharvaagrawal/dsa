/*
Simple Binary Tree

-create()
-recursive inorder()
-nonrecursive preorder
-search data
-find leaf node of any Node
-find height of any Node
-Print height of all the nodes in a tree
-delete a node from tree.
*/

#include<iostream>
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
			left = right = NULL;	
		}		
};


class Stack
{	
	Node* data[MAX];
	int top;
	
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
			if(top == MAX -1)
				return 1;
			return 0;
		}
	
		void push(Node* t)
		{
			if(!isFull())
			{
				top++;
				data[top] = t;
			}
			else
			{
				cout<<"\n Stack is Full";
			}
		}
		
		Node* pop()
		{
			return data[top--];
		}
};

class Tree
{
	Node* root;
	public:
		Tree()
		{
			root = NULL;
		}	
		Node* getRoot()
		{
			return root;
		}
		void create();
		
		Node* create_rec();
		
		void inorder(Node*);
		
		int search(Node*,int x);
		
		Node* leafNode(Node*);
		
		int height(Node*);
		
		void delete_(int);
		
		Node* deleteNode(Node*,int,int&);
		
		void preorder();
		
		void heightAll(Node*);		
};


void Tree::create()
{
	root = create_rec();
}

Node* Tree::create_rec()
{
	int x;
	cout<<"\n Enter data, enter 0 to stop:";
	cin>>x;
	
	if(x == 0)
	{
		return NULL; 
	}
	
	Node *p = new Node(x);
	
	cout<<"\n Enter left of "<<x<<":";
	p->left = create_rec();

	cout<<"\n Enter right of "<<x<<":";
	p->right = create_rec();
	
	return p;	
}
		
void  Tree::inorder(Node* t)
{
	if(t!=NULL)
	{
		inorder(t->left);
		cout<<t->data<<" ";
		inorder(t->right);
	}
}
		
int Tree::search(Node *t,int x)
{
	if(t == NULL)
		return 0;
	
	if(t->data == x)
	{
		return 1;
	}
	int res;
	
	res =search(t->left,x);
	
	if(res == 0)
		res = search(t->right,x);
	
	return res;
}
		
Node* Tree::leafNode(Node *t)
{
	if(t==NULL)
	{
		return NULL;
	}
	
	if(t->left == NULL && t->right == NULL)
	{
		return t;
	}
	
	if( t->left != NULL)
	{
		return leafNode(t->left);	
	}
	else
	{		
		return leafNode(t->right);	
	}
}
		
int Tree::height(Node* t)
{
	int res1 = 0,res2 = 0;
	
	if(t == NULL)
	{
		return 0;
	}
	
	if(t->left == NULL && t->right == NULL)
	{
		return 0;
	}
	
	if(t->left != NULL)
	{
	    res1 =  1+height(t->left);
	}
	
	if(t->right != NULL)
	{
		res2 = 1+height(t->right);
	}
	
	return res1 > res2 ? res1 : res2;
}
		
void Tree::delete_(int x)
{
	int res=0;
	
	root = deleteNode(root,x,res);
	
	if(res == 0)
	{
		cout<<"\n Data Not Found!";
	}
}
		
Node* Tree::deleteNode(Node* t,int x,int &res)
{
	if(t == NULL)
	{
		return NULL;
	}
	
	while(t->data != x)
	{
		t->left = deleteNode(t->left,x,res);
		if(res == 0)
			t->right = deleteNode(t->right,x,res);	
		return t;
	}
	
	// Data Found
	if(t->left == NULL && t->right == NULL)
	{
		delete t;
		res = 1;
		cout<<"\n Data Delete Successfully";
		return NULL;
	}
	
	if(t->left == NULL)
	{
		Node *p = t->right;
		res = 1;
		delete t;
		return p;
	}
	
	if(t->right == NULL)
	{
		Node *p = t->left;
		res = 1;
		delete t;
		return p;
	}
	
	Node *p = leafNode(t);
	
	t->data = p->data;
	t->left = deleteNode(t->left,p->data,res);
	
	return t;
}


void Tree::heightAll(Node *t)
{
	if(t != NULL)
	{
		heightAll(t->left);
		
		cout<<"\n Element: "<<t->data;
		cout<<" Height: "<<height(t)<<endl;
		
		heightAll(t->right);
	}
}

void Tree::preorder()
{
	if(root == NULL)
		return;
	
	Node* t = root;
	Stack s;
	
	while(t != NULL)
	{
		cout<<t->data<<" ";
		s.push(t);
		t = t->left;
	}
	
	while( ! s.isEmpty() )
	{
		t = s.pop();
		t = t->right;
		
		while(t != NULL)
		{
			cout<<t->data<<" ";
			s.push(t);
			t = t->left;
		}
	}
}
	
int main()
{
	freopen("input.txt","r",stdin);
	
	Tree t;
	
	int x;
	
	t.create();
	
	Node* p = t.getRoot();
	
	cout<<"\n\n Inorder Display:";
	t.inorder(p);
	
	cout<<"\n\n Preorder Display:";
	t.preorder();
	
	cout<<"\n\n Height of tree:"<<t.height(p);
	
	cout<<"\n\n Height of All Node:";
	t.heightAll(p);
	
	cout<<"\n\n Enter element to search:";
	cin>>x;
	
	if(t.search(p,x))
	{
		cout<<"\n Element found!";
	}
	else
	{
		cout<<"\n Element not Found!";
	}
	
	cout<<"\n\n Enter element to be deleted:";
	cin>>x;
	t.delete_(x);
	
	cout<<"\n\n After Delete Inorder Display:";
	t.inorder(p);
	
	return 0;
}
