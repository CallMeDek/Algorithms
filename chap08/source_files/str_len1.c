#include<stdio.h>

int str_len_v1(const char *s)
{
  int len = 0;
  
  while(s[len])
    len++;
  
  return len;
}

int str_len_v2(const char *s)
{
  int len = 0;

  while(*s++)
    len++;

  return len;
}

int str_len_v3(const char *s)
{
  const char *p = s;
  
  while(*s)
    s++;
  
  return s - p;
}

int main(void)
{
  char str[256];
 
  printf("문자열: ");
  scanf("%s", str);
  printf("V1: 이 문자열의 길이는 %d입니다.\n", str_len_v1(str));
  printf("V2: 이 문자열의 길이는 %d입니다.\n", str_len_v2(str));
  printf("V3: 이 문자열의 길이는 %d입니다.\n", str_len_v3(str));

  return 0;
} 
