#ifndef __HEAP__
#define __HEAP__

#include<stdio.h>
#include<stdlib.h>

#define swap(type, x, y) do{type tmp = x; x = y; y = tmp;}while(0)

void downheap(int [], int, int);
void heapsort(int [], int);

#endif
