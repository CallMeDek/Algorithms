#ifndef __CircDblLinkedList__
#define __CircDblLinkedList__
#include"Member.h"

typedef struct __node{
  Member data;
  struct __node *prev;
  struct __node *next;
}Dnode;

typedef struct{
  Dnode *head;
  Dnode *crnt;
}Dlist;

void Initialize(Dlist *);
void PrintCurrent(const Dlist *);
Dnode *Search(Dlist *, const Member *,
              int (const Member *, const Member *));
void Print(const Dlist *);
void PrintReverse(const Dlist *);
int Next(Dlist *);
int Prev(Dlist *);
void InsertAfter(Dlist *, Dnode *, const Member *);
void InsertFront(Dlist *, const Member *);
void InsertRear(Dlist *, const Member *);
void Remove(Dlist *, Dnode *);
void RemoveFront(Dlist *);
void RemoveRear(Dlist *);
void RemoveCurrent(Dlist *);
void Clear(Dlist *);
void Terminate(Dlist *);

#endif
