/* Linear Search on sorted array*/
#include<stdio.h>
#include<conio.h>

int main()
{
	int a[100],i,j,k,temp,n,search,flag=0;
	
	printf("\n\nEnter the size of an array: ");
	scanf("%d",&n);
	
	printf("\n\nEnter the %d number of elements: ",n);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
		
	// Insertion sort	
	for(i=1;i<n;i++)
	{
		for(j=0;j<i;j++)
		{
			
			if(a[i]<a[j])
			{
				temp=a[i];
				for(k=i;k>j;k--)
				{
					a[k]=a[k-1];
				}
				a[j]=temp;
			}
		}
	}
	
	printf("\n\nArray elements: ");
	for(i=0;i<n;i++)
	{
		printf(" %d ",a[i]);
    }
    
	printf("\n\n Enter element do you want to search: ");
	scanf("%d",&search);
	
	for(i=0;i<n;i++)
	{
		if(search<=a[i])
		{
			if(search==a[i])
			{
				printf("\n\n Element %d is found at %d ",search,i+1);
	    		break;
			}
			else
			{
				flag=1;
				break;
			}
		}
	}
	
	if(flag==1)
	  printf("\n\n Element not found. ");
	getch();
	
}
