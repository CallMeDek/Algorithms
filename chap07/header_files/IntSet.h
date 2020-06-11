#ifndef __IntSet__
#define __IntSet__

typedef struct{
  int max;
  int num;
  int *set;
}IntSet;

int Initialize(IntSet *, int);
int IsMember(const IntSet *, int);
void Add(IntSet *, int);
void Remove(IntSet *, int);
int Capacity(const IntSet *);
int Size(const IntSet *);
void Assign(IntSet *, const IntSet *);
int Equal(const IntSet *, const IntSet *);
IntSet *Union(IntSet *, const IntSet *, const IntSet *);
IntSet *Intersection(IntSet *, const IntSet *, const IntSet *);
IntSet *Difference(IntSet *, const IntSet *, const IntSet *);
void Print(const IntSet *);
void Terminate(IntSet *);

#endif
