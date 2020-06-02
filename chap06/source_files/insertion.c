#include<stdio.h>
#include<stdlib.h>

void insertion(int a[], int n)
{
  int i, j, tmp;

  for(i = 1; i < n; i++){
    tmp = a[i];
    for(j = i; j > 0 && a[j - 1] > tmp; j--)
      a[j] = a[j - 1];
    a[j] = tmp; 
  }
}

void get_values(int a[], int n)
{
  int i;

  for(i = 0; i < n; i++){
    printf("x[%d] : ", i);
    scanf("%d", &a[i]);
  } 
}

void Print(int a[], int n)
{
  int i;
 
  for(i = 0; i < n; i++){
    printf("%d ", a[i]);     
  }
  putchar('\n');
}

int main(void)
{
  int nx;
  int *x;
  printf("삽입 정렬\n");
  printf("요소 개수: ");
  scanf("%d", &nx);
  x = calloc(nx, sizeof(int));
  get_values(x, nx);
  insertion(x, nx);
  printf("정렬 후: ");
  Print(x, nx);

  free(x);

  return 0;
}
