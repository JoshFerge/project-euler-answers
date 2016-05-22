#include <stdio.h>

int main() {
  FILE *fp;
  char buff[1024];
  fp = fopen("p022_names.txt","r+");
  fscanf(fp,"%s",buff);

  return 0;
}