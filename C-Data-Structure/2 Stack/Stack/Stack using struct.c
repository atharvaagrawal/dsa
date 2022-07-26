/*
  Stack using Structure
*/
#include<stdio.h>
#include<conio.h>
#define SIZE 100

typedef struct STACK
{
    int data[SIZE];
    int top;
}stack;

void intialize(stack *s);
void push(stack *s,int ch);
void pop(stack *s);
void display(stack *s);

int main()
{
    stack s;
    int ch ,item ;
    intialize(&s);

      while(1)
      {
         printf("\n\n Menu: ");

         printf("\n 1.Push ");
         printf("\n 2.Pop ");
         printf("\n 3.Traverse");
         printf("\n 4.Quit");

         printf("\n\n Enter Your Choice (1/2/3/4) = ");
         scanf("%d",&ch);

         switch(ch)
         {
           case 1 :printf("\n\n Enter any element = ");
               scanf("%d",&item);
               push(&s,item);
               break;

           case 2 : pop(&s);
                  break;

           case 3 : display(&s);
               break;

           case 4 : exit(0);
               break;

          default: printf("\n\n Invalid Input");
         }
      }

   return 0;
}

void intialize(stack *s)
{
    s->top=-1;
}
void push(stack *s,int ch)
{
    if(s->top != SIZE-1 )
    {
        s->top++;
        s->data[s->top]=ch;
    }
    else
    {
        printf("\n\n Stack is Overflow.");
    }
}
void pop(stack *s)
{
    if(s->top != -1 )
    {
       printf("\n\n Deleted element: %d",s->data[s->top]);
       s->top--;
    }
    else
    {
        printf("\n\n Stack is Underflow.");
    }
}
void display(stack *s)
{
   int i;
   if(s->top!=-1)
   {
       for(i=0;i<=s->top;i++)
       {
           printf(" %d ",s->data[i]);
       }
   }
   else
   {
       printf("\n\n Stack is Empty.");
   }
}
