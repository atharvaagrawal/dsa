/*
    Radix Sort
*/
#include<stdio.h>

int passes(int a[],int n);
void radixSort(int a[],int n);
void display(int a[],int n);

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

    radixSort(a,n);

    printf("\n\n After Sorting : ");
    display(a,n);

    return 0;
}

int passes(int a[],int n)
{
    int large,i,count=0;
    large=a[0];

    for(i=0;i<n;i++)
    {
        if(large < a[i])
            large=a[i];
    }

    while(large>0)
    {
        large=large/10;
        count++;
    }

    return count;

}
void radixSort(int a[],int n)
{
    int bucket[10][10],i,j,k,div=1,num,pass,countDigit;

    int b[10]={0};

    countDigit=passes(a,n);

    for(pass=0;pass<countDigit;pass++)
    {
        for(i=0;i<10;i++)
            b[i]=0;

        for(i=0;i<n;i++)
        {
            num=(a[i]/div)%10;
            bucket[num][b[num]]=a[i];
            b[num]++;
        }
        div=div*10;
        i=0;

        for(j=0;j<10;j++)
        {
            for(k=0;k<b[j];k++)
            {
                a[i++]=bucket[j][k];
            }
        }
    }
}
void display(int a[],int n)
{
    int i;
    for(i=0;i<n;i++)
        printf(" %d ",a[i]);
}

