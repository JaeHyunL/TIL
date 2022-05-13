# WEB2 JAVASCRIPT

> 생활코딩 WEB2 JAVASCRIPT 강의를 보고 필요한 내용을 초 간단하게 정리 함.
> 

### 1강.

인터넷 브라우저가 생성 됐을 때 HTML만 존재하였다 ( 정적 ) 이것을 동적으로 생성하기 위해 만들기 위한 언어가 JavaScript

Html 위에 JavaScript를 올려 사용 함.

### 2강 .

html 태그 분석

<body/>를 컨트롤하기 위해 document.querySelect(’body’)  구문을 사용 

 document.querySelect(’body’).style.backgroundColor=’black’; Css를  통해 백그라운드 컬러를 조정 

### 3강.

<script /> 태그를 통해 자바스크립트 문법을 수행 함.

<scipt /> 태그 안에 있는 구문에 대하여 동적으로 수행함 ex) 1 + 1 

### 4강.

OnClick을 통한 alert 메세지를 띄운다. (이벤트 핸들링)

Event리스너에 종류는 다양한지만 대표적으로

onClick, onChange 를 소개함 .

### 5강.

자바스크립트를 실행하는 Console 창 사용 방법.

간단하게 코드를 입력하여 웹 브라우저 상에서 처리하는 방법을 설명 함 .

### 6강.

자바스크립트 데이터 타입

모질라 재단에서 제공하는 내용에 따르면 Boolean, Null, Undefiend, Number, String, Symbol 이 존재한다고 함 

String 문법에 여러가지 내장 함수를 사용 하는 방법을 알아 봄

### 7강.

변수와 대입 연산자. 

변수에 대입하는 규칙을 살펴 보고 변수를 통해 간단하게 문자열을 제어하는 방법을 배움 .

### 8강.

웹 브라우저 제어.  Style, JS 를 활용 

### 9강.

CSS 문법을 통해 스타일을 설정 함 

### 10강 & 11강

CSS 문법 기초 . 

<div> <span> 태그 줄바꿈을 사용하지 않는다.

<style>태그를 활용 하여 class 값을 통하여 전역으로 스타일을 적용하는 방법을 살펴 봄 .

.은 클래스 #은 아이디를 의미 함 . 

ID 와 Class 사이에 우선 순위는 ID 가 우선임 Class 가 좀더 그룹 적인 의미로 사용하기에.

### 12강.

예제 웹 사이트에 클론 코딩 하는 방법을 설명 함.

### 13강.

HTML 가 프로그래밍 언어가 아닌 이유. 

프로그램은 순서라는 의미가 중요하게 자리 잡혀 있음 . 

### 14강, 15강, 16강, 17강.

조건문. 을 통한 웹브라우저 상태 동적 핸들링.

비교 연산자와 블리언.  비교 연산자( === ) 로 표기함.

조건 문.

```jsx
if (조건 === true) {
} else if (조건 !== true) {
} else {
}
```

### 18강.

리팩토링 필요성 사례 등 을 살펴 보아요.

긴 구문에 중복된 구문은 하나의 변수로 사용해서 씀 . 

### 19강.

반복문 

```jsx
var links = document.querySelectorAll('a');
var i = 0;
while(i<links.length) {
	links[i].style.color='powderblue'
	j = i + 1
}
```

### 20강.

배열. Array. 배열에 문법을 대입해볼 것 이다.

```jsx
var tester = ['test', 'test1', 'test2']
tester[0] // 1번 째 인덱스 eaㄷㄷㄷㄷaeffeff
```

### 21강. 22강, 23강

배열 loop  Script 

배열 LOOP 와 While 배열을 이용한 while 구문을 살 펴 봄 .

### 24강.

함수가 불행으로 부터 탈출 시켜주는 이유!

함수는 수납장. 지저분한 것을 차곡차곡 담아 줌

### 25강.

함수 = function = method 

함수 선언 방식을 살펴 봄 

### 26강.

매개변수 =아규먼트 = 파라미터 인자 입력 방식  self활용 방식 

### 27강.

간단한 함수 리턴  

### 28강 (살짝 중요).

함수를 활용환 코드 리팩터링  this를 활용했을 때 함수로 넣었을 때 처리 방법  this + self 활용 

### 29강

객체 Object의 사용 법 객채 obect.method 사용 방법 

### 30강

객체를 생성하고 object에 정보를 읽고 대입하는 방식을 알아 봄   

### 31강

객체의 obecjt에 반복문으로 접근하여 객체에서 데이터를 뽑아내는 방법 

```jsx
var coworkers = {
 "programmer": "egoing",
 "designer": "leezche",
}
for (var key in coworkers) {
	document.write(coworkers[key] + '<br>');
}
```

### 32강

객체의 함수 정의 하는 방법 

```jsx
coworker.showAll = fucntion() {
	for (~~~) {
		this ~~~
	}
} 
```

### 33강

객체를 활용한 코드 리팩터리 방식을 살펴봄 

### 34강

리팩토링 방식 :) 하나의 파일이 아닌 여러개의 컴퍼넌트로 분리하여 파일을 임포트하여 사용하는 방법을 아라봄 ; 코드의 재사용성 유지보수성 증 대  

### 35강

라이브러리와 프레임 웤 을 살펴보고 그 중 JQuery를 살펴 봄 

### 36강

유저 인터패이스와 어플리케이션 인터페이스를 구분하는 법을 살펴 봄 

### 37강

웹사이트 검색 키워드 추천