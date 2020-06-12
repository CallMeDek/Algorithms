#include<stdio.h>
#include"IntSet.h"

int main(void)
{
  int i;
  IntSet s1, s2, s3;

  Initialize(&s1, 24);
  Initialize(&s2, 24);
  Initialize(&s3, 24);

  for(i = 10; i < 30; i += 5)
    Add(&s1, i);

  Assign(&s2, &s1);
  Add(&s2, 12);
  Remove(&s2, 20);
  Assign(&s3, &s2);

  printf("s1 = "); Print(&s1);
  printf("s2 = "); Print(&s2);
  printf("s3 = "); Print(&s3);

  printf("집합 s1에 15가 들어 있%s.\n", IsMember(&s1, 15) > 0 ? "습니다" : "지 않습니다");
  printf("집합 s2에 25가 들어 있%s.\n", IsMember(&s2, 25) > 0 ? "습니다" : "지 않습니다");
  printf("집합 s1과 s2는 서로 같%s.\n", Equal(&s1, &s2) ? "습니다" : "지 않습니다");
  printf("집합 s2와 s3는 서로 같%s.\n", Equal(&s2, &s3) ? "습니다" : "지 않습니다");

  Terminate(&s1);
  Terminate(&s2);
  Terminate(&s3);

  return 0;
}

