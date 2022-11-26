#include<iostream>
using namespace std;

/*
78
21
14
11
97
85
74
63
42
45
57
16
20
19
52
-1
*/ 


class Node
{
	public:
		int data;
		Node* left, *right;
	
		Node()
		{
			left = right = NULL;
		}
		
		Node(int x)
		{
			data = x;
			left = right = NULL;
		}
};

class AVLTree
{
	Node *root;
	
	public:	
		AVLTree()
		{
			root = NULL;
		}

		Node* getRoot()
		{
			return root;
		}

		void create();
		Node* insert(Node* t,int x);
		
		void inorder(Node *t);
		void preorder(Node *t);
		int balanceFactor(Node *t);
		int height(Node *t);
		
		Node* rotateLeft(Node *t);
		Node* rotateRight(Node *t);
		Node* rotateLeftRight(Node *t);
		Node* rotateRightLeft(Node *t);
		
		Node* delete_(Node *t,int x);
		Node* findMin(Node *t);
		
		void delete_data();
};

void AVLTree::create()
{
	int x;
	while(1)
	{
		cout<<"\n\n Enter Data -1 to Stop:";
		cin>>x;
		
		if(x == -1)
			break;
		
		root = insert(root,x);	
	}
}
Node* AVLTree::insert(Node* t,int x)
{
	if( t == NULL)
	{
		t = new Node(x);
		return t;
	}
	
	// search data
	if(x < t->data)
	{
		t->left = insert(t->left,x);
		
		if(balanceFactor(t) == 2)
		{
			if(x < t->left->data)
			{
				t = rotateRight(t);
				cout<<"\n RotateRight";
			}	
			else
			{
				t = rotateLeftRight(t);
				cout<<"\n RotateLeftRight";
			}
		}
		
		return t;
	}
	else if(x > t->data)
	{
		t->right = insert(t->right,x);
		
		if(balanceFactor(t) == -2)
		{
			if(x > t->right->data)
			{
				t = rotateLeft(t);
				cout<<"\n RotateLeft";
			}	
			else
			{
				t = rotateRightLeft(t);
				cout<<"\n RotateRightLeft";
			}
		}		
		
		return t;
	}
	else
	{
		cout<<"\n\n Duplicate Data!";
		return t;
	}
}
		
void AVLTree::inorder(Node *t)
{
	if( t != NULL)
	{
		inorder(t->left);
		cout<<"\n Data:"<<t->data<<" BalanceFactor: "<<balanceFactor(t);
		inorder(t->right);
	}
}

int AVLTree::balanceFactor(Node *t)
{
	if(t == NULL)
	{
		return 0;
	}
	int hl = 0, hr =0;
	
	if(t->left != NULL)
	{
		hl = 1 + height(t->left);			
	}	
	
	if( t->right != NULL)
	{
		hr = 1 + height(t->right);
	}
	
	return hl - hr;
}

int AVLTree::height(Node *t)
{
	if(t == NULL)
		return 0;
	
	if( t->left == NULL && t->right == NULL)
		return 0;
	
	int hl = 0,hr = 0;
	
	if( t->left != NULL)
		hl = 1 + height(t->left);	

	if( t->right != NULL)
		hr = 1 + height(t->right);
	
	return hl > hr ? hl : hr;
}

		
Node* AVLTree::rotateLeft(Node *t)
{
	Node *p = t->right;
	
	t->right = p->left;
	
	p->left = t;
	
	return p;		
}

Node* AVLTree::rotateRight(Node *t)
{
	Node *p = t->left;
	
	t->left = p->right;
	
	p->right = t;
	
	return p;
}

Node* AVLTree::rotateLeftRight(Node *t)
{
	t->left = rotateLeft(t->left);
	
	return rotateRight(t);
}

Node* AVLTree::rotateRightLeft(Node *t)
{
	t->right = rotateRight(t->right);
	
	return rotateLeft(t);	
}
		
Node* AVLTree::delete_(Node *t,int x)
{
	if(t == NULL)
	{
		cout<<"\n\n Data Not Found!";
		return NULL;	
	}	
	
	// Search data
	
	if(x < t->data)
	{
		t->left = delete_(t->left,x);
		
		if(balanceFactor(t) == -2)
		{
			if(balanceFactor(t->right) == 0 || balanceFactor(t->right) == -1 )
			{
				t = rotateLeft(t);
				cout<<"\n RotateLeft";	
			}	
			else // bf = 1
			{
				t = rotateRightLeft(t);
				cout<<"\n RotateRightLeft";
			}
		}
		
		return t;
	}
	else if( x > t->data)
	{
		t->right = delete_(t->right,x);
		
		if(balanceFactor(t) == 2)
		{
			if(balanceFactor(t->left) == 0 || balanceFactor(t->left) == 1 )
			{
				t = rotateRight(t);	
				cout<<"\n RotateRight";
			}	
			else // bf = -1
			{
				t = rotateLeftRight(t);
				cout<<"\n RotateLeftRight";
			}
		}		
		return t;
	}
	
	// Data Found
	
	if(t->left == NULL && t->right == NULL)
	{
		delete t;
		
		return NULL;
	}
	
	// node with 1 child
	if(t->left == NULL)
	{
		Node* p = t->right;
		
		delete t;
		
		return p;
	}
	
	if(t->right == NULL)
	{
		Node *p = t->left;
		delete t;
		return p;
	}
	
	// Node with 2 child
	
	Node *p = findMin(t->right);
	t->data = p->data;
	
	t->right = delete_(t->right,p->data);
	
	return t;
}

Node* AVLTree::findMin(Node *t)
{
	while(t->left != NULL)
		t = t->left;

	return t;
}

void AVLTree::delete_data()
{
	int x;
	cout<<"\n\n Enter Data to Delete:";
	cin>>x;
	
	root = delete_(root,x);
}

void AVLTree::preorder(Node *t)
{
	if(t!=NULL)
	{
		cout<<t->data<<" ";
		
		preorder(t->left);
		preorder(t->right);
	}
}

int main()
{
	AVLTree t;
	
	t.create();
	
	cout<<"\n\n Inorder Traversal:";
	t.inorder(t.getRoot());	
	
	cout<<"\n\n Preorder Traversal:";
	t.preorder(t.getRoot());
	
	t.delete_data();
	
	t.inorder(t.getRoot());
	
	return 0;
}
