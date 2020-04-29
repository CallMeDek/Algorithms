#include <stdio.h>

int main(void)
{
  int n;

  printf("Insert an integer: "); 
  scanf("%d", &n);

  if(n > 0) printf("This is a positive value.\n");
  else if(n < 0) printf("This is a negative value.\n");
  else printf("This is 0.\n");

  return 0;
}
