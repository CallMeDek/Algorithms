#include <stdio.h>

int main(void)
{
  int i, n;
  int sum;

  puts("The sum of 1 through n");
  printf("n: ");
  scanf("%d", &n);
  sum = 0;
  for(i = 1; i <= n; i++)
    sum += i;
  
  printf("The sum of 1 through %d is %d.\n", n, sum);
  
  return 0;
}
