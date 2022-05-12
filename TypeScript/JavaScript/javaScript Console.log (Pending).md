# javaScript Console.log (Pending)

### console.log를 찍었을 때 {Pending} 상태로 찍히는 경우가 있다.

해당 원인은  비동기 처리 async/await 구문 사용시 반환하기 전보다 console.log가 더 빠르게 찍혀서 그렇다.

해당 상태를 수정하기 위하여  JavaScript는 Priomise 상태 매서드를 지원해 주고 있다. 

또 다른 방법으로 

then 함수를 입력받아 파라미터를 전달 받고 그 후에 데이터를 처리하면 된다.