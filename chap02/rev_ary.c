#include<rev_ary.h>

void ary_reverse(int a[], int n)
{
  int i;
  for(i = 0; i < n/2; i++)
    swap(int, a[i], a[n-i-1]);
}

int main(void)
{
  int i, nx;
  int *x;

  printf("요소 개수: ");
  scanf("%d", &nx);
  x = malloc(sizeof(int)*nx);
  printf("%d개의 정수를 입력하세요.\n", nx);
  for(i = 0; i < nx; i++){
    printf("x[%d] : ", i);
    scanf("%d", &x[i]);
  }
  ary_reverse(x, nx);
  puts("배열의 요소를 역순을 정렬했습니다");
  for(i = 0; i < nx; i++)
    printf("x[%d] = %d\n", i, x[i]);

  return 0;
}
