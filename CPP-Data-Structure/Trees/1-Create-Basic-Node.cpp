#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *left;
    Node *right;

    Node(int data)
    {
        this->data = data;
        left = right = NULL;
    }
};

int main()
{
    Node *root = new Node(10);

    Node *temp = new Node(20);
    cout << &temp << endl;
    root->left = temp;

    temp = new Node(30);
    cout << &temp << endl;
    root->right = temp;

    temp = new Node(40);
    cout << &temp << endl;
    root->left->right = temp;

    cout << root->data << ends;
    cout << root->left->data << ends;
    cout << root->right->data << ends;
    cout << root->left->right->data << ends;

    return 0;
}