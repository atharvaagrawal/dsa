/*
 Fibonacci Series using Recursion
 0 1 1 2 3 5 8 13 21
*/
#include<stdio.h>

void fibo(int num);

int main()
{
   int num;

   printf("\n\n Enter any number: ");
   scanf("%d",&num);

   printf("\n\n Fibonacci Series: ");
   fibo(num);


   return 0;
}

void fibo(int num)
{
   static int f1=0,f2=1,f3=0;

   if(num>0)
   {
       printf(" %d ",f3);
       f3=f2+f1;
       f2=f1;
       f1=f3;

       fibo(num-1);
   }
}
