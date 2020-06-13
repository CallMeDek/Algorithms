#ifndef __BITSET__
#define __BITSET__

typedef unsigned long BitSet;

#define BitSetNull (BitSet)0
#define BitSetBits 32
#define SetOf(no) ((BitSet)1 << (no))

int IsMember(BitSet, int);
void Add(BitSet *, int);
void Remove(BitSet *, int);
int Size(BitSet);
void Print(BitSet);

#endif
