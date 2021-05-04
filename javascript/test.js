// ２つの正の整数 a, b が半角スペース区切りで入力されるので a と b を足した数を出力してください。
// ※「掛け算」の問題では入力が改行区切りで与えられましたが、今回は半角スペース区切りで与えられます。

const fs = require("fs");

const input = fs.readFileSync("/dev/stdin", "utf-8");

const [a, b] = input.split(" ").map((num) => Number(num));
console.log(a + b);