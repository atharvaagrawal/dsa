/* Insertion Sort */
#include<stdio.h>
#include<conio.h>

int main()
{
	int a[100],i,j,k,temp,n;
	
	printf("\n\nEnter the size of an array: ");
	scanf("%d",&n);
	
	printf("\n\nEnter the %d number of elements: ",n);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
		
	printf("\n\nArray Before sorting: ");
	for(i=0;i<n;i++)
		printf(" %d ",a[i]);
	
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
	
	printf("\n\nArray elements after sorting: ");
	
	for(i=0;i<n;i++)
	{
		printf(" %d ",a[i]);
    }
	getch();
	
}
