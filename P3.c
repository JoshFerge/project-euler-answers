#include <stdio.h>


int main() {
  int j;
  int i = 20;
  int not_divis_by_nums = 0;
  int isGood;

  while (!not_divis_by_nums) {
    isGood = 1;
    // printf("%d\n",i);
    for (j = 11; j <= 20; j++) {
      if (i % j != 0) {
        isGood = 0;
      }
    }

    if (isGood) {
      not_divis_by_nums = 1;
      printf("%d\n",i);
    }

    i+=2;
  }


  return 0;
}