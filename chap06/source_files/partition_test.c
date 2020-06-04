#include"partition.h"

int main(void)
{
  int i, nx;
  int *x;
  puts("배열을 나눕니다.");
  printf("요소 개수: ");
  scanf("%d", &nx);
  x = calloc(nx, sizeof(int));
  for(i = 0; i < nx; i++){
    printf("x[%d] : ", i);
    scanf("%d", &x[i]);
  }
  partition(x, nx);
  free(x);

  return 0;
}
