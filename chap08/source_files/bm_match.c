#include<limits.h>
#include<string.h>
#include"bm_match.h"

int bm_match(const char txt[], const char pat[])
{
  int pt, pp;
  int txt_len, pat_len;
  int skip[UCHAR_MAX + 1];

  txt_len = strlen(txt);
  pat_len = strlen(pat);

  for(pt = 0; pt <= UCHAR_MAX; pt++)
    skip[pt] = pat_len;
  for(pt = 0; pt < pat_len - 1; pt++)
    skip[pat[pt]] = pat_len - pt - 1;

  while(pt < txt_len){
    pp = pat_len - 1;
    while(txt[pt] == pat[pp]){
      if(pp == 0)
        return pt;
      pp--;
      pt--;
    }
   pt += (skip[txt[pt]] > pat_len - pp) ? skip[txt[pt]] : pat_len - pp;
  }

  return -1;
}
