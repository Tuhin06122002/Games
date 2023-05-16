#include <bits/stdc++.h>

using namespace std;

typedef struct Node* link;
struct Node{int data; link next;};

link HEAD = new Node[1];

int main()
{
    int n,i,m;
    cin>>n>>m;

    link curr = HEAD;

    for(i=0;i<n;i++)
    {
        link t = new Node[1];
        t->data = i+1;
        curr->next = t;
        curr = curr->next;
    }

    curr->next = HEAD->next;

    //prints the linked list
    link c = HEAD;
    for(i=0;i<n;i++)
    {
        cout<<c->next->data<<" ";
        c = c->next;
    }
    cout<<endl;

    curr = HEAD->next;
    
    while(curr->next != curr)
    {
        for(i=0;i<m-1;i++)
            curr = curr->next;
        curr->next = curr->next->next;
        curr = curr->next;

        // //prints the linked list
        // n--;
        // link c = HEAD;
        // for(i=0;i<n;i++)
        // {
        //     cout<<c->next->data<<" ";
        //     c = c->next;
        // }
        // cout<<endl;        
    }

    cout<<curr->data;

    return 0;
}