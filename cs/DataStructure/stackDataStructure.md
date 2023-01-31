# 4장 스택과 큐

스택은 데이터를 일시적으로 쌓아 놓는 자료구조로, 데이터의 입력과 출력순서는 후입 선출 LIFO 

```java
public class IntStack {
    private int[] stk; // 스택용 배열
    private int capacity; // 스택 용량
    private int ptr; // 스택 포인트

    // 스택이 비어있을경우 Exception
    public class EmptyIntStackException extends RuntimesException { 
        public **EmptyIntStackException**() { }
    };

    public class OverflowIntStackException extends RuntimesException { 
        public OverflowIntStackException() { }
    };

    public IntStack(int maxlen) { 
        ptr = 0;
        capacity = maxlen;
        try {
            stk = new int[capacity];
        } catch (OutOfMemoryError e) { 
            capacity = 0;
        }
    }

    // 스택에 X를 푸시
    public int push(int x) throws OverflowIntStackException { 
        if (ptr >= capacity) 
            throw new OverflowIntStackException();
        return stk[ptr++] = x;
    }

    // =스택의 맨 위 값을 추출.
    public int pop() throws EmptyIntStackException { 
        if (ptr <= 0)
            throw new EmptyIntStackException();
        return stk[--ptr];
    }

    // 스택에서 데이터를 피크(꼭대기에 있는 데이터를 들여다봄)
    public int peek() throws EmptyIntStackException {
        if (ptr <= 0)
            throw new EmptyIntStackException();
        return stk[ptr-1];
    }
    
    public static int clear() { 
        ptr = 0;
    }

    public int indexOf(int x) { 
        for (int i = ptr - 1; i >= 0; i--) {
            if (stk[i] == x)
            return i
        }
        return -1;
    }

    public int getCapacity() {
        return capacity;
    }
}
```

### 검색 메서드 indexOf

스택 본체의 배열 stk에 x와 같은 값의 데이터가 포함되어 있는지 포함되어 있다면 배열의 어디에 들어가있는지를 조사하는 메서드 임.\