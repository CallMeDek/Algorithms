#include"IntStack.h"

int Initialize(IntStack *s, int max)
{
  s->ptr = 0;
  if((s->stk = malloc(sizeof(int)*max)) == NULL){
    s->max = 0;
    return -1;
  }
  s->max = max;
  return 0;
}
