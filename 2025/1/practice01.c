#include <stdio.h>

int main()
{
  // 変数の宣言と初期化
  int age = 25;
  float pi = 3.14;

  // 制御構造

  // if文
  int num = 10;

  if (num > 5)
  {
    printf("numは5より大きい\n");
  }
  else
  {
    printf("numは5以下\n");
  }

  // for文
  for (int i = 0; i < 5; i++)
  {
    printf("iの値: %d\n", i);
  }

  // while文
  int count = 0;
  while (count < 3)
  {
    printf("count: %d\n", count);
    count++;
  }

  // switch文
  char grade = 'B';

  switch (grade)
  {
  case 'A':
    printf("素晴らしい！\n");
    break;
  case 'B':
    printf("良い成績！\n");
    break;
  default:
    printf("もっと頑張ろう！\n");
  }

  // 配列
  int numbers[5] = {1, 2, 3, 4, 5};
  printf("numbers[1]: %d\n", numbers[1]);

  // 文字列
  char name[] = "Alice";
  printf("name: %s\n", name);
}