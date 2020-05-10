#ifndef __DAY_OF_YEAR__
#define __DAY_OF_YEAR__

#include<stdio.h>

const int mdays[][12] = {
  {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
  {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
};

int isleap(int);
int dayofyear(int, int, int);

#endif
