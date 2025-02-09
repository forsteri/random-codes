#include <stdio.h>

int main()
{
  int num = 10;    // 変数
  int *ptr = &num; // ポインタ変数（numのアドレスを指す）

  printf("numの値: %d\n", num);
  printf("numのアドレス: %p\n", &num);
  printf("ptrの値: %p\n", ptr);
  printf("ptrが指す値: %d\n", *ptr);

    return 0;
}