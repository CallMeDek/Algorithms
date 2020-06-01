#include"bubble1.h"

void bubble(int a[], int n)
{
  int i, j;
  for(i = 0; i < n - 1; i++){
    for(j = n - 1; j > i; j--)
      if(a[j - 1] > a[j])
        swap(int, a[j - 1], a[j]);
  }
}

void bubble2(int a[], int n)
{
  int i, j, exchg;
  for(i = 0; i < n - 1; i++){
    exchg = 0;
    for(j = n - 1; j > i; j--)
      if(a[j - 1] > a[j]){
        swap(int, a[j - 1], a[j]);
        exchg++;
      }
    if(exchg == 0) break;
  }
}

void bubble3(int a[], int n)
{
  int j, k, last;
  for(k = 0; k < n - 1; ){
    last = n - 1;
    for(j = n - 1; j > k; j--){
      if(a[j - 1] > a[j]){
        swap(int, a[j - 1], a[j]);
        last = j;
      }
    }
    k = last;
  }
}

void copy(int ori[], int cpy[], int n)
{
  int i;
  for(i = 0; i < n; i++)
    cpy[i] = ori[i];
}

int main(void)
{
  int i, nx;
  int *x;
  int *a;
  int *b;
  int *c;

  clock_t start1, start2, start3, end1, end2, end3;
  float res1, res2, res3;

  puts("버블 정렬");
  printf("요소 개수 : ");
  scanf("%d", &nx);
  x = malloc(sizeof(int) * nx);
  a = malloc(sizeof(int) * nx);
  b = malloc(sizeof(int) * nx);
  c = malloc(sizeof(int) * nx);
  
  for(i = 0; i < nx; i++){
    x[i] = nx - i;
  }

  copy(x, a, nx);
  copy(x, b, nx);
  copy(x, c, nx);

  start1 = clock();
  bubble(a, nx);
  end1 = clock();
  res1 = (float)(end1 - start1)/CLOCKS_PER_SEC;
  printf("1st version : %.3f \n", res1);  
   
  start2 = clock();
  bubble2(b, nx);
  end2 = clock();
  res2 = (float)(end2 - start2)/CLOCKS_PER_SEC;
  printf("2nd version : %.3f \n", res2);  

  start3 = clock();
  bubble3(c, nx);
  end3 = clock();
  res3 = (float)(end3 - start3)/CLOCKS_PER_SEC;
  printf("3rd version : %.3f \n", res3);  
  
  free(x);
  free(a);
  free(b);
  free(c);

  return 0;
}
