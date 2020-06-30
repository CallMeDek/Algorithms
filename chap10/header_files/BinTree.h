#ifndef __BINTREE__
#define __BINTREE__

#include"Member.h"

typedef struct __bnode{
  Member data;
  struct __bnode *left;
  struct __bnode *right;
}BinNode;

BinNode *Search(BinNode *, const Member *);
BinNode *Add(BinNode *, const Member *);
int Remove(BinNode **, const Member *);
void PrintTree(const BinNode *);
void FreeTree(BinNode *);

#endif
