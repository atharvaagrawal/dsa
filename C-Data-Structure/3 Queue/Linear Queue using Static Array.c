/*
    Linear Queue using Static Array
*/
#include<stdio.h>
#include<process.h>
#define SIZE 5

typedef struct QUEUE
{
  int data[SIZE];
  int front;
  int rear;
}queue;

void initialize(queue *q);
void enqueue(queue *q,int e);
int dequeue(queue *q );
void display(queue *q);


int main()
{
  queue q;
  int ch,ele;
  initialize(&q);

  while(1)
  {
     printf("\n\n Menu: ");
     printf("\n 1.Insert  ");
     printf("\n 2.Delete  ");
     printf("\n 3.Display  ");
     printf("\n 4.Exit  ");

     printf("\n\n Enter your choice (1/2/3/4):  ");
     scanf("%d",&ch);

     switch(ch)
     {
         case 1: printf("\n\n Enter any number: ");
                 scanf("%d",&ele);

                 enqueue(&q,ele);
                 break;

        case 2: ele=dequeue(&q);
                if(ele==-999)
                    printf("\n\n Queue is Empty. ");
                else
                    printf("\n\n Deleted element: %d",ele);
                break;

        case 3: display(&q);
                break;

        case 4: exit(0);

        default: printf("\n\n Wrong Choice ");

     }

  }


  return 0;
}

void initialize(queue *q)
{
  q->rear=-1;
  q->front=-1;
}

void enqueue(queue *q,int e)
{
  if(q->rear == SIZE-1)
  {
      printf("\n\n Queue is Full: Overflow ");
  }
  else
  {
      if(q->front==-1)
        q->front++;
      q->rear++;
      q->data[q->rear]=e;
  }
}
int dequeue(queue *q )
{
  int val;
  if(q->front==-1)
  {
        return -999;
  }
  else
  {
      val=q->data[q->front];
      if(q->rear==q->front)
      {

          q->rear=-1;
          q->front=-1;
      }
      else
      {
          q->front++;
      }

      return val;
  }
}
void display(queue *q)
{
    int i;

   if(q->front==-1)

        printf("\n\n Queue is Empty: Underflow");
   else
   {
       printf("\n\n Queue element's : ");

       for(i=q->front;i<=q->rear;i++)
           printf(" %d ",q->data[i]);
   }
}

