/*
WAP to create a TBT from given BST.
*/
#include<iostream>
using namespace std;

class Node
{
	public:
		int data;
		Node* left,*right;
		
		Node()
		{
			data = 0;
			left=right = NULL;
		}
		
		
		Node(int x)
		{
			data = x;
			left=right = NULL;
		}
};

class BST
{
	Node *root;
	public:
		BST()
		{
			root = NULL;
		}	
		
		Node* getRoot()
		{
			return root;
		}
		
		void inorder(Node *t);
		
		void create();
		Node* insert_rec(Node *t,int x);
};

void BST::create()
{
	int x;
	while(1)
	{
		cout<<"\n\n Enter data: 0-Stop:";
		cin>>x;
		
		if(x == 0)
			return;	
			
		root = insert_rec(root,x);	
	}
}

Node* BST::insert_rec(Node *t,int x)
{
	if(t == NULL)
	{
		t = new Node(x);
		return t;
	}
	
	if(x < t->data)
	{
		t->left = insert_rec(t->left,x);
		return t;
	}
	else if (x > t->data)
	{
		t->right = insert_rec(t->right,x);
		return t;
	}
	else
	{
		cout<<"\n\n Duplicated Data!";
		return NULL;
	}
}

void BST::inorder(Node *t)
{
	if(t!=NULL)
	{
		inorder(t->left);
		cout<<t->data<<" ";
		inorder(t->right);
	}
}

class TBTNode
{
	public:
		TBTNode *left;
		int lbit;
		int data;
		int child;
		int rbit;
		TBTNode *right;
		
		TBTNode()
		{
			left = right = NULL;
			lbit = rbit = 0;
			child = -1;
			data = 0;	
		}	
		
		TBTNode(int x)
		{
			left = right = NULL;
			lbit = rbit = 0;
			child = -1;
			data = x;	
		}	
};

class TBT
{
	TBTNode *root;
	public:
		TBT()
		{
			// dummy node
			root = new TBTNode();
			root->left = root->right = root;
		}	
		
		void copy(BST bt);
		TBTNode* copy_rec(Node *t,int cld);
		void convertIntoTBT(TBTNode *inorderArray[10]);
		void createInorderArray(TBTNode *inorderArray[10],TBTNode* t);
	
		void inorder();
		TBTNode* findInorderSucc(TBTNode *t);
};

void TBT::inorder()
{
	TBTNode *t = root->left;
	
	while(t->lbit == 1)
	{
		t = t->left;	
	}	
	
	while( t != root)
	{
		cout<<t->data<<" ";
		t = findInorderSucc(t);
	}
}

TBTNode* TBT::findInorderSucc(TBTNode *t)
{
	if(t->rbit == 0)
	{
		return t->right;
	}
	
	t = t->right;
	
	while(t->lbit == 1)
	{
		t = t->left;
	}
	
	return t;
}
		
int ind = 0;

void TBT::copy(BST bt)
{
	cout<<"\n copy rec start";
	root->left = copy_rec(bt.getRoot(),0);
	
	cout<<"\n Copy rec comp";	
	TBTNode *inorderArray[10];
		
	createInorderArray(inorderArray,root->left);
	
	cout<<"\n\n InorderArray:";
	for(int i=0;i<ind;i++)
	{
		cout<<inorderArray[i]->data<<" ";
	}
	
	convertIntoTBT(inorderArray);		
}

void TBT::convertIntoTBT(TBTNode *inorderArray[10])
{
	TBTNode *t;
	
	// changing first node
	t = inorderArray[0];
	
	t->left = root;
	t->lbit = 0;
	t->rbit = 1;
	
	if(t->right == NULL)
	{
		t->right = inorderArray[1];
		t->rbit = 0;
	}
	
	// changing last node
	t = inorderArray[ind-1];
	
	t->right = root;
	t->rbit = 0;
	t->lbit = 1;
	
	if(t->left == NULL)
	{
		t->left = inorderArray[ind-2];
		t->lbit = 0;
	}
	
	// changing middle ones
	for(int i=1;i<=ind-2;i++)
	{
		t = inorderArray[i];
		
		t->lbit = 1;
		
		if(t->left == NULL)
		{
			t->left = inorderArray[i-1];
			t->lbit = 0;
		}
		
		t->rbit = 1;
		
		if(t->right == NULL)
		{
			t->right = inorderArray[i+1];
			t->rbit = 0;
		}
	}
}

void TBT::createInorderArray(TBTNode *inorderArray[10],TBTNode* t)
{
	if(t == NULL)
		return;
	
	createInorderArray(inorderArray,t->left);
	
	inorderArray[ind++] = t;
	
	createInorderArray(inorderArray,t->right);
}

TBTNode* TBT::copy_rec(Node *t,int cld)
{
	if(t == NULL)
		return NULL;
	
	TBTNode *p = new TBTNode(t->data);
	p->child = cld;
	
	p->left = copy_rec(t->left,0);
	p->right = copy_rec(t->right,1);
	
	return p;	
}

int main()
{
	freopen("input.txt","r",stdin);
	
	BST bt;
	TBT tb;
	
	bt.create();
	cout<<"\n\n Inorder Traversal BST:";
	bt.inorder(bt.getRoot());

	tb.copy(bt);
	
	cout<<"\n\n Inorder Traversal TBT:";
	tb.inorder();
		
	return 0;
}
