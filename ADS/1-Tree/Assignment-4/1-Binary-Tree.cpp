/*
Q1.WAP to create Binary tree.Implement following functions.
-recursive create()
-non recursive postorder()
-recursive delete()
-recursive inorder()
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


class StackNode
{
	public:
		Node *address;
		int flag;
		
		StackNode()
		{
			address = NULL;
			flag = 0;
		}
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
			if( top == -1)
				return 1;
			return 0;
		}
		
		int isFull()
		{
			if(top == MAX-1)
				return 1;
			return 0;
		}
		
		void push(StackNode st)
		{
			if( isFull())
			{
				cout<<"\n\n Stack is Full";
				return;
			}
			top++;
			data[top] = st;
		}
		
		StackNode pop()
		{
			return data[top--];
		}
};

class BinaryTree
{
	Node* root;
	
	public: 
		BinaryTree()
		{
			root = NULL;	
		}	
		
		Node* getRoot()
		{
			return root;
		}
		
		void create();
		Node* create_rec();
				
		void inorder(Node *t);
		
		void postorder_non();
		
		Node* findLeaf(Node* t);		
		
		Node* delete_rec(Node* t, int x);
		void delete_(int);
};

void BinaryTree::create()
{
	root=create_rec();
}

Node* BinaryTree::create_rec()
{
	int x;
	cout<<"\n Enter Data, 0 for Stop:";
	cin>>x;
	
	if(x == 0)
	{
		return NULL;
	}
	Node *t = new Node(x);
	
	cout<<"\n Enter left of "<<x<<":";
	t->left = create_rec();
	cout<<"\n Enter right of "<<x<<":";
	t->right = create_rec();
	return t;
}

void BinaryTree::inorder(Node *t)
{
	if(t != NULL)
	{
		inorder(t->left);
		cout<<t->data<<" ";
		inorder(t->right);
	}
}

void BinaryTree::postorder_non()
{
	Node *t = root;
	
	StackNode sn;
	Stack s;
	
	while(t != NULL)
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
		
		if( sn.flag == 1)
		{
			cout<< t->data<<" ";
			continue;
		}	
		else
		{
			sn.flag = 1;
			s.push(sn);

			t = t->right;
			
			while(t != NULL)
			{
				sn.address = t;
				sn.flag = 0;
				s.push(sn);
				t = t->left;
			}
		}			
	}
}

Node* BinaryTree::findLeaf(Node *t)
{
	if(t->left != NULL || t->right != NULL)
	{
		if(t->left != NULL)
		{
			t = t->left;
		}
		else
		{
			t = t->right;
		}
	}
	return t;
}

void BinaryTree::delete_(int x)
{
	root = delete_rec(root,x);
}

Node* BinaryTree::delete_rec(Node* t, int x)
{	
	int res = 0;
	
	if(t == NULL)
	{
		return NULL;
	}

	// 1. Search the element
	while(t->data != x)
	{
		t->left=delete_rec(t->left,x);
		t->right=delete_rec(t->right,x);
		return t;	
	}	
	
	// 2. Element found
	
	if(t->left == NULL && t->right == NULL)
	{
		delete t;
		cout<<"\n Element Deleted Successfully!";
		return NULL;
	}
	
	if(t->right == NULL)
	{
		Node *p = t->left;
		delete t;
		return p;
	}

	if(t->left == NULL)
	{
		Node *p = t->right;
		delete t;
		return p;
	}
	
	// Node having 2 child
	Node *p = findLeaf(t->right);
	t->data = p->data;
	t->right = delete_rec(t->right,p->data);
	return t;
}


int main()
{
	freopen("input.txt","r",stdin);
	
	BinaryTree t;
	
	t.create();
	cout<<"\n\n Inorder Traversal:";
	t.inorder(t.getRoot());
	
	cout<<"\n\n PostOrder Traversal:";
	t.postorder_non();
	
	cout<<"\n Enter element to be deleted:";
	int x;
	cin>>x;
	
	t.delete_(x);
	
	cout<<"\n\n Inorder Traversal:";
	t.inorder(t.getRoot());
	
	return 0;
}

