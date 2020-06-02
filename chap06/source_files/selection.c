#include<stdio.h>
#include<stdlib.h>

#define swap(type, a, b) do{type temp = a; a = b; b = temp;}while(0)

void selection(int a[], int n)
{
  int i, j, min;
  
  for(i = 0; i < n - 1; i++){
    min = i;
    for(j = i + 1; j < n; j++)
      if(a[j] < a[min])
        min = j;
    swap(int, a[i], a[min]);  
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
  printf("선택 정렬\n");
  printf("요소 개수: ");
  scanf("%d", &nx);
  x = calloc(nx, sizeof(int));
  get_values(x, nx);
  selection(x, nx);
  printf("정렬 후: ");
  Print(x, nx);

  free(x);

  return 0;
}
