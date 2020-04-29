#include <stdio.h>

int main(void)
{
  int no;
  printf("Insert a two-digit number");

  do{
    printf("no : ");
    scanf("%d", &no);
  }while(no < 10 || no > 99);
  printf("no is %d.\n", no);

  return 0;
}
