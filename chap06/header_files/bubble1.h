#ifndef __BUBBLE1__
#define __BUBBLE1__

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define swap(type, x, y) do{type t = x; x = y; y = t; }while(0)

void bubble(int [], int);
void bubble2(int [], int);
void bubble3(int [], int);

void copy(int [], int [], int);

#endif
