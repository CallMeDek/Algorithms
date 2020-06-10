#include"heap.h"

void downheap(int a[], int left, int right)
{
  int temp, child, parent;
  int cl, cr;

  temp = a[left];
  for(parent = left; parent < (right + 1)/2; parent = child){
    cl = parent * 2 + 1;
    cr = cl + 1;
    child = (cr <= right && a[cr] > a[cl]) ? cr : cl;
    if(temp >= a[child])
      break;
    a[parent] = a[child];  
  }
  a[parent] = temp;
}

void heapsort(int a[], int n)
{
  int i;

  for(i = (n - 1) / 2; i >= 0; i--)
    downheap(a, i, n - 1);
  for(i = n - 1; i > 0; i--){
    swap(int, a[0], a[i]);
    downheap(a, 0, i - 1);
  } 
}
