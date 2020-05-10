#ifndef __PHYSICAL__
#define __PHYSICAL__

#include<stdio.h>

#define VMAX 21

typedef struct{
  char name[20];
  int height;
  double vision;
}PhysCheck;

double ave_height(const PhysCheck[], int);
void dist_vision(const PhysCheck[], int, int[]);

#endif
