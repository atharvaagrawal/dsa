#include <iostream>
using namespace std;

struct Node
{
    int data;
    struct Node *next = NULL;
};
struct Node *head = new Node();

void insert(int new_data)
{
    struct Node *new_node = new Node();
    new_node->data = new_data;
    new_node->next = head;
    head = new_node;
}

void display()
{
    struct Node *ptr;
    ptr = head;
    while (ptr != NULL)
    {
        cout << ptr->data << " ";
        ptr = ptr->next;
    }
}
void rearrange(struct Node *list)
{
    struct Node *p, *q;

    int temp;

    if (!list || !list->next)
        return;

    p = list;
    q = list->next;

    while (q)
    {
        temp = p->data;
        p->data = q->data;
        q->data = temp;
        p = q->next;
        q = p ? p->next : 0;
    }
}

int main()
{
    struct Node *temp;
    temp = head;
    temp->data = 1;
    for (int i = 2; i < 8; i++)
    {
        struct Node *curr = new Node();
        curr->data = i;
        temp->next = curr;
        temp = temp->next;
        //insert(i);
        cout << i << " ";
    }
    cout << "The linked list is: ";
    display();

    rearrange(head);
    cout << "\n The linked list is: ";
    display();

    return 0;
}