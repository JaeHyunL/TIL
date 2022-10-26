# 03-1 검색 알고리즘이란?

이 장에서는 데이터 집합에서 원하는 값을 가진 요소를 찾아내는 검색알고리즘을 아라보자

- 선형 검색: 무작위로 늘어서 있는 데이터 모임에서 검색을 수행함
- 이진 검색: 일정한 규칙으로 늘어서 있는 데이터 모임에서 아주 빠른 검색을 수행
- 해시법: 추가, 삭제가 자주 일어나는 데이터 모임에서 아주 빠른 검색을 수행
    - 체인법: 같은 해시값의 데이터를 선형 리스트로 연결 하는 방법
    - 오픈 주소법: 데이터를 위한 해시값이 충돌할 때 재해시하는 방법

```java
선형 조회 벼열의 요솟수를 판단하는 횟수는 평균 n/2 회 임.

int i = 0;
while (true) {
	if (i == n)  
		return -1;
	if (a[i] == key) 
		return i;
	i++
}
```

### 보초법으로 선형 검색 구현하기

선형 검색은 반복할 때마다 다음의 종료조건 1과 2를 모두 판단합니다. 단순한 판단할 수 있지만 티종료조건을 검사하는 비용은 결코 무시할 수 없음 

### 03-3 이진 검색(binary search)

이진 검색법은 알고리즘을 적용하는 저체 조건은 데이터가 키값으로 이미 정렬 되어 있다는 것 임, 이진검색은 선형 검색보다 좀 더 빠르게 검색할 수 있다는 장점이 있음 .

이진검색은 요소가 오름차순 또는 내림차순으로 정렬된 배열에서 검색하는 알고리즘임 

중간 값을 찾고 폭을 줄여나가는 방식임 

장점 검색할때 평균 비용은 log n 이며 최악의 경우 log(n+1)

### 복잡도 구하기

프로그램의 실행속도는 프로그램이 동자갛는 하드웨어나 컴파일러 등의 조건에 따라 달라짐

성능을 객관적으로 평가하는 기준을 복잡도라고 합니다.

복잡도는 다음 두 가지 요소를 가지고 있음

- 시간 복잡도: 실행에 필요한 시간을 평가한 것
- 공간 복잡도: 기억 영역과 파일 공간이 얼마나 필요한가를 평가하는 것

2장에서 배운 소수를 나열하는 프로그램 버전 1, 2, 3 은 알고리즘을 선택할 때 두 복잡도를 생각ㅎ ㅏㄹ 필요가 있음 

```java
// Q1
import java.util.Scanner;

class Today2 {

    static int seqSearchSen(int[] a, int n, int key) {
        a[n] = key;

        for (int i =0; i< a.length; i++) { 
            if (a[i] == key)
                return a[i];
        }
        return a[key];
    }
    public static void main(String[] args) { 
        Scanner stdIn = new Scanner(System.in);   
        int num = stdIn.nextInt( );
        int[] x = new int [num +1]; 

        for (int i = 0; i < num; i++) {
            x[i] = stdIn.nextInt( );
        }
        int ky = stdIn.nextInt( );
        int idx = seqSearchSen(x, num, ky);

        if (idx == -1)
            System.out.println("그런 요소가 없음");
        else
            System.out.println("그 값은 x["+ idx + "]에 있습니다.");
    }
}

```

```python
//Q2  위 소스코드 + print
```

```java
//Q3 int[] 배열 형변한 너 무 귀찮음 ;

import java.util.ArrayList;

class Today3 {

    static ArrayList<Integer> searchIdx(int[] a, int n, int key, int[] idx) { 
        ArrayList<Integer> newList = new ArrayList<Integer>();
        for( int i=0; i<a.length; i++ ) { 
            if (a[i] == key) {
                newList.add(i);
            }
        }
        return newList;

    }
    public static void main(String[] args) {
        int[] idx = {};
        int[] input = { 1 , 9, 2, 9, 4, 7, 8, 9};
        System.out.println(searchIdx(input, 8, 9, idx ));
    }
}
```

```java
//Q4 단순 이진 검색문에 프린트.
```

```java
//Q5 
class Today3 {

    static int binSearch(int[] a, int n, int key) { 
        int pl = 0;
        int pr = n- 1;
        do {
            int pc = (pl + pr) / 2; //center
            if (a[pc] == key) { 
                int x = pc;
                while ( a[x] == key) {
                    x--;
                }
                return x+1; // locaiton index 
            }
            else if (a[pc] < key) { 
                pl = pc + 1;
            } else { 
                pr = pc -1;
            } 

        } while (pl <= pr);
       
        return -1;
    }
    public static void main(String[] args) {
        int[] idx = {};
        int[] input = { 1, 3, 5, 7, 7, 7, 8, 8, 9, 9};
        System.out.println(binSearch(input, input.length, 7));
    }
}
```

```java
// Q6 실습 3-5 idx 요소가없음 proint
```

```java
// Q7  실습 3-8 height -->  vision 변수 변경
```