## Caesar cipher(시저 암호)
Caesar cipher는 알파벳을 n번 만큼 이동하여 암호화하는 방식입니다.  이동할 거리인 n을 key라고 부르기도 합니다.  음수도 가능하지만 일반적으로는 양수만 사용합니다.  
예를 들어, key=3인 경우 다음과 같이 이동합니다.   
A → D, B → E, C → F, D → G, ... , Y → B, Z → C   
Caesar cipher는 단순한 암호화 방식이므로 보안적 유용성이 낮습니다.  
하지만 간단하게 구현할 수 있으며, 암호화가 필요한 문장이나 단어를 쉽게 암호화할 수 있는 장점이 있습니다.

## 예시
다음은 "HELLO WORLD"를 key=5로 암호화하는 예제입니다.

```python  
txt = "HELLO WORLD"  
key = 5

result = ""  
for char in txt:  
    if char.isalpha():  
        if char.isupper():  
            result += chr((ord(char) - 65 + key) % 26 + 65)  
        else:  
            result += chr((ord(char) - 97 + key) % 26 + 97)  
    else:  
        result += char  

print(result) # MJQQT BTWQI
```
