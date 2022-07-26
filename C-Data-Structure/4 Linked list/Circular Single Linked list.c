/*
    Circular Single Linked list
*/
#include<stdio.h>

typedef struct NODE
{
  int data;
  struct NODE *next;
}node;

node *first;

void initialize();

void insertatbegin();
void insertatlast();
void insertatSpecified();

void deleteatbegin();
void deleteatlast();
void deleteatSpecified();

void display();


int main()
{
    int ch;
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
            case 1: insertatbegin();
                    break;

            case 2: insertatlast();
                    break;

            case 3: insertatSpecified();
                    break;

            case 4: deleteatbegin();
                    break;

            case 5: deleteatlast();
                    break;

            case 6: deleteatSpecified();
                    break;

            case 7:
                    break;

            case 8: display();
                    break;

            case 9: exit(0);

            default: printf("\n\n Wrong Choice ");
        }
    }
    return 0;
}

void initialize()
{
    first=NULL;
}

void insertatbegin()
{
    node *temp;
    temp=(node*)malloc(sizeof(node));

    printf("\n\n Enter to be inserted: ");
    scanf("%d",&temp->data);

    temp->next=NULL;

    if(first==NULL)
    {
        first=temp;
        temp->next=first;
    }
    else
    {
        node *p;

        p=first;

        while(p->next!=first)
            p=p->next;

        p->next=temp;

        temp->next=first;
        first=temp;
    }
}

void insertatlast()
{
    node *temp;
    temp=(node*)malloc(sizeof(node));

    printf("\n\n Enter to be inserted: ");
    scanf("%d",&temp->data);

    temp->next=first;

    if(first==NULL)
    {
        first=temp;
    }
    else
    {
        node *p;

        p=first;

        while(p->next!=first)
            p=p->next;

        p->next=temp;
        temp->next=first;

    }
}

void insertatSpecified()
{
    node *temp;
    temp=(node*)malloc(sizeof(node));

    printf("\n\n Enter to be inserted: ");
    scanf("%d",&temp->data);

    temp->next=first;

    if(first==NULL)
    {
        first=temp;
    }
    else
    {
        int pos;
        node *p,*q;

        p=first;

        printf("\n\n Enter Position to insert: ");
        scanf("%d",&pos);

        while(p->data!=pos && p->next!=first)
            p=p->next;

        if(p->data == pos)
        {
            temp->next=p->next;
            p->next=temp;
        }
        else
        {
            printf("\n\n Invalid Position ");
            return;
        }
    }
}

void deleteatbegin()
{
    node *p,*q;

    if(first==NULL)
    {
        printf("\n\n List is Empty ");
    }
    else
    {
        q=p=first;

        while(p->next!=first)
        {
            p=p->next;
        }
        first=first->next;

        p->next=first;

        q->next=NULL;
        free(q);
    }
}

void deleteatlast()
{
    node *p,*q;

    if(first==NULL)
    {
        printf("\n\n List is Empty ");
    }
    else
    {
        q=p=first;

        while(p->next!=first)
        {
            p=p->next;
        }

        while(q->next!=p)
        {
            q=q->next;
        }

        if(first==p)
            first=NULL;

        q->next=first;
        p->next=NULL;
        free(p);
    }
}

void deleteatSpecified()
{
    int pos;
    node *p,*q;

    if(first==NULL)
    {
        printf("\n\n List is Empty ");
    }
    else
    {
        q=p=first;

        printf("\n\n Enter the position : ");
        scanf("%d",&pos);

        while(p->data!=pos && p->next!=first)
        {
            p=p->next;
        }

        while(q->next!=p)
        {
            q=q->next;
        }

        if(first==p)
            first=NULL;

        q->next=p->next;
        p->next=NULL;
        free(p);
    }
}

void display()
{
    node *p;

    p=first;

    if(first==NULL)
        printf("\n\n List is Empty: ");
    else
    {
      printf("\n\n List element's are:  ");

      printf(" %d ",p->data);
      p=p->next;
      while(p!=first)
      {
        printf(" %d ",p->data);
        p=p->next;
      }

     }

}

