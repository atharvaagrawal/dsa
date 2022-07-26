#include <stdio.h>
#include <stdlib.h>
#include<malloc.h>
#include<process.h>

typedef struct NODE
{
    int data;
    struct NODE *next ;
}node;

node *q ,*r ,*first,*newnode ;

// linked list operation function
void insertnode();
void deletenode();
void display();

int main()
{
    int ch=0,ans=0;

    // initializing linked list is empty

    first=NULL;

    do
    {
        printf("\n\n Operation List");
        printf("\n 1. Insert a element ");
        printf("\n 2. Delete a element ");
        printf("\n 3. Display the elements ");
        printf("\n 4. Exit ");

        printf("\n\n Enter your choice: ");
        scanf("%d",&ch);

        switch(ch)
        {
            case 1: insertnode();
                    break;

            case 2: deletenode();
                    break;

            case 3: display();
                    break;

            case 4: exit(0);

            default: printf("\n\n Wrong Choice ");
        }

        printf("\n\n do you want to continue press 1 else press 0 to exit : ");
        scanf(" %d",&ans);
    }while(ans==1); // do while loop
    getch();

} // main

// Insertion is performed at the last position of the list

void insertnode()
{
    int data ;
    printf("\n\n Enter the data to be insert: ");
    scanf("%d",&data);

    //runtime memory allocation
    newnode=(node*)malloc(sizeof(node));

    //initialize

   newnode->data=data;
   newnode->next=NULL;

   if(first==NULL)
   {
       first=newnode;
   }
   else
   {
       q=first;

       while(q->next!=NULL)
       {
           q=q->next;
       }
        q->next=newnode;
   }

    printf("\n\n Node is inserted ");
}


void deletenode()
{
    int search=0 , flag =0 ;
    if(first==NULL) // empty
    {
        printf("\n\n The list is empty \n");

    }
    else //not empty
    {
        printf("\n\n Enter the node data to u want to delete  ");
        scanf(" %d",&search);

        q=first;
        while(q!=NULL)
        {
            if(q->data==search)
            {
                flag=1;
                break;
            }
            else
            {
                q=q->next; // increment q
            }
        }

        if(flag==0)
        {
            printf("\n\n The node having %d data is not found",search);
        }
        else if(q==first)
        {
            first=q->next; //error
            printf("\n\n The data %d is delete",q->data);
            free(q); // deleting node
        }
        else // node is not first node
        {
            r=first;
            while(r->next!=q)
            {
                r=r->next;
            }

            r->next=q->next;

            printf("\n\n The data %d is deleted",q->data);

            free(q);
        }
    }
}

void display()
{
    if(first==NULL)
    {
        printf("\n\n The list empty ");
    }
    else
    {
      q=first;

        while(q!=NULL)
        {
            printf("\n\n Data=%d \t *node=%u",q->data,q->next);
            q=q->next;
        }
    }
}

