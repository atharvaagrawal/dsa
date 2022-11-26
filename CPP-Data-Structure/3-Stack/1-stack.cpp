#include <iostream>
#define deb(x) cout << #x << '=' << x << endl
#define MAX 100

using namespace std;

class Stack
{
    int top;
    int arr[MAX];

public:
    Stack()
    {
        top = -1;
    }

    void display()
    {
        cout << "\n\n Elements of the Stack: ";

        if (top == -1)
        {
            cout << "\n\n Stack is Empty";
            return;
        }
    }

    void push(int ele)
    {
        top++;
        arr[top] = ele;
        cout << "\n\n Element " << arr[top] << " is pushed onto the Stack";
    }

    int pop()
    {
        if (top == -1)
        {
            cout << "\n\n Stack is Empty";
            return -1;
        }

        return arr[top--];
    }

    bool isEmpty()
    {
        return (top >= 0);
    }
};

int main()
{
    Stack s;
    cout << "\n Element Poped: " << s.pop();

    s.push(10);
    s.push(20);
    s.push(30);
    s.push(40);
    s.push(50);

    while (s.isEmpty())
    {
        cout << "\n Element Poped: " << s.pop();
    }
}