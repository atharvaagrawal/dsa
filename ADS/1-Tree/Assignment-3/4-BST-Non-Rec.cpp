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
*/
#include<iostream>
#include<string.h>
#define MAX 100

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


class StackNode
{
	public:
		Node* addr;
		int flag;	
};

class Stack
{
	StackNode data[MAX];
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
		
		void push(StackNode x)
		{
			if( !isFull() )
			{
				top++;
				data[top] = x;	
			}
			else
			{
				cout<<"\n\n Stack is Full";
			}
		}	
		
		StackNode pop()
		{
			return data[top--];
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
		void create();	
		 
		void insert(int);
		
		void postorder();
		
		Node* findmin();
};

void BSTree::create()
{
	int x;
	while(1)
	{
		cout<<"\n Enter number to be inserted and 0 to stop:";
		cin>> x;
		
		if(x == 0)
		{
			break;
		}
		insert(x);
	}
}

void BSTree::insert(int x)
{
	if(root == NULL)
	{
		root = new Node(x);
		return;	
	}	
	
	Node*t = root;
	Node *p;
	
	while(t != NULL)
	{
		p = t;	
		if(x < t->data)
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
			return;
		}
	}
	
	t = new Node(x);
	if(x > p->data)
	{
		p->right =t;
	}
	else
	{
		p->left = t;
	}
}

Node* BSTree::findmin()
{
	if(root == NULL)
		return NULL;
	
	Node *t = root;
	
	while(t->left != NULL)
	{
		t = t->left;
	}
	
	return t;
}


void BSTree::postorder()
{
	if(root == NULL)
	{
		cout<<"\n\n Tree is Empty";
		return;
	}
	
	Node *t = root;
	Stack s;
	StackNode st;
	
	while(t != NULL)
	{
		st.addr = t;
		st.flag = 0;
		s.push(st);
		
		t = t->left;
	}
	
	while(!s.isEmpty())
	{
		st = s.pop();
		t = st.addr;
		
		if( st.flag == 1 )
		{
			cout<<t->data<<" ";
			continue;
		}
		st.flag = 1;
		s.push(st);
		
		t = t->right;
		
		while(t != NULL)
		{
			st.addr = t;
			st.flag = 0;
			s.push(st);
			
			t = t->left;
		}		
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	BSTree t;
	
	t.create();
	
	cout<<"\n\n Displaying Data:";
	t.postorder();
	
	Node *p = t.findmin();
	cout<<"\n Minimum Value:"<<p->data;
	
	return 0;
}



