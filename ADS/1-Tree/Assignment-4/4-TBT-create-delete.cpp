/*Q4.WAP to implement TBT with following functions.
-create() recursive
-delete() recursive */

#include <iostream>
using namespace std;

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
		lbit = rbit = 0;
		data = 0;
		child = -1;
		left = right = NULL;
	}

	TBTNode(int x)
	{
		lbit = rbit = 0;
		data = x;
		child = -1;
		left = right = NULL;
	}
};

class TBT
{
	TBTNode *root;

public:
	TBT()
	{
		// dummmy node
		root = new TBTNode();
		root->left = root->right = root;
	}

	void create();
	void create_rec(TBTNode *father, int cld);

	void inorder();
	TBTNode *inorder_suc(TBTNode *t);
	void deleteData(int);

	TBTNode *findLeaf(TBTNode *t);
	void delete_rec(int x);
	void deleteData(TBTNode *t);

	TBTNode *findFather(TBTNode *t);
};

void TBT::create()
{
	create_rec(root, 0);
}

void TBT::create_rec(TBTNode *father, int cld)
{
	int x;
	cout << "\n Enter Data: 0 to stop:";
	cin >> x;

	if (x == 0)
	{
		return;
	}

	TBTNode *t = new TBTNode(x);

	// left child
	if (cld == 0)
	{
		t->left = father->left;
		t->child = 0;
		t->right = father;

		father->left = t;
		father->lbit = 1;
	}
	else
	{
		t->right = father->right;
		t->child = 1;
		t->left = father;

		father->right = t;
		father->rbit = 1;
	}

	cout << "\n Enter left of " << x << ":";
	create_rec(t, 0);
	cout << "\n Enter right of " << x << ":";
	create_rec(t, 1);
}

void TBT::inorder()
{
	TBTNode *t = root->left;

	while (t->lbit == 1)
	{
		t = t->left;
	}

	while (t != root)
	{
		cout << t->data << " ";
		t = inorder_suc(t);
	}
}

TBTNode *TBT::inorder_suc(TBTNode *t)
{
	if (t->rbit == 0)
		return t->right;

	t = t->right;

	while (t->lbit == 1)
		t = t->left;

	return t;
}

void TBT::delete_rec(int x)
{
	TBTNode *t = root->left;

	while (t->lbit == 1)
	{
		t = t->left;
	}

	// searching for the data
	while (t != root)
	{
		if (t->data == x)
		{
			break;
		}

		t = inorder_suc(t);
	}

	if (t == root)
	{
		cout << "\n\n Data Not Found";
		return;
	}
	
	cout << "\n\n Data found:" << t->data;
	// data found
	deleteData(t);
}

void TBT::deleteData(TBTNode *t)
{
	TBTNode *father = findFather(t);

	cout << "\n\n father:" << father->data;

	// leaf node
	if (t->lbit == 0 && t->rbit == 0)
	{
		if (t->child == 0)
		{
			father->left = t->left;
			father->lbit = 0;

			delete (t);
		}
		else
		{
			father->right = t->right;
			father->rbit = 0;
			delete (t);
		}
		return; // important statement
	}

	// not a leaf node
	TBTNode *p = findLeaf(t);
	cout << "\n\n p=" << p->data;
	t->data = p->data;
	deleteData(p);
}

TBTNode *TBT::findFather(TBTNode *t)
{
	// left child
	if (t->child == 0)
	{
		if (t->rbit == 0)
		{
			return t->right;
		}
		
		t = t->right;
		
		while (t->rbit == 1)
		{
			t = t->right;
		}

		return t->right;
	}
	else
	{
		// right child
		if (t->lbit == 0)
			return t->left;
		
		t = t->left;
		
		while (t->lbit == 1)
			t = t->left;

		return t->left;
	}
}

TBTNode *TBT::findLeaf(TBTNode *t)
{
	while (t->lbit == 1 || t->rbit == 1)
	{
		if (t->lbit == 1)
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

int main()
{
	freopen("input.txt", "r", stdin);
	TBT t;
	t.create();

	cout << "\n\n Inorder Traversal:";
	t.inorder();

	int x;
	cout << "\n Enter data to be deleted:";
	cin >> x;

	cout << "\nx:" << x;
	t.delete_rec(x);

	cout << "\n\n Inorder Traversal:";
	t.inorder();

	return 0;
}
