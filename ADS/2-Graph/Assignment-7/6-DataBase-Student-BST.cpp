/*
Q6.Create a database of Students using Binary Search Tree.Database must contain rollnumber(key for BST),
name,hometown,birthdate of student.One must be able to search student by rollnumber,update the data of student
and delete the student.

33303
Atharva Agrawal
Dhule
07 02 2002

31224
Rohit Dhengle
Solapur
17 04 2002

33313
Soham Sheth
Raigad
27 05 2001

33320
Atharva Joshi
Bhusawal
18 01 2002

33340
Piyush Bonde
Jalgaon
10 2 2002

33360
Yash Bhujbal
Pune
25 12 2002
0
*/

#include<iostream>
#include<string.h>

using namespace std;

class Date
{
	public:
		int month,day,year;
};

class Student
{
	public:
		int roll_no;
		char name[20];
		char hometown[30];
		Date birthdate;                                                            
};

class Node
{	
	public:
		Student data;
		Node* left,*right;
		
		Node()
		{
			left = right = NULL;
		}	
		
		Node(Student val)
		{
			data = val;
			cout<<data.roll_no<<endl;
			left = right = NULL;
		}
};

class BST
{
	Node *root;
	
	public:
		BST()
		{
			root = NULL;
		}
		
		Node* getRoot()
		{
			return root;
		}
		
		void create_rec();
		Node* insert(Node *t,Student s);
		
		void search();
		void update();
		void delete_();
		void display();
		void inorder(Node*);
		int search_rec(Node *t,int roll);
		Node* findMin(Node* t);
		Node* delete_rec(Node* t,int x);
		Node* update_rec(Node *t,int roll);
		
};

void BST::create_rec()
{
	while(1)
	{
		Student s1;
			
		cout<<"\n\n Enter Data:";
	
		cout<<"\n Enter RollNo 0 to Stop:";
		cin>>s1.roll_no;
		
		if(s1.roll_no == 0)
			break;
				
		cin.ignore();
		cout<<"\n Enter Name:";
		cin.getline(s1.name,20);
	
		cout<<"\n Enter Hometown:";
		cin.getline(s1.hometown,30);
		
		
		cout<<"\n Enter BirthDate Day Month Year:";
		cin>>s1.birthdate.day>>s1.birthdate.month>>s1.birthdate.year;
		
		root = insert(root,s1);
	}
}

Node* BST::insert(Node *t,Student s)
{
	if(t == NULL)
	{
		t = new Node(s);
		return t;
	}
	
	if( s.roll_no > t->data.roll_no )
	{
		t->right = insert(t->right,s);
		return t;
	}
	else if( s.roll_no < t->data.roll_no )
	{
		t->left = insert(t->left,s);
		return t;
	}
	else
	{
		cout<<"\n\n Duplicate Roll No";
		return t;	
	}	
}

void BST::inorder(Node* t)
{
	if( t!=NULL )
	{
		inorder(t->left);
		cout<<endl<<t->data.roll_no<<"\t"<<t->data.name<<"\t\t"<<t->data.hometown<<"\t\t"<<t->data.birthdate.day<<"/"<<t->data.birthdate.month<<"/"<<t->data.birthdate.year;
		inorder(t->right);
	}
}

void BST::display()
{
	cout<<"\n\n Student Data:";		
	cout<<"\n RollNo \t Name \t\t HomeTown \t\t Birthdate";
	
	inorder(getRoot());
}

void BST::search()
{
	int roll;
	cout<<"\n\n Enter RollNo to Search:";
	cin>>roll;
	
	if(search_rec(root,roll))
	{
		cout<<"\n\n RollNo "<<roll<<" Found!";
	}
	else
	{
		cout<<"\n\n RollNo "<<roll<<" Not Found!";
	}
}

int BST::search_rec(Node *t,int roll)
{
	if(t == NULL)
	{
		return 0;
	}
	
	if(roll < t->data.roll_no)
	{
		return search_rec(t->left,roll);
	}
	else if(roll > t->data.roll_no)
	{
		return search_rec(t->right,roll);
	}
	else
	{
		return 1;
	}
}

void BST::update()
{
	int roll;
	cout<<"\n\n Enter RollNo to Update:";
	cin>>roll;
	
	if(search_rec(root,roll))
	{
		Node* t= update_rec(root,roll);
		
		cout<<"\n\n Name:"<<t->data.name;
		
		char update[30] = "0";
		cin.ignore();
		cout<<"\n Enter New Name 0 to Skip:";
		cin.getline(update,30);
		
		if( update[0] != '0')
		{
			strcpy(t->data.name,update);
		}
		
		cout<<"\n Enter Hometown 0 to Skip:";
		cin.getline(update,30);
		if( update[0] != '0')
		{
			strcpy(t->data.hometown,update);			
		}
		
		int m,d,y;
		cout<<"\n Enter DOB day month year 0 to Skip:";
		cin>>d>>m>>y;
		
		if( d != '0')
		{
			t->data.birthdate.month = m;
			t->data.birthdate.day = d;
			t->data.birthdate.year = y;
		}
	}
	else
	{
		cout<<"\n\n RollNo "<<roll<<" Not Found!";
	}
	
}

Node* BST::update_rec(Node *t,int roll)
{
	if(t == NULL)
	{
		return NULL;
	}
	
	if(roll < t->data.roll_no)
	{
		return update_rec(t->left,roll);
	}
	else if(roll > t->data.roll_no)
	{
		return update_rec(t->right,roll);
	}
	else
	{
		return t;
	}
}


void BST::delete_()
{
	int roll;
	cout<<"\n\n Enter RollNo to Delete:";
	cin>>roll;
	
	root = delete_rec(root,roll);	
}

Node* BST::delete_rec(Node* t,int x)
{
	if( t == NULL)
	{
		cout<<"\n Element Not found";
		return NULL;
	}
	
	if(x < t->data.roll_no)
	{
		t->left =delete_rec(t->left,x);
		return t;
	}
	else if(x > t->data.roll_no)
	{
		t->right = delete_rec(t->right,x);
		return t;
	}
	
	// Element found
	if( t->left == NULL && t->right == NULL)
	{
		delete t;
		cout<<"\n Element Deleted Successfully!";
		return NULL;
	}
	
	if( t->left == NULL)
	{
		Node *p = t->right;
		cout<<"\n Element Deleted Successfully!";
		delete t;
		return p;
	}
	
	if( t->right == NULL)
	{
		Node *p = t->left;
		cout<<"\n Element Deleted Successfully!";
		delete t;
		return p;
	}
	
	// Node having 2 child
	Node *p = findMin(t->right);	
	t->data = p->data;
	t->right = delete_rec(t->right,p->data.roll_no);
	
	return t;
}

Node* BST::findMin(Node* t)
{
	if(t == NULL)
	{
		return NULL;
	}
	
	while(t->left != NULL)
	{
		t = t->left;
	}
	
	return t;
}

int main()
{
	BST t;
	t.create_rec();
	int c,i=1;
	while(i)
	{
		cout<<"\n\n Menu";
		cout<<"\n 1 - Display";
		cout<<"\n 2 - Search";
		cout<<"\n 3 - Delete";
		cout<<"\n 4 - Update";
		cout<<"\n 5 - Stop";
		
		cout<<"\n Enter Choice:";
		cin>>c;

		switch(c)
		{
			case 1:	t.display();
					break;
	
			case 2: t.search();
					break;
		
			case 3:	t.delete_();		
					break;
			case 4:	t.update();
					break;
					
			case 5: i = 0;
					break;	
			
			default: cout<<"\n\n Enter Correct Choice!";
					break;
		}
	}
	
	return 0;
}
