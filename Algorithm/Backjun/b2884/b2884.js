// 알람 시계
// https://www.acmicpc.net/problem/2884

const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');
const inputVal = inputData[0].split(' ').map(Number);

main(inputVal);

function main(inputVal) {
  let h = inputVal[0];
  let m = inputVal[1];

  if (m >= 45) {
    m = m-45;
  }
  else {
    m = 60-(45-m);
    if (h == 0) {
      h = 23;
    }
    else h = h-1;
  }

  console.log(h + " " + m);
}

