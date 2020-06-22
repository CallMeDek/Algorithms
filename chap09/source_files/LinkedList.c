#include<stdio.h>
#include<stdlib.h>
#include"Member.h"
#include"LinkedList.h"

static Node *AllocNode(void)
{
  return calloc(1, sizeof(Node));
}

static void SetNode(Node *n, const Member *x, const Node *next)
{
  n->data = *x;
  n->next = next;
}

void Initialize(List *list)
{
  list->head = NULL;
  list->crnt = NULL;
}
