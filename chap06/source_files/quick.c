#include"quick.h"
#include"IntStack.h"

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

void quick_iterative(int a[], int left, int right)
{
  IntStack lstack;
  IntStack rstack;
  int pl, pr, x;

  Initialize(&lstack, right - left + 1);
  Initialize(&rstack, right - left + 1);

  Push(&lstack, left);
  Push(&rstack, right);

  while(!IsEmpty(&lstack)){
    pl = (Pop(&lstack, &left), left);
    pr = (Pop(&rstack, &right), right);
    x = a[(left + right) / 2];
    do{
      while(a[pl] < x) pl++;
      while(a[pr] > x) pr--;
      if(pl <= pr){
        swap(int, a[pl], a[pr]);
        pl++;
        pr--;
      }
    }while(pl <= pr);

   if(left < pr){
     Push(&lstack, left);
     Push(&rstack, pr);
   } 
   if(pl < right){
     Push(&lstack, pl);
     Push(&rstack, right);
   }
  }

  Terminate(&lstack);
  Terminate(&rstack);
}

int main(void)
{
  int i, nx;
  int *x;
  int *x2;

  puts("퀵 정렬");
  printf("요소 개수 : ");
  scanf("%d", &nx);
  x = malloc(nx * sizeof(int));
  x2 = calloc(nx, sizeof(int));
  for(i = 0; i < nx; i++){
    printf("x[%d]: ", i);
    scanf("%d", &x[i]);
    x2[i] = x[i];
  }
  quick(x, 0, nx-1);
  puts("오름차순으로 정렬했습니다.");
  print_values(x, 0, nx);
  
  quick_iterative(x2, 0, nx - 1);
  puts("오름차순으로 정렬했습니다.");
  print_values(x2, 0, nx);
  free(x);
  free(x2);
  return 0;
}
