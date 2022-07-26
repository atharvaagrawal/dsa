#include<stdio.h>
#include<conio.h>
int main()
{
	int n , i , a[100], flag=1;
	int first=0 ,item, last, mid,j,temp,k;

    printf("Enter number of element: ");
	scanf("%d",&n);

	printf("\n\n Enter %d element: ",n);
	for(i=0;i<n;i++)
	   scanf("%d",&a[i]);

	printf("Enter the Element you want to search: ");
	scanf("%d",&item);

    // Insertion Sort
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



    last=n-1;
    mid=(first+last)/2;


	while(first<=last)
	{
		if(item>a[mid])
		{
			first=mid+1;
		}
		else if(item==a[mid])
		{
			printf("\n\n Element %d is found at %d",item,mid+1);
			flag=0;
			break;
		}
		else
		{
			last=mid-1;
		}

		mid=(first+last)/2;
	}

	if(flag==1)
		printf("\n\n Element isn't found");
	return 0;
}
