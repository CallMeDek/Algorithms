#include<stdio.h>
#include<stdlib.h>
#include"IntSet.h"

int Initialize(IntSet *s, int max)
{
  s->num = 0;
  if((s->set = calloc(max, sizeof(int))) == NULL){
    s->max = 0;
    return -1;
  }
  s->max = max;
  return 0;
}

int IsMember(const IntSet *s, int n)
{
  int i;

  for(i = 0; i < s->num; i++)
    if(s->set[i] == n)
      return i;
  return -1;
}

void Add(IntSet *s, int n)
{
  if(s->num < s->max && IsMember(s, n) == -1)
    s->set[s->num++] = n;
}

void Remove(IntSet *s, int n)
{
  int idx;
  if((idx = IsMember(s, n)) != -1){ 
    s->set[idx] = s->set[--s->num];
  }
}
