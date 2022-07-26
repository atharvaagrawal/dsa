#include<stdio.h>
#include<conio.h>
int main()
{
    int i,j,a[5];
    int temp,count=0;

    printf("\n\n Enter any 5 element: ");
    for(i=0;i<5;i++)
       scanf("%d",&a[i]);

    printf("\n\n Element before sorting : ");
    for(i=0;i<5;i++)
       printf(" %d ",a[i]);

    for(i=0;i<4;i++)
    {
        for(j=i+1;j<5;j++)
        {
            printf("\n i=%d   j=%d  a[%d]=%d    a[%d]=%d ",i,j,j,a[j],i,a[i]);
            if(a[i]>a[j])
            {
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
        printf("\n\n");
    }

    printf("\n\n Element after sorting : ");
    for(i=0;i<5;i++)
       printf(" %d ",a[i]);

    return 0;
}
