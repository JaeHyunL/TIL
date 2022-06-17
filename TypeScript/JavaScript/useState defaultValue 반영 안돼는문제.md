# UseState DefaultValue 반영 불가 현상.

useState로 데이터 값을 변경 시킬 때 Input 박스 안에 defaultValue가 실시간으로 변경이 안돼는 현상 발견

```JavaScript
const [remState, setRemState] = useState("test")

setRemState("test2")

<Input
    prefix={<UserOutlined className="site-form-item-icon" />}
    placeholder="Username"
    defaultValue={remState}
/>

```

해당 태그에서 remState가 고정 되어있어 key 값을 추가하면 해결 가능하다

```JavaScript
const [remState, setRemState] = useState("test")

setRemState("test2")

<Input
    prefix={<UserOutlined className="site-form-item-icon" />}
    placeholder="Username"
    key={remState}
    defaultValue={remState}
  />

```

