# Send mail in Python
## 1. 제작배경
크롤러를 사용해 데이터를 수집을 할 때 시간이 오래걸린다. 그래서 중간에 Error가 나오거나, 데이터 수집이 끝이 나도 바로 확인하기 쉽지 않다. 이런 이벤트가 발생했을 때 메일로 상황을 전송을 해주면 바로 대처를 해줄 수 있기 때문에 만들게 되었다.

## 2. 사용방법
보낼 메일의 id와 password(pw) 정보가 들어 있는 password.py 파일을 만든 다음 send_mail.py 와 같은 경로에 저장한 후 사용하면 된다.

```python
# password.py 형식
def main_info():
    config = {
        'id' : '사용자의 ID',
        'pw' : 'ID의 password'
    }

    return config
```

## 3. 보낼 메일의 id와 pw 생성방법
SMTP 방식으로 메일을 보낼 수 있는 메일을 사용해야한다. 개인적으로는 g-mail을 추천한다.
pw는 일반적으로 메일에 입력하는 pw가 아닌 메일에서 발급받은 pw를 사용해야한다. pw를 발급받는 방법에 대해서 자세하게 알아보기 위해서는 [여기](https://yeolco.tistory.com/93)를 클릭해주세요.