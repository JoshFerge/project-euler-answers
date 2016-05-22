#include <stdio.h>


int main() {
  int last = 1;
  int i = 1;
  int cap = 0;
  int sum = 0;
  while (i+last < 4000000) {
    cap = i;
    i = i+last;
    last = cap;
    // printf("%d\n",i );

    if (i % 2 == 0) {
      sum+=i;
    }
  }
  printf("%d\n",sum );

  return 0;
}