#include"heap.h"

int main(void)
{
  int i, nx;
  int *x;

  puts("힙 정렬");
  printf("요소 개수: ");
  scanf("%d", &nx);
  x = malloc(nx * sizeof(int));
  for(i = 0; i < nx; i++){
    printf("x[%d]: ", i);
    scanf("%d", &x[i]);
  }
  heapsort(x, nx);
  puts("오름차순으로 정렬했습니다.");
  for(i = 0; i < nx; i++)
    printf("%d ", x[i]);
  putchar('\n');
  
  free(x);

  return 0;
}
