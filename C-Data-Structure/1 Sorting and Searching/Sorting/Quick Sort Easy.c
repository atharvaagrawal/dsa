/*
    Quick Sort
*/
#include<stdio.h>

void display(int a[],int n);
void quickSort(int a[],int first,int last);

int main()
{
    int a[100],n,i;

    printf("\n\n Enter the number of element to insert: ");
    scanf("%d",&n);

    printf("\n\n Enter %d elements: ",n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);

    printf("\n\n Before Sorting : ");
    display(a,n);

    quickSort(a,0,n-1);

    printf("\n\n After Sorting : ");
    display(a,n);

    return 0;

}

void display(int a[],int n)
{
    int i;
    for(i=0;i<n;i++)
        printf(" %d ",a[i]);
}

void quickSort(int a[],int first,int last)
{
    int pivot,up,down,i,j,temp;

    if(first<last)
    {
        pivot=first;
        up=first;
        down=last;

        while(up<down)
        {
            while(a[up]<a[pivot]&&up<last)
                up++;

            while(a[down]>a[pivot])
                down--;

            if(up<down)
            {
                temp=a[up];
                a[up]=a[down];
                a[down]=temp;
            }
        }
        temp=a[down];
        a[down]=a[pivot];
        a[pivot]=temp;

        quickSort(a,first,down-1);
        quickSort(a,down+1,last);
    }
}
