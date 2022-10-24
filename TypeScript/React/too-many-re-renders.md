# **Error: Too many re-renders. React limits the number of renders to prevent an infinite loop.**

**Error: Too many re-renders. React limits the number of renders to prevent an infinite loop. 버그 해결** 

로직상으로 State 값이 계속 변경 됨

1) 루프 걸린 부분을 풀어준다

2) UseEffect를 사용하여 State 변경을 제어한다.