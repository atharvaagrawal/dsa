/*Program to impelement all st	ack operation using static array */

#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#define CAPACITY 5 

void push(int ele);
int pop();
void traverse();
int isFull();
int isEmpty();

int top=-1 , stack[CAPACITY];

int main()
{
  int ch ,item ;

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
	       push(item);
	       break;

       case 2 : item = pop();
	       if(item==0)
	       {
	    	 printf("\n Stack is underflow");
	       }
	       else
	       {
		      printf("\n Popped item: %d \n ",item);
	       }
	       break;
	       
       case 3 : traverse();
	       break;

       case 4 : exit(0);
	       break;

      default: printf("\n\n Invalid Input");
     }
  }
   return 0;
}

void push(int ele)
{
  if(isFull())
    printf("\n Stack is full");
  else
 {
    top++;
    stack[top]=ele;
    printf("\n %d inserted",ele);
 }
}

int pop()
{
  int ele;

  if(isEmpty())
    return 0;
  else
  {
    ele=stack[top];
    top--;
   return ele;
  } 
  return 0;
}


void traverse()
{
  int i;

  if( isEmpty() )
    printf("\n\n No element");
  else
  {
     printf("\n\n Stacks element are: ");

     for(i=0;i<=top;i++)
     {
       printf("%d\n",stack[i]);
     }
  }
}

int isFull()
{
  if(top == CAPACITY-1)
    return 1;
  else
    return 0;
}

int isEmpty()
{
  if(top== -1)
    return 1;
  else
    return 0;
}

