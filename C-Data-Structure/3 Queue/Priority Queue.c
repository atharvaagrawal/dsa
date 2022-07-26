/*
    Priority Queue Ascending Order
*/
#include<stdio.h>
#include<process.h>

struct node
{
    int data;
    int priority;
    struct node *next;
}*front;

void enqueue();
void dequeue();
void display();

int main()
{
   int ch;
   while(1)
   {
       printf("\n\n Menu: ");
       printf("\n 1.Insert: ");
       printf("\n 2.Delete: ");
       printf("\n 3.Display: ");
       printf("\n 4.Exit: ");

       printf ("\n\n Enter your choice(1/2/3/4): ");
       scanf("%d",&ch);

       switch(ch)
       {
           case 1: enqueue();
                    break;
           case 2: dequeue();
                    break;
           case 3: display();
                    break;

           case 4: exit(0);

           default: printf("\n\n Wrong Choice. ");
       }
   }

   return 0;
}

void enqueue()
{
  struct node *temp,*t;

  temp = (struct node*)malloc(sizeof(struct node));
  t = (struct node*)malloc(sizeof(struct node));

  printf("\n\n Enter value to be inserted and Priority: ");
  scanf("%d%d", &temp->data,&temp->priority);

  temp->next = NULL;

   if(front==NULL)
   {
      front=temp;
   }
   else if(front->priority > temp->priority)
   {
      temp->next=front;
      front=temp;
   }
   else
   {
      t=front;
      while(t->next != NULL && (t->next)->priority<=temp->priority)
      {
            t=t->next;
      }
      temp->next=t->next;
      t->next=temp;
   }
}
void dequeue()
{
    if(front!=NULL)
    {
        printf("\n\n Removed element: %d",front->data);
        front=front->next;
    }
    else
    {
        printf("\n\n Queue is Empty.");
    }

}
void display()
{
  int i;
  struct node *temp=front;

  while(temp != NULL)
  {
      printf("\n Data=%d  Priority=%d",temp->data,temp->priority);
      temp=temp->next;
  }
}
