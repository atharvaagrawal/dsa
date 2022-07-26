/*Program:- Quick Sort*/
#include<stdio.h>
#include<conio.h>

void quick(int a[],int first,int last);

void main()
{
  int a[30],n,i;
  clrscr();

  printf("\n\n Enter no. of Element: ");
  scanf("%d",&n);

  printf("\n\n Enter %d element: ",n);
  for(i=0;i<n;i++)
    scanf("%d",&a[i]);

  quick(a,0,n-1);

  printf("\n\n Sorted array is: ");
  for(i=0;i<n;i++)
    printf("\n %d",a[i]);

  getch();
}

void quick(int a[],int first,int last)
{
  int pivot,up,down,temp;

  if(first<last)
  {
  pivot=first;
  up=first;
  down=last;

  while(up<down)
  {
	while(a[pivot]>= a[up] && up<last)
	   up++;
	while(a[pivot]< a[down] )
	   down--;

     if(up<down)
     {
       temp=a[up];
       a[up]=a[down];
       a[down]=temp;
     }
}

temp=a[pivot];
a[pivot]=a[down];
a[down]=temp;


  quick(a,first,down-1);
  quick(a,down+1,last);
}
}

