#ifndef __MEMBER__
#define __MEMBER__

typedef struct{
  int no;
  char name[20];
}Member;

#define MEMBER_NO 1
#define MEMBER_NAME 2

int MemberNoCmp(const Member *, const Member *);
int MemberNameCmp(const Member *, const Member *);
void PrintMember(const Member *);
Member ScanMember(const char *, int);

#endif
