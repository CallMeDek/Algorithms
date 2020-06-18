#include<stdio.h>
#include"bf_match.h"
#include"kmp_match.h"

int main(void)
{
  int idx;
  char s1[256]; char s2[256];
  
  puts("브루트-포스법");
  printf("텍스트: ");
  scanf("%s", s1);
  printf("패턴: ");
  scanf("%s", s2);
  idx = bf_match(s1, s2);
  if(idx == -1)
    puts("텍스트에는 패턴이 없습니다.");
  else
    printf("%d번째 문자부터 match합니다.\n", idx+1);
  
  puts("KMP법");
  printf("텍스트: ");
  scanf("%s", s1);
  printf("패턴: ");
  scanf("%s", s2);
  idx = kmp_match(s1, s2);
  if(idx == -1)
    puts("텍스트에는 패턴이 없습니다.");
  else
    printf("%d번째 문자부터 match합니다.\n", idx+1);


  return 0;
}
