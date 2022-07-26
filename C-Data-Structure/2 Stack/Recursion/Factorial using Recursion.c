/*
 Factorial using Recursion
*/
#include<stdio.h>

long int factorial(int num);

int main()
{
   int num;
   long int fact;

   printf("\n\n Enter any number: ");
   scanf("%d",&num);

   fact=factorial(num);

   printf("\n\n Factorial= %ld",fact);

   return 0;
}

long int factorial(int num)
{
    long int fact=1;

    if(num==1)
    {
        return 1;
    }
    else
    {
        fact=num*factorial(num-1);
        return fact;
    }

}
