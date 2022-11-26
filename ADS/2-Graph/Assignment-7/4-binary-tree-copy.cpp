/*
Q4.Create a binary tree.Make exact copy of the binary tree.

10 5 3 0 0 7 0 0 15 13 0 0 17 0 0
*/
#include<iostream>

using namespace std;

class Node
{
	public:
		int data;
		Node* left;
		Node* right;

		Node()
		{
			data = -1;
			left = right = NULL;
		}
		
		Node(int x)
		{
			data = x;
			left = right = NULL;
		}
};

class Tree
{
	Node *root;
	
	public:
		Tree()
		{
			root = 	NULL;
		}	
			
		Node* getRoot()
		{
			return root;	
		}		
		
		void create();
		Node* create_rec();
		void inorder(Node *t);
		void copy(Tree);
		Node* copy_rec(Node* t);
};

void Tree::create()
{
	root = create_rec();
}

Node* Tree::create_rec()
{
	int x;
	cout<<"\n Enter Data 0 to Stop:";
	cin>>x;
	
	if(x == 0)
		return NULL;
	
	Node* p = new Node(x);
	
	cout<<"\n Enter left of "<<x<<":";
	p->left = create_rec();
	
	cout<<"\n Enter right of "<<x<<":";
	p->right = create_rec();
	
	return p;
}

void Tree::inorder(Node *t)
{
	if(t == NULL)
		return;
	
	inorder(t->left);
	cout<<t->data<<" ";
	inorder(t->right);
}

void Tree::copy(Tree t)
{
	root = copy_rec(t.root);
}

Node* Tree::copy_rec(Node* t)
{
	if(t == NULL)
	{
		return NULL;
	}

	Node* p;
	p = new Node(t->data);
	p->left = copy_rec(t->left);
	p->right = copy_rec(t->right);

	return p;
}

int main()
{
	Tree t1,t2;
	
	t1.create();
	
	cout<<"\n\n Displaying T1:";
	t1.inorder(t1.getRoot());	
	
	t2.copy(t1);
	
	cout<<"\n\n Displaying Copied T2:";
	t2.inorder(t2.getRoot());
	
	return 0;
}

