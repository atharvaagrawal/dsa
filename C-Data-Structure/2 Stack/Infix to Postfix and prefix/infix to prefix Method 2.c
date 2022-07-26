/* INfix to Prefix
  Method 2 
  left to right
  1.reverse the string 
  2.do same as postfix and minor change
                            1 Equal Priority 
  3.reverse the final answer
*/
#include<stdio.h>
#include<conio.h>
#include<ctype.h>
#include<string.h>
#define SIZE 100

typedef struct STACK
{
	char data[SIZE];
	int top;
	
}stack;

void intialize(stack *s);
void push(stack *s,char ch);
char pop(stack *s);
int priority(char ch);
void intopre(stack *s,char infix[]);

int main()
{
   char infix[SIZE];
   int i,j;
   stack s;
   
   printf("\n\n Enter the infix string: ");
   scanf("%s",infix);	
   strrev(infix);
   j=strlen(infix);
   for(i=0;i<j;i++)
   {
   	  if(infix[i]=='(')
   	       infix[i]=')';
	  else if(infix[i]==')')
	       infix[i]='(';
   }  
   printf("\n\n Revese:%s ",infix);
   intopre(&s,infix);
   
   return 0;
}

void intialize(stack *s)
{
	s->top=-1;
}
void push(stack *s,char ch)
{
	if(s->top != SIZE-1 )
	{
		s->top++;
		s->data[s->top]=ch;
	}
}
char pop(stack *s)
{
	char ch;
	if(s->top != -1)
	{
		ch=s->data[s->top];
		s->top--;
		return ch;	
	}
	return 0;
}
int priority(char ch)
{
	switch(ch)
	{
		case '^': 
		        return 3;
		         break;
		case '%':
		case '/':
		case '*':
		          return 2;
				  break;
		case '+':
		case '-':
		         return 1;
		         
		default: return 0; 
	}
}
void intopre(stack *s,char infix[])
{ 
   char  prefix[SIZE],ch;
   int length,i,j=0,k;
       
   intialize(s);	
   push(s,'#');
   
   length=strlen(infix);
   
   for(i=0;i<length;i++)
   {
   	 ch=infix[i];
   	 
	 if(ch=='(')
	 {
	 	push(s,ch);
	 }
	 else if(isalnum(ch))
	 {
	 	 prefix[j]=ch;
	 	j++;
	 }
	 else if(ch==')')
	 {
	 	while(s->data[s->top] != '(')
	 	{
	 	   prefix[j]=pop(s);
		   j++; 	 	
		}
		s->top--;
	 }
	 else 
	 {
	 	while(priority(ch)<priority(s->data[s->top]))
	 	{
	 		 prefix[j]=pop(s);
	 		j++;
		}
		push(s,ch);
	 }
   }
   while(s->data[s->top] != '#' )
   {
   	 prefix[j]=pop(s);
   	 j++;
   }
   prefix[j]='\0';

   printf("\n\n The Prefix String: %s",prefix);
}
