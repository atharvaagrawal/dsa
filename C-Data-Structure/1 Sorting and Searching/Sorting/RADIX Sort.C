/*RadixSort */
#include<stdio.h>
#include<conio.h>


void main()
{
  int a[5],b[10],bucket[10][10],i;
  int large,count=0,div,j,k,pass,num,c;
  clrscr();

  //1.Accept
  printf("\n\n Enter any 5 elementL: ");
  for(i=0;i<5;i++)
  {
     scanf("%d",&a[i]);
  }

  printf("\n\n Element Before Sort: ");
  for(i=0;i<5;i++)
  {
     printf(" %d ",a[i]);
  }

  //Count
  large=a[0];
  for(i=0;i<5;i++)
  {
     if( large < a[i] )
     {
	large=a[i];
     }
  }

  while(large>0)
  {
     large/=10;
     count++;
  }

  div=1;
  for(i=0;i<count-1;i++)
     div=div*10;
  c=count-1;
  for(pass=0;pass<count;pass++)
  {
     int b[10]={0};

     for(i=0;i<5;i++)
     {
	if(c==count-1)
	{
	  num=a[i]/div;
	}
	else
	{
	  num=(a[i]/div)%10;
	}
	printf("\n %d    %d ",num,a[i]);
	bucket[num][b[num]]=a[i];

	b[num]++;

     }
     printf("\n");
     div=div/10;
     c--;
     i=0;

     for(j=10;j>0;j--)
     {
       for(k=0;k<b[j];k++)
       {
	  a[i++]=bucket[j][k];
       }
     }
  }

  printf("\n\n Element after Sort: ");
  for(i=0;i<5;i++)
  {
     printf(" %d ",a[i]);
  }

  getch();
}