#ifndef __CLOSEDHASH__
#define __CLOSEDHASH__

#include"Member.h"

typedef enum{
  Occupied, Empty, Deleted
}Status;

typedef struct{
  Member data;
  Status stat;
}Bucket;

typedef struct{
  int size;
  Bucket *table;
}ClosedHash;

int Initialize(ClosedHash *, int );
Bucket *Search(const ClosedHash *, const Member *);
int Add(ClosedHash *, const Member *);
int Remove(ClosedHash *, const Member *);
void Dump(const ClosedHash *);
void Clear(ClosedHash *);
void Terminate(ClosedHash *);

#endif
