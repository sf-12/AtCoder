// inputに入力データ全体が入る
function Main(input) {
  // 1行目がinput[0], 2行目がinput[1], …に入る
  input = input.split("\n");
  xRange = input[0].split(" ");
  yRange = input[1].split(" ");

  // 演算
  let arr = [];
  arr.push(xRange[0] - yRange[0]);
  arr.push(xRange[0] - yRange[1]);
  arr.push(xRange[1] - yRange[0]);
  arr.push(xRange[1] - yRange[1]);

  // 出力
  console.log(Math.max(...arr));

}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
