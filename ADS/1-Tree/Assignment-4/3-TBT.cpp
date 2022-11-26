/*
Q3.WAP to implement TBT with following functions.
-create() 
-preorder() 
-postorder()
-preorder() 
-inorder()
*/

#include<iostream>

using namespace std;

class TBTNode
{
	public:
		int data;
		int child,lbit,rbit;
		TBTNode *left, *right;
		
		TBTNode()
		{
			data = -1;
			child = -1;
			lbit = rbit = 0;
			left = right = NULL;	
		}	
		
		TBTNode(int x)
		{
			data = x;
			child = -1;
			lbit = rbit = 0;
			left = right = NULL;	
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
		
		void create();
		void create_rec(TBTNode*,int);
		
		void preorder();
		TBTNode* findPreSuc(TBTNode*);	
		
		void postorder();
		TBTNode* findPostSuc(TBTNode*);	
		
		void inorder();
		TBTNode* findInSuc(TBTNode*);	
};

void TBT::create()
{
	create_rec(root->left,0);
}
		
void TBT::create_rec(TBTNode* father,int cld)
{
	int x;
	cout<<"\n Enter Data 0 to stop:";
	cin>>x;
	
	if(x == 0)
	{
		return;
	}
	
	TBTNode* t = new TBTNode(x);
	
	// left child
	if(cld == 0)
	{
		t->left = father->left;
		t->child = 0;
		t->right = father;
		
		father->left = t;
		father->lbit = 1;
	}
	else
	{
		// right child
		t->right = father->right;
		t->child = 1;
		t->left = father;
		
		father->right = t;
		father->rbit = 1;
	}
	
	cout<<"\n\n Enter left of "<<x<<" :";
	create_rec(t,0);
	cout<<"\n\n Enter right of "<<x<<" :";
	create_rec(t,1);
}


// Preorder traversal
void TBT::preorder()
{
	TBTNode *t = root->left;
		
	while(t!=root)
	{
		cout<<t->data<<" ";
		t = findPreSuc(t);
	}
}

// finding preorder successor
TBTNode* TBT::findPreSuc(TBTNode* t)
{
	if( t->lbit == 1)
		return t->left;
	
	if(t->rbit == 1)
		return t->right;
	
	t =  t->right;
	while(t->rbit == 0 && t != root)
		t = t->right;
	
	return t->right;
}

// postorder
void TBT::postorder()
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
		t = findPostSuc(t);
	}
	
}

// find postorder successor
TBTNode* TBT::findPostSuc(TBTNode* t)
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
	freopen("input.txt","r",stdin);
	TBT t;
	
	t.create();
	
	cout<<"\n\n Preorder traversal:";
	t.preorder();
	
	cout<<"\n\n Postorder traversal:";
	t.postorder();
	
	cout<<"\n\n Inorder traversal:";
	t.inorder();
	
	return 0;
}
