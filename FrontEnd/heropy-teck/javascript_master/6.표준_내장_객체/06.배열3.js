// .join()
// 대상 배열의 모든 요소를 '구분자'로 연결한 '문자'를 반환합니다.

const arr = ['A', 'B', 'C']
console.log(arr.join())        // A,B,C
console.log(arr.join(', '))    // A, B, C
console.log(arr.join(''))      // ABC
console.log(arr.join('-'))     // A-B-C



// .map()
// 대상 배열의 길이만큼(반복) 주어진 콜백을 실행하고, '콜백의 반환 값을 모아 새로운 배열'을 반환합니다.
// 대상 배열을 개조(콜백 조건)하여 새로운 배열(같은 길이) 만들기

const numbers = [1, 2, 3, 4, 5]
const doubled = numbers.map(item => item * 2)
console.log(doubled)

const users = [
  { name: 'Neo', age: 85 },
  { name: 'Amy', age: 22 },
  { name: 'Lewis', age: 11 }
]
const newUsers = users.map(user => {
  return {
    ...user,
    isValid: true,
    email: null
  }
})
console.log(newUsers)



// .pop()
// 대상에서 마지막 요소를 제거하고 그 요소를 반환합니다.
// 대상 배열의 원본이 변경됩니다.

const fruits = ['Apple', 'Banana', 'Cherry']
console.log(fruits.pop())
console.log(fruits)


// .push()
// 대상 배열의 마지막에 하나 이상의 요소를 추가하고, 배열의 새로운 길이를 반환합니다.
// 대상 배열 원본이 변경됩니다.

const fruits2 = ['Apple', 'Banana', 'Cherry']
console.log(fruits2.push('Orange', 'Kiwi'))
console.log(fruits2)
