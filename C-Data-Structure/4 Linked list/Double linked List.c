/*
    Double linked List
*/
#include<stdio.h>
#include<stdlib.h>
typedef struct NODE
{
    int data;
    struct NODE *next;
    struct NODE *prev;
}node;

node *first;

void initialize();

void insertatbegin(int a);
void insertatlast(int a);
void insertatspecified(int a);

void deleteatbegin();
void deleteatlast();
void deleteatspecified();

void display();

int main()
{
    int data,ch;
    initialize();

    while(1)
    {
        printf("\n\n Menu: ");
        printf("\n 1. Insert at Begin ");
        printf("\n 2. Insert at last ");
        printf("\n 3. Insert at Specified Position ");
        printf("\n 4. Deletion from Begin");
        printf("\n 5. Deletion from End ");
        printf("\n 6. Deletion from Specified Position ");
        printf("\n 7. Searching a Node  ");
        printf("\n 8. Display ");
        printf("\n 9. Exit");

        printf("\n\n Enter your choice ");
        scanf("%d",&ch);

        switch(ch)
        {
            case 1: printf("\n\n Enter data to insert: ");
                    scanf("%d",&data);
                    insertatbegin(data);
                    break;
            case 2: printf("\n\n Enter data to insert: ");
                    scanf("%d",&data);

                    insertatlast(data);
                    break;
            case 3: printf("\n\n Enter data to insert: ");
                    scanf("%d",&data);

                    insertatspecified(data);
                    break;

            case 4: deleteatbegin();

                    break;

            case 5:
                    deleteatlast();
                    break;

            case 6:
                    deleteatspecified();
                    break;

            case 7:
                    break;

            case 8: display();
                    break;

            case 9: return 0;

            default: printf("\n\n Wrong Choice ");
        }
    }
}

void initialize()
{
   first=NULL;
}

void insertatbegin(int a)
{
	node *newnode;
	newnode=(node*)malloc(sizeof(node));
    newnode->data=a;
    newnode->next=NULL;
    newnode->prev=NULL;

    if(first==NULL)
        first=newnode;
    else
    {
       newnode->next=first;
       first->prev=newnode;
       first=newnode;
    }
}

void insertatlast(int a)
{
	node *newnode;
	newnode=(node*)malloc(sizeof(node));
    newnode->data=a;
    newnode->next=NULL;
    newnode->prev=NULL;

    if(first==NULL)
        first=newnode;
    else
    {
       node *temp;
       temp=first;

       while(temp->next!=NULL)
       {
           temp=temp->next;
       }
       newnode->prev=temp;
       temp->next=newnode;
    }
}
void insertatspecified(int a)
{
	node *newnode;
	newnode=(node*)malloc(sizeof(node));
    newnode->data=a;
    newnode->next=NULL;
    newnode->prev=NULL;

    int pos;

    if(first==NULL)
        first=newnode;
    else
    {
        node *temp=first;

        printf("\n\n Enter Position to insert ");
        scanf("%d",&pos);

        while(temp->data!=pos)
        {
            temp=temp->next;
             if(temp==NULL)
                break;
        }
        if(temp==NULL)
        {
          printf("\n\n No Such Node Found");
        }
        else
        {
            newnode->next=temp->next;
            temp->next->prev=newnode;
            temp->next=newnode;
            newnode->prev=temp;
        }
    }
}

void display()
{
    node *temp;
    temp=first;

    if(first==NULL)
        printf("\n\n List is Empty");
    else
    {
        printf("\n\n Element in List: ");
        while(temp!=NULL)
        {
            printf(" %d ",temp->data);
            temp=temp->next;
        }
    }
}

void deleteatbegin()
{
    if(first==NULL)
        printf("\n\n List is Empty ");
    else
    {
        node *temp;
        temp=first;
        first=first->next;
        first->prev=NULL;
        temp->next=NULL;

        printf("\n\n Node %d Delete Sucessfully ",temp->data);
        free(temp);
    }
}
void deleteatlast()
{
    if(first==NULL)
        printf("\n\n List is Empty ");
    else
    {
        node *temp;
        temp=first;

        while(temp->next!=NULL)
        {
            temp=temp->next;
        }
        temp->prev->next=NULL;
        temp->prev=NULL;
        free(temp);
    }

}
void deleteatspecified()
{
    int pos;
    if(first==NULL)
        printf("\n\n List is Empty ");
    else
    {
        node *temp;
        temp=(node*)malloc(sizeof(node));
        temp=first;

        printf("\n\n Enter position to be deleted: ");
        scanf("%d",&pos);

        while(temp->data!=pos)
        {
            temp=temp->next;
        }

        temp->prev->next=temp->next;
        temp->next->prev=temp->prev;
        temp->prev=NULL;
        temp->next=NULL;
        free(temp);
    }

}
