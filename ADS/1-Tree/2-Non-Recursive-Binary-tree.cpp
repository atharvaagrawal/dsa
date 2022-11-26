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
#include<string>

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

class Stack
{
	Node* data[MAX];
	int top;
	
	public:
		Stack()
		{
			top = -1;	
		}	
		
		int isFull()
		{
			if(top==MAX-1)
				return 1;
			return 0;
		}
		
		int isEmpty()
		{
			if(top==-1)
				return 1;
			return 0;
		}
		
		void push(Node*);
		Node* pop();
};

void Stack::push(Node *p)
{
	if(isFull())
	{
		cout<<"\n Stack is FULL!!";		
		return;
	}

	top++;
	data[top] = p;	
}

Node* Stack::pop()
{
	if(isEmpty())
	{
		cout<<"\n Stack is Empty!!";
		return NULL;
	}
	
	return data[top--];
}


/// Stack for PostOrder
class StackNode
{
	public:
		Node* address;
		int flag;	
};

class StackP
{
	StackNode data[MAX];
	int top;
	
	public:
		StackP()
		{
			top = -1;	
		}	
		
		int isFull()
		{
			if(top==MAX-1)
				return 1;
			return 0;
		}
		
		int isEmpty()
		{
			if(top==-1)
				return 1;
			return 0;
		}
		
		void push(StackNode);
		StackNode pop();
};

void StackP::push(StackNode sn)
{
	if(isFull())
	{
		cout<<"\n Stack is FULL!!";
		return;
	}
	
	top++;
	data[top] = sn;
}

StackNode StackP::pop()
{
	if(isEmpty())
	{
		cout<<"\n Stack is Empty!!";
		
		// Check
		StackNode s;
		return s;
	}
	
	return data[top--];
}

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
		
		Node* create_rec();

		void create()
		{
			root = create_rec();	
		}
							
		// Non-Recursive Call Def
		void non_rec_preorder();
		void non_rec_inorder();
		void non_rec_postorder();	
};

// Create 0
Node* Tree::create_rec()
{
	int x;
	cout<<"\nEnter Data:";
	cin>>x;
	
	if(x == 0)
		return NULL;
	
	Node *p;
	p = new Node(x);
	
	cout<<"\n Enter"<<x<<" of Left:";
	p->left = create_rec();
	
	cout<<"\n Enter "<<x<<" of Right:";
	p->right = create_rec();
	
	return p;
}


// Non-Recursive Tree Traversal
void Tree::non_rec_preorder()
{
	Stack s;
	Node* t;
	
	t = root;
	
	while(t != NULL || !s.isEmpty())
	{
		while(t != NULL)
		{
			cout<<t->data<<" ";
			s.push(t);
			t = t->left;
		}
		
		t = s.pop();
		t = t->right;
	}
}

void Tree::non_rec_inorder()
{
	Stack s;
	Node* t;
	t = root;
	
	while(t != NULL || !s.isEmpty() )
	{
		while(t!=NULL)
		{
			s.push(t);
			t = t->left;	
		}	
		
		t = s.pop();
		cout<<t->data<<" ";
		t = t->right;
	}		
}

void Tree::non_rec_postorder()
{
	StackNode sn;
	StackP s;
	Node* t;
	t = root;
	
	while(t!=NULL)
	{
		sn.address = t;
		sn.flag = 0;
		s.push(sn);
		t = t->left;
	}
	
	while(!s.isEmpty())
	{
		sn = s.pop();
		t = sn.address;
		
		if(sn.flag == 1)
		{
			cout<<t->data<<" ";
		}
		else // flag = 0 left subtree visited
		{
			sn.flag = 1;
			s.push(sn);
			t = t->right;
			
			while(t!=NULL)
			{
				sn.address=t;
				sn.flag = 0;
				s.push(sn);
				t = t->left;	
			}		
		}
	}
}

	
int main()
{
	freopen("input.txt","r",stdin);
	
	Tree t;
	t.create();	
	
	cout<<"\n-------------------------------";
	cout<<"\n\n Non-Recursive Traversal ";
	
	cout<<"\n\n Preorder Traversal:";
	t.non_rec_preorder();	
	
	cout<<"\n\n Inorder Traversal:";
	t.non_rec_inorder();	
	
	cout<<"\n\n Postorder Traversal:";
	t.non_rec_postorder();	
	
	return 0;
}

