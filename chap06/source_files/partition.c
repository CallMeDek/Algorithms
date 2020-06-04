#include"partition.h"

void partition(int a[], int *ptr_l, int *ptr_r, int left, int right)
{
  int pl, pr, x;

  pl = left; pr = right; 
  x = a[(pl+pr) / 2];
  do{
    while(a[pl] < x) pl++;
    while(a[pr] > x) pr--;
    if(pl <= pr){
      swap(int, a[pl], a[pr]);
      pl++;
      pr--;
    }
  }while(pl <= pr);
  *ptr_l = pl;
  *ptr_r = pr;
}

