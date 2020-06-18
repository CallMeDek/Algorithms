#include"bf_match.h"

int bf_match(const char txt[], const char pat[])
{
  int pt, pp;

  pt = pp = 0;
  while(txt[pt] != '\0' && pat[pp] != '\0'){
    if(txt[pt] == pat[pp]){
      pt++; pp++;
    } else {
      pt = pt - pp + 1;
      pp = 0;
    }  
  }

  if(pat[pp] == '\0')
    return pt - pp;
  return -1;
}

