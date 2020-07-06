#ifndef __CHAINHASH__
#define __CHAINHASH__

#include"Member.h"

typedef struct __node{
  Member data;
  struct __node *next;
}Node;

typedef struct{
  int size;
  Node **table;
}ChainHash;

int Initialize(ChainHash *, int);
Node *Search(const ChainHash *, const Member *);
int Add(ChainHash *, const Member *);
int Remove(ChainHash *, const Member *);
void Dump(const ChainHash *);
void Clear(ChainHash *);
void Terminate(ChainHash *);

#endif
