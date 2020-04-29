#include <stdio.h>

int main(void)
{
  int i, n;
  int sum;
  
  puts("The sum of 1 through n");
  printf("n: "); scanf("%d", &n);

  sum = 0;
  i = 1;
  while(i <= n){
    sum += i;
    i++;
  }
  printf("The sum of 1 through %d is %d.\n", n, sum);
  
  return 0;
}
