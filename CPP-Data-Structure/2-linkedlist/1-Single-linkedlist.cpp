#include <iostream>
#define deb(x) cout << #x << '=' << x << endl
using namespace std;

class Node
{
public:
    int data;
    Node *next;

    Node()
    {
        data = 0;
        next = NULL;
    }
    Node(int data)
    {
        this->data = data;
        this->next = NULL;
    }
};

class LinkedList
{
    Node *head;

public:
    LinkedList()
    {
        head = NULL;
    }

    void insert(int ele)
    {
        Node newNode = Node(ele);

        cout << "\n\n NewNode:" << newNode.data << " Address:" << &newNode;

        if (head == NULL)
        {
            head = &newNode;
            cout << "\n\n " << head->data << head->next;
        }
        else
        {
            Node *temp = head;

            while (temp->next != NULL)
            {
                temp = temp->next;
            }

            temp->next = &newNode;
            cout << "\n\n temp:" << temp->next->data << " temp seld:" << temp->data;
        }
    }
    void display();
};

void LinkedList::display()
{
    // cout << "\n here" << head;
    if (head == NULL)
    {
        cout << "\n\n List is Empty";
        return;
    }

    Node *temp = head;

    cout << "\n\n Elements in LinkedList: \n";
    while (temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
}

int main()
{
    LinkedList l;
    cout << " hello \n";

    // l.display();
    l.insert(10);
    l.insert(20);
    l.insert(30);
    l.insert(40);
    l.insert(50);

    l.display();
    return 0;
}