/*
Q2.WAP to create a DLL and implement following functions
	-create()
	-show()
	-addatbeg()
	-addatend()
	-delatbeg()
	-delatend()
	-search()
*/
#include<iostream>
using namespace std;

class Node
{
	public:
		Node* prev;
		Node* next;
		int data;
		
		Node()
		{
			data=0;
			prev=next=NULL;
		}	
		
		Node(int x)
		{
			data = x;
			prev=next=NULL;
		}
};

class DLL
{
	Node* head;
	
	public:
		DLL()
		{
			head=NULL;
		}
	
	void create();
	void show();
	void show_rev();
	void addatbeg(int x);
	void addatend(int x);
	void delatbeg();
	void delatend();
	int search(int x);
};

void DLL::create()
{
	int x;
	Node *p,*temp;
	
	while(true)
	{
		cout<<"\n Enter Data:";
		cin>>x;
		
		if(x==0)
			break;
		if(head==NULL)
		{
			p = new Node(x);
			head = p;
			temp = p;
		}
		else
		{
			temp = new Node(x);
			p->next = temp;
			temp->prev = p;			
			p = temp;
		}
	}
}

void DLL::show()
{
	Node* p;
	p = head;
	
	while(p != NULL)
	{
		cout<<p->data<<" ";
		p = p->next;
	}
}

void DLL::addatbeg(int x)
{
	Node *p;
	
	if(head == NULL)
	{
		p = new Node(x);
		head = p;
		return;	
	}
	
	p = new Node(x);
	head->prev = p;
	p->next = head;
	head = p;
}

void DLL::show_rev()
{
	Node *p;
	p = head;
	
	while(p->next != NULL)
	{
		p = p->next;
	}
	
	while(p!=NULL)
	{
		cout<<p->data<<" ";
		p = p->prev;
	}
}

void DLL::addatend(int x)
{
	Node *p,*temp;

	if(head == NULL)
	{
		p = new Node(x);
		head = p;
		return;
	}
	p = head;
	
	while(p->next != NULL)
	{
		p = p->next;
	}
	
	temp = new Node(x);
	temp->prev = p;
	p->next = temp;
}

void DLL::delatbeg()
{
	Node *p;
		
	if(head == NULL)
		return;
	else if(head->next == NULL)
	{
		head = NULL;
		return;
	}
	
	p = head;
	head = head->next;
	head->prev = NULL;
	
	p->next = NULL;
	delete p;
}

void DLL::delatend()
{
	Node *p,*temp;
	
	p = head;
	
	if(head == NULL)
		return;
	
	while(p->next != NULL)
		p = p->next;
	
	temp = p;
	p = p->prev;
	p->next = NULL;
	temp->prev = NULL;
		
	delete temp;
}

int DLL::search(int x)
{
	Node* p;
	p = head;
	
	if(head==NULL)
		return 0;
	
	while(p != NULL)
	{
		if(p->data == x)
			return 1;
		p = p->next;	
	}

	return 0;
}

int main()
{
	DLL d;
	d.create();
	cout<<"\n\n Elements in Linked List:";
	d.show();	
	cout<<"\n\n Elements in Linked List in Reverse Order:";
	d.show_rev();	
	
	int x;
	cout<<"\n\n Enter value to search:";
	cin>>x;
	if(d.search(x))
	{
		cout<<"\n Element Found";		
	}
	else
	{
		cout<<"\n Element Not Found";
	}

	d.addatbeg(10);
	cout<<"\n\n Elements in Linked List After AddAtBeg: ";
	d.show();	 
		
	d.addatend(50);
	cout<<"\n\n Elements in Linked List After AddAtEnd: ";
	d.show();	 

	d.delatend();
	cout<<"\n\n Elements in Linked List After DeleteAtEnd: ";
	d.show();	 
	
	d.delatbeg();
	cout<<"\n\n Elements in Linked List After DeleteAtBeg: ";
	d.show();	 
		
	return 0;
}
