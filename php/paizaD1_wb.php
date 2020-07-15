<?php
// fgets
// ()で指定したファイルポインタから1行取得する関数

// STDIN
// 標準入力（standard input）を意味する定数

$i = 0;

while ($i == 3) {
  $array[] = trim(fgets(STDIN));
  $i += 1;
};
echo "$array[0]\n";
echo "$array[1]\n";
echo $array[2];
?>