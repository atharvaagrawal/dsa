/* 
Q7.Create a binary tree.Copy this binary tree in Threaded Binary Tree.
Print TBT using nonrecursive postorder and recursive inorder. */

#include<iostream>
using namespace std;

int ind = 0;

class Node
{
	public:
		int data;
		Node *left;
		Node *right;
		
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

class BTree
{
	Node *root;
	
	public:
		BTree()
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
};

void BTree::inorder(Node *t)
{
	if(t == NULL)
		return;
	
	inorder(t->left);
	cout<<t->data<<" ";
	inorder(t->right);
}

void BTree::create()
{
	root = create_rec();
}

Node* BTree::create_rec()
{
	cout<<"\n\n Enter data: 0-stop:";
	int x;
	cin>>x;
	
	if(x == 0)
		return NULL;
		
	Node *p = new Node(x);
	
	cout<<"\n\n Enter left of "<<x<<" :";	
	p->left = create_rec();
	cout<<"\n\n Enter right of "<<x<<" :";
	p->right = create_rec();
	
	return p;
}

// TBT
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
			
			data = -1;
			child = -1;
		}
		
		TBTNode(int x)
		{
			left = right = NULL;
			lbit = rbit = 0;
			
			data = x;
			child = -1;
		}
};

class TBT
{
	TBTNode *root;
	public:
		TBT()
		{
			root = new TBTNode();
			root->left = root->right = root;
		}
		
		void copy(BTree b);
		TBTNode* preorderCopy(Node *p,int cld);
		void createInorderArray(TBTNode* t, TBTNode* inorderArray[10]);
		void convertIntoTBT(TBTNode* inorderArray[10]);
	
		void postOrder();
		TBTNode* postOrderSuc(TBTNode *t);
		
		void inorder();
		TBTNode* findInSuc(TBTNode*);	
};

void TBT::copy(BTree b)
{
	// copying using preorder
	root->left = preorderCopy(b.getRoot(),0);
	
	TBTNode* inorderArray[10];
	
	createInorderArray(root->left,inorderArray);
	
	TBTNode* t;
	cout<<"\n\n Inorder Array:";
	for(int i=0;i<ind;i++)
	{
		t = inorderArray[i];
		cout<<t->data<<" ";
	}
	cout<<"\n\n";
	
	convertIntoTBT(inorderArray);
}

TBTNode* TBT::preorderCopy(Node *p,int cld)
{
	if( p == NULL)
		return NULL;
	
	TBTNode *t = new TBTNode(p->data);
	t->child = cld;
	t->left = preorderCopy(p->left,0);
	t->right = preorderCopy(p->right,1);
	return t;
}

void TBT::createInorderArray(TBTNode* t, TBTNode* inorderArray[10])
{
	if(t == NULL)
		return;
	
	createInorderArray(t->left,inorderArray);
	inorderArray[ind] = t;
	ind++;
	createInorderArray(t->right,inorderArray);
}

void TBT::convertIntoTBT(TBTNode* inorderArray[10])
{
	// changing first
	TBTNode *t;
	
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

void TBT::postOrder()
{
	TBTNode *t = root ->left;
	
	while( t->lbit == 1 || t->rbit == 1)
	{
		if(t->lbit == 1)
		{
			t = t->left;
		}
		else
		{
			t = t->right;
		}
	}	
	
	while( t!= root)
	{
		cout<<t->data <<" ";
		t = postOrderSuc(t);
	}	
}

TBTNode* TBT::postOrderSuc(TBTNode *t)
{
	// right child
	if( t->child == 1)
	{
		while(t->lbit == 1)
			t = t->left;
		
		return t->left;
	}
	else
	{
		// left child
		while(t->rbit == 1)
			t = t->right;
		
		t = t->right; // on parent
		
		if( t->rbit == 0)
			return t;
		
		t = t->right;
		
		while( t->lbit == 1 || t->rbit == 1)
		{
			if(t->lbit == 1)
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
}

// Inorder traversal	
void TBT::inorder()
{
	TBTNode *t = root ->left;
	
	while( t->lbit == 1 )
	{
		t = t->left;
	}	
	
	while( t!= root)
	{
		cout<<t->data <<" ";
		t = findInSuc(t);
	}

}

// Inorder successor
TBTNode* TBT::findInSuc(TBTNode* t)
{
	if(t->rbit == 1)
	{
		t = t->right;
		while( t->lbit == 1 )
		{
			t = t->left;
		}
		
		return t;
	}
	
	if(t->rbit == 0)
		return t->right;	
}

int main()
{
	freopen("inputTree.txt","r",stdin);
	BTree bt;
	TBT t;
	
	bt.create();
	
	cout<<"\n\n Binary Tree Inorder:";
	bt.inorder(bt.getRoot());
	
	t.copy(bt);
	
	cout<<"\n\n TBT After Copy:";
	t.inorder();
	
	cout<<"\n\n PostOrder:";
	t.postOrder();
	
		
	return 0;
}
