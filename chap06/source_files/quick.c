#include"quick.h"

void print_values(int a[], int s, int e)
{
  int i;

  for(i = s; i < e; i++)
    printf("%d ", a[i]);
  putchar('\n');
}

void quick(int a[], int left, int right)
{
  int pl;
  int pr;

  partition(a, &pl, &pr, left, right);
  if(left < pr) quick(a, left, pr);
  if(right > pl) quick(a, pl, right);
}

int main(void)
{
  int i, nx;
  int *x;

  puts("퀵 정렬");
  printf("요소 개수 : ");
  scanf("%d", &nx);
  x = malloc(nx * sizeof(int));
  for(i = 0; i < nx; i++){
    printf("x[%d]: ", i);
    scanf("%d", &x[i]);
  }
  quick(x, 0, nx-1);
  puts("오름차순으로 정렬했습니다.");
  print_values(x, 0, nx);
  free(x);

  return 0;
}
