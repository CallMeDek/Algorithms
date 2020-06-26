#ifndef __ArrayLinkedList__
#define __ArrayLinkedList__

#include"Member.h"

#define NULL -1

typedef int Index;

typedef struct{
  Member data;
  Index next;
  Index Dnext;
}Node;

typedef struct{
  Node *n;
  Index head;
  Index max;
  Index deleted;
  Index crnt;
}List;

void Initialize(List *, int);
Index search(List *, const Member *, int (const Member *, const Member *));
void InsertFront(List *, const Member *);
void InsertRear(List *, const Member *);
void RemoveFront(List *);
void RemoveRear(List *);
void RemoveCurrent(List *);
void Clear(List *);
void PrintCurrent(const List *);
void Print(const List *);
void Terminate(List *);

#endif
