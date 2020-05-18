#ifndef __INTSTACK__
#define __INTSTACK__

typedef struct{
  int max;
  int ptr;
  int *stk;
}IntStack;

int Initialize(IntStack *, int);
int Push(IntStack *, int);
int Pop(IntStack *, int *);
int Peek(const IntStack *, int *);
void Clear(IntStack *);
int Capacity(const IntStack *);
int Size(const IntStack *);
int IsEmpty(const IntStack *);
int IsFull(const IntStack *);
int Search(const IntStack *, int);
void Print(const IntStack *);
void Terminate(IntStack *);

#endif
