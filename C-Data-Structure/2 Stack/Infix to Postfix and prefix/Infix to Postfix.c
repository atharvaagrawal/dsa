/* INfix to Postfix*/
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
void intopost(stack *s,char infix[]);

int main()
{
   char infix[SIZE];
   stack s;
   
   printf("\n\n Enter the infix string: ");
   scanf("%s",infix);	
   
   intopost(&s,infix);
   
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
void intopost(stack *s,char infix[])
{ 
   char postfix[SIZE],ch;
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
	 	postfix[j]=ch;
	 	j++;
	 }
	 else if(ch==')')
	 {
	 	while(s->data[s->top] != '(')
	 	{
	 		postfix[j]=pop(s);
			j++; 	 	
		}
		s->top--;
	 }
	 else 
	 {
	 	while(priority(ch)<=priority(s->data[s->top]))
	 	{
	 		postfix[j]=pop(s);
	 		j++;
		}
		push(s,ch);
	 }
   }
   while(s->data[s->top] != '#' )
   {
   	 postfix[j]=pop(s);
   	 j++;
   }
   postfix[j]='\0';
   printf("\n\n The Postfix String: %s",postfix);
}
