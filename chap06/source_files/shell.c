#include"shell.h"

void shell1(int a[], int n)
{
  int i, j, h;
  int temp;  

  for(h = n / 2; h > 0; h /= 2)
    for(i = h; i < n ; i++){
      temp = a[i];
      for(j = i - h; j >= 0 && a[j] > temp; j-= h)
        a[j + h] = a[j];
      a[j + h] = temp;  
    }
}

void shell2(int a[], int n)
{
  int i, j, h;
  int temp;
  
  for(h = 1; h < n/9; h = h*3+1)
    ;
  for(; h > 0; h /= 3)
    for(i = h; i < n; i++){
      temp = a[i];
      for(j = i - h; j >= 0 && a[j] > temp; j -= h)
        a[j + h] = a[j];
      a[j + h] = temp;
    }
}

int main(void)
{
  int i, nx;
  int *x;
  int *x_copy;
  clock_t start1, start2, end1, end2;
  float res1, res2;
   
  puts("셸 정렬");
  printf("요소 개수 : ");
  scanf("%d", &nx);
  x = calloc(nx, sizeof(int));
  x_copy = malloc(nx * sizeof(int));

  for(i = 0; i < nx; i++){
    printf("x[%d] : ", i);
    scanf("%d", &x[i]);
    x_copy[i] = x[i];
  }
  
  start1 = clock();
  shell1(x, nx);
  end1 = clock();

  start2 = clock();
  shell2(x_copy, nx);
  end2 = clock();

  puts("오름차순으로 정렬했습니다.");
  puts("SHELL1");
  for(i = 0; i < nx; i++)
    printf("%d ", x[i]);
  putchar('\n');
  res1 = (float)(end1 - start1)/CLOCKS_PER_SEC;
  printf("1st version: %.3f\n", res1);
  
  puts("SHELL2");
  for(i = 0; i < nx; i++)
    printf("%d ", x_copy[i]);
  putchar('\n');
  res2 = (float)(end2 - start2)/CLOCKS_PER_SEC;
  printf("2nd version: %.2f\n", res2);
  
  free(x);
  free(x_copy);  

  return 0;
}
