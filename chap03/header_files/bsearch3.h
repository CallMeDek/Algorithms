#ifndef __BSEARCH3__
#define __BSEARCH3__

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct{
  char name[10];
  int height;
  int weight;
}Person;

int npcmp(const Person *, const Person *);

#endif
