/*
   Postfix Evaluation
*/
#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#define SIZE 100
int top=-1;
int stack[SIZE];

void push(int ch);
int pop();


int main()
{
   char postfix[SIZE],ch;
   int length,i,n1,n2,n3;

   printf("\n\n Enter postfix Expression: ");
   scanf("%s",postfix);

   length=strlen(postfix);

   for(i=0;i<length;i++)
   {
       ch=postfix[i];

       if( isdigit(ch) )
       {
           ch=ch-'0';
           push(ch);
       }
       else
       {
           n1=pop();
           n2=pop();

           switch(ch)
           {
             case '^': n3=pow(n2,n1);
                       push(n3);
                       break;

             case '*': n3=n2*n1;
                       push(n3);
                       break;
             case '/': n3=n2/n1;
                       push(n3);
                       break;
             case '+': n3=n2+n1;
                       push(n3);
                       break;

             case '-': n3=n2-n1;
                       push(n3);
                       break;

           }
        }
   }

   n3=pop();
   printf("\n\n Result= %d",n3);

   return 0;
}

void push(int ch)
{
    if(top!=SIZE-1)
    {
      top++;
      stack[top]=ch;
    }
}

int pop()
{
  int ch;

  if(top!=-1)
  {
      ch=stack[top];
      top--;
      return ch;
  }
  return 0;
}

