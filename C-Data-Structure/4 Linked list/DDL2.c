/*Double linked list all operation */
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

void delete();
void append();
int length();
void addatbegin();
void addatafter();
void display();

struct node
{
  int data;
  struct node* left;
  struct node* right;
};
struct node* root=NULL;

int main()
{
  int ch,len;

  while(1)
  {
     printf("\n\n Single Linked list operations :");
     printf("\n 1.Append ");
     printf("\n 2.Add at Begin ");
     printf("\n3.Add at after ");
     printf("\n 4.Length ");
     printf("\n 5.Display ");
     printf("\n 6.Delete ");
     printf("\n 7.Quit ");

     printf("\n\n Enter your choice(1/2/3/4/5/6/7) = ");
     scanf("%d",&ch);

     switch(ch)
     {
	case 1: append();
	       break;

	case 2: addatbegin();
	       break;

       case 3: addatafter();
	       break;

       case 4: len=length();
	       printf("\n\n Length= %d",len);
	       break;

       case 5: display();
	       break;

       case 6: delete();
	       break;

       case 7: exit(1);
	       break;

      default: printf("\n Invalid Input");
     }
  }

  return 0;
}

void append()
{
  struct node* temp;
  temp=(struct node*)malloc(sizeof(struct node));
  printf("\n Enter node data= ");
  scanf("%d",&temp->data);
  temp->left = NULL;
  temp->right = NULL;

  if(root==NULL)
  {
      root=temp;
  }
  else
  {
    struct node* p;
    p=root;

    while(p->right != NULL)
    {
       p=p->right;
    }
    p->right=temp;
    temp->left=p;
  }
}

int length()
{
   int count=0;
   struct node* temp;
   temp=root;

   while(temp!=NULL)
   {
     count++;
     temp=temp->right;
   }
   return count;
}

void addatbegin()
{
  struct node* temp;
  temp=(struct node*)malloc(sizeof(struct node));

  printf("\n Enter node data: ");
  scanf("%d",&temp->data);

  temp->left=NULL;
  temp->right=NULL;

  if(root==NULL)
  {
    root=temp;
  }
  else
  {
    temp->right=root;
    root->left=temp;
    root=temp;
  }
}

void addatafter()
{
  struct node *temp,*p;
  int loc,len,i=1;

  printf("\n\n Enter Location: ");
  scanf("%d",&loc);

  len=length();

  if(loc>len)
  {
    printf("\n\n Invalid Locations");
    printf("\n Currently list having %d nodes.",len);
  }
  else
  {
     temp=(struct node*)malloc(sizeof(struct node));

     printf("\n Enter node data: ");
     scanf("%d",&temp->data);

     temp->left=NULL;
     temp->right=NULL;

     p=root;

     while(i<loc)
     {
       p=p->right;
       i++;
     }

     temp->right=p->right;

     p->right->left=temp;

     temp->left=p;

     p->right=temp;
  }
}

void display()
{
    struct node* temp;
    temp=root;

    if(temp==NULL)
    {
      printf("\n No nodes in the list");
    }
    else
    {
       while(temp!=NULL)
       {
	 printf("\n %d",temp->data);
	 temp=temp->right;
       }
    }
}

void delete()
{
  struct node* temp;
  int loc;

  printf("\n Enter location to delete: ");
  scanf("%d",&loc);

  if(loc>length())
  {
    printf("\n Invalid Location");
  }
  else if(loc==1)
  {
     temp=root;
     root=temp->right;
     temp->right=NULL;
     root->left=NULL;
     free(temp);
  }
  else
  {
    struct node *p=root;
    int i=1;

    while(i<loc)
    {
      p=p->right;
      i++;
    }
    p->right->left=p->left;

    p->left->right=p->right;

    p->left=p->right=NULL;

    free(p);
  }
}
