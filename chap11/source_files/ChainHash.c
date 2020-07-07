#include<stdio.h>
#include<stdlib.h>
#include"Member.h"
#include"ChainHash.h"

static int hash(int key, int size)
{
  return key % size;
}

static void SetNode(Node *n, const Member *x, const Node *next)
{
  n->data = *x;
  n->next = next;
}

int Initialize(ChainHash *h, int size)
{
  int i;

  if((h->table = calloc(size, sizeof(Node *))) == NULL){
    h->size = 0;
    return 0;
  }
  h->size = size;
  for(i = 0; i < size; i++)
    h->table[i] = NULL;
  return 1;
}

Node *Search(const ChainHash *h, const Member *x)
{
  int key;
  Node *p;

  key = hash(x->no, h->size);
  p = h->table[key];

  while(p != NULL){
    if(p->data.no == x->no)
      return p;
    p = p->next;
  }

  return NULL;
}

int Add(ChainHash *h, const Member *x)
{
  int key;
  Node *p;
  Node *temp;

  key = hash(x->no, h->size);
  p = h->table[key];
  while(p != NULL){
    if(p->data.no == x->no)
      return 1;
    p = p->next;
  }
  if((temp = calloc(1, sizeof(Node))) == NULL)
    return 2;
  SetNode(temp, x, h->table[key]);
  h->table[key] = temp;
  return 0;
}

int Remove(ChainHash *h, const Member *x)
{
  int key;
  Node *p;
  Node **pp;

  key = hash(x->no, h->size);
  p = h->table[key];
  pp = &h->table[key];
  while(p != NULL){
    if(p->data.no == x->no){
      *pp = p->next;
      free(p);
      return 0;  
    }
    pp = &p->next;
    p = p->next;
  }
  
  return 1;
}

void Dump(const ChainHash *h)
{
  int i;
  Node *p;

  for(i = 0; i < h->size; i++){
    p = h->table[i];
    printf("%02d ", i);
    while(p != NULL){
      printf("-> %d :(%s) ", p->data.no, p->data.name);
      p = p->next;
    }
    putchar('\n');
  }
}
