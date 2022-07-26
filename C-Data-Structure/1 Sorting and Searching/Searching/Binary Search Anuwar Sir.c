#include<stdio.h>
#include<conio.h>
int main()
{
	int n , i , a[10]={1,2,3,4,5,6,7,8,9,10}, k=1;

	int first=0 ,item, last=10, mid=(first+last)/2;

	printf("Enter the Element you want to search: ");
	scanf("%d",&item);


	for(i=0;first<last;i++)
	{
		if(item>a[mid])
		{
			first=mid+1;
		}
		else if(item==a[mid-1])
		{
			printf("\n\n\n\n\t\t\t\tElement is found at %d",mid);
			k=0;
			break;
		}
		else //(item<a[mid])
		{
			last=mid-1;

		}

		mid=(first+last)/2;
	}

	if(k==1)
		printf("\n\n\n\n\t\t\t\tElement isn't found");
	return 0;
}
