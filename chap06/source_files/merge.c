#include"merge.h"

void __mergesort(int a[], int left, int right)
{
  if(left < right){
    int center, p, i, j, k;
    
    center = (left + right)/2;
    p = j = 0;
    k = left;
    __mergesort(a, left, center);
    __mergesort(a, center + 1, right);
    for(i = left; i <= center; i++)
      buff[p++] = a[i];
    while(i <= right && j < p)
      a[k++] = (buff[j] <= a[i]) ? buff[j++] : a[i++];
    while(j < p)
      a[k++] = buff[j++];
  }
}

int mergesort(int a[], int n)
{
  if((buff = (int *)calloc(n, sizeof(int))) == NULL)
    return -1;
  __mergesort(a, 0, n - 1);
  free(buff);
  return 0;
}

int main(void)
{
  int i, nx;
  int *x;
  
  puts("병합 정렬");
  printf("요소 개수: ");
  scanf("%d", &nx);
  x = malloc(nx * sizeof(int));
 
  for(i = 0; i < nx; i++){
    printf("x[%d]: ", i);
    scanf("%d", &x[i]);
  }
  
  mergesort(x, nx);
  puts("오름차순으로 정렬했습니다.");
  for(i = 0; i < nx; i++)
    printf("%d ", x[i]);
  putchar('\n');

  free(x);

  return 0;
}
