/*
    Binary Search Tree
*/
#include<stdio.h>

typedef struct NODE
{
    int data;
    struct NODE *left;
    struct NODE *right;
}node;

node *root;

void initialize();

void insert(int d);

void inorder(node *t);
void preorder(node *t);
void postorder(node *t);

int main()
{
    int ch,data;

    initialize();

    while(1)
    {
        printf("\n\n Operations on Binary Search Tree : ");
        printf("\n 1.Insert ");
        printf("\n 2.In Order Traverse ");
        printf("\n 3.Pre Order Traverse ");
        printf("\n 4.Post Order Traverse");
        printf("\n 5. Exit");

        printf("\n\n Enter your choice: ");
        scanf("%d",&ch);

        switch(ch)
        {
            case 1: printf("\n\n Enter Data to Insert: ");
                    scanf("%d",&data);
                    insert(data);
                    break;

            case 2: inorder(root);
                     break;

            case 3: preorder(root);
                    break;

            case 4: postorder(root);
                    break;

            case 5: exit(0);

            default: printf("\n\n Wrong Choice. ");
        }
    }

    return 0;
}


void initialize()
{
    root=NULL;
}

void insert(int d)
{
    node *temp,*p;

    temp=(node*)malloc(sizeof(node));

    temp->data=d;
    temp->left=NULL;
    temp->right=NULL;

    p=root;

    if(root==NULL)
    {
        root=temp;
    }
    else
    {
        node *curr;
        curr=root;

        while(curr)
        {
            p=curr;

            if(temp->data > curr->data)
            {
                curr=curr->right;
            }
            else
            {
                curr=curr->left;
            }
        }

        if(temp->data>p->data)
        {
            p->right=temp;
        }
        else
        {
            p->left=temp;
        }
    }
}

void inorder(node *t)
{
    if(t->left)
        inorder(t->left);

    printf(" %d ",t->data);

    if(t->right)
        inorder(t->right);
}

void preorder(node *t)
{
    printf(" %d ",t->data);

    if(t->left)
        inorder(t->left);

    if(t->right)
        inorder(t->right);
}

void postorder(node *t)
{
    if(t->left)
        inorder(t->left);

    if(t->right)
        inorder(t->right);

    printf(" %d ",t->data);
}
