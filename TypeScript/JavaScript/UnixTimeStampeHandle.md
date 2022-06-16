# 자바 스크립트 유닉스 타임스탬프 핸들링

Unix Time Stampe 19700101 기준으로 서버 시간이 설정 됨

Unix Time Stamp -> Date Time

```javascript
let unix_timeStamp = 1655382467
var date = new Date(unix_timeStamp * 1000)
date 
"2022-06-16T12:27:47.000Z"
```



Date Time -> Unix Time Stamp

```
today = new Date("2022.06.16")
Math.floor(today.getTime() / 1000)
today.getTime() / 1000
```

