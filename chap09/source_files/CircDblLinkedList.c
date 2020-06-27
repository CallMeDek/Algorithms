#include<stdio.h>
#include<stdlib.h>
#include"CircDblLinkedList.h"

static Dnode *AllocDNode(void)
{
  return calloc(1, sizeof(Dnode));
}

static void SetDNode(Dnode *n, const Member *x, const Dnode *prev, const Dnode *next)
{
  n->data = *x;
  n->prev = prev;
  n->next = next;
}

static int IsEmpty(const Dlist *list)
{
  return list->head->next == list->head;
}

void Initialize(Dlist *list)
{
  Dnode *dummpyNode = AllocDNode();
  list->head = list->crnt = dummyNode;
  dummyNode->prev = dummyNode->next = dummyNode;
}

void PrintCurrent(const Dlist *list)
{
  if(IsEmpty(list))
    printf("선택한 노드가 없습니다.");
  else
    PrintMember(&list->crnt->data);
}
