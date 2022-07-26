/*
    Circular Queue using array
*/
#include<stdio.h>
#define SIZE 5
typedef struct CQUEUE
{
  int data[SIZE];
  int front;
  int rear;
}cqueue;

void initialize(cqueue *q);
void enqueue(cqueue *q);
void dequeue(cqueue *q);
void display(cqueue *q);

int main()
{
    cqueue q;
    int ch;

    initialize(&q);

    while(1)
    {
        printf("\n\n Menu: ");
        printf("\n 1.Enqueue ");
        printf("\n 2.Dequeue ");
        printf("\n 3.Display ");
        printf("\n 4.Exit ");

        printf("\n\n Enter your choice: ");
        scanf("%d",&ch);

        switch(ch)
        {
            case 1: enqueue(&q);
                    break;

            case 2: dequeue(&q);
                    break;

            case 3: display(&q);
                    break;

            case 4: exit(0);

            default: printf("\n\n Wrong Choice");
        }
    }

    return 0;
}

void initialize(cqueue *q)
{
    q->front=-1;
    q->rear=-1;
}

void enqueue(cqueue *q)
{
    int data;

    if(q->front==(q->rear+1)%SIZE)
    {
        printf("\n\n Queue is Full ");
    }
    else
    {
        if(q->front==-1)
        {
            q->front++;
        }
        q->rear=(q->rear+1)%SIZE;
        printf("\n\n Enter data to insert: ");
        scanf("%d",&data);

        q->data[q->rear]=data;
    }
}

void dequeue(cqueue *q)
{
    int data;

    if(q->front==-1)
    {
        printf("\n\n Queue is Empty ");
    }
    else
    {
        data=q->data[q->front];
        if(q->front==q->rear)
        {
            q->front=-1;
            q->rear=-1;
        }
        else
            q->front=(q->front+1)%SIZE;

        printf("\n\n Deleted Element: %d",data);
    }
}

void display(cqueue *q)
{
    int i;

    if(q->front==-1)
    {
        printf("\n\n Queue is Empty ");
    }
    else
    {
        printf("\n\n Queue elements are: ");
        if(q->front < q->rear)
        {
            for(i=q->front;i<=q->rear;i++)
                printf(" %d ",q->data[i]);
        }
        else if(q->front==q->rear)
        {
            printf(" %d ",q->data[q->front]);
        }
        else //(q->front > q->rear)
        {
            for(i=0;i<=q->rear;i++)
                 printf(" %d ",q->data[i]);
            for(i=q->front;i<SIZE;i++)
                 printf(" %d ",q->data[i]);
        }
    }

}
