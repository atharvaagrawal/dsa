
#include <bits/stdc++.h>

using namespace std;

struct node
{
  int data;
  struct node *left, *right;
};

bool isLeaf(node *root)
{
  return !root->left && !root->right;
}

void addLeftBoundary(node *root, vector<int> &res)
{
  node *cur = root->left;
  while (cur)
  {
    if (!isLeaf(cur))
      res.push_back(cur->data);
    if (cur->left)
      cur = cur->left;
    else
      cur = cur->right;
  }
}
void addRightBoundary(node *root, vector<int> &res)
{
  node *cur = root->right;
  vector<int> tmp;
  while (cur)
  {
    if (!isLeaf(cur))
      tmp.push_back(cur->data);
    if (cur->right)
      cur = cur->right;
    else
      cur = cur->left;
  }
  for (int i = tmp.size() - 1; i >= 0; --i)
  {
    res.push_back(tmp[i]);
  }
}

void addLeaves(node *root, vector<int> &res)
{
  if (isLeaf(root))
  {
    res.push_back(root->data);
    return;
  }
  if (root->left)
    addLeaves(root->left, res);
  if (root->right)
    addLeaves(root->right, res);
}

vector<int> printBoundary(node *root)
{
  vector<int> res;
  if (!root)
    return res;

  if (!isLeaf(root))
    res.push_back(root->data);

  addLeftBoundary(root, res);

  // add leaf nodes
  addLeaves(root, res);

  addRightBoundary(root, res);
  return res;
}

struct node *newNode(int data)
{
  struct node *node = (struct node *)malloc(sizeof(struct node));
  node->data = data;
  node->left = NULL;
  node->right = NULL;

  return (node);
}

int main()
{
  struct node *root = newNode(4);
  root->left = newNode(10);

  root->left->right = newNode(5);
  root->left->left = newNode(5);

  root->left->left->right = newNode(6);
  root->left->right->left = newNode(7);

  // root->left->left->right->left = newNode(5);
  // root->left->left->right->right = newNode(6);

  // root->right->right->left = newNode(9);
  // root->right->right->left->left = newNode(10);
  // root->right->right->left->right = newNode(11);

  vector<int> boundaryTraversal;
  boundaryTraversal = printBoundary(root);

  cout << "The Boundary Traversal is : ";
  for (int i = 0; i < boundaryTraversal.size(); i++)
  {
    cout << boundaryTraversal[i] << " ";
  }
  return 0;
}

// 4 10 N 5 5 N 6 7 N 8 8 N 8 11 N 3 4 N 1 3 N 8 6 N 11 11 N 5 8.
// [4, 10, null, 5, 5, null, 6, 7, null, 8 ,8,null, 8, 11, null, 3, 4, null, 1, 3, null, 8, 6, null, 11, 11, null, 5, 8]