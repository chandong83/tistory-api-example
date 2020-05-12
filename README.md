# 티스토리 블로그 API 파이썬 예제


티스토리 블로그 API 사용 예제 - 파이썬

https://tistory.github.io/document-tistory-apis 링크 글을 기준으로 작성되었습니다.


[테스트 버전]<br>
    
    파이선 : 3.7.6
    beautifulsoup4 : 4.9.0
    lxml : 4.5.0
    requests : 2.23.0

[필요 패키지 설치]<br>

    $ pip install beautifulsoup4
    $ pip install lxml
    $ pip install requests

[먼저 진행해야하는 것]<br>

    먼저 개발자 API 등록 및 토큰을 얻는 과정은 https://limsee.com/325 참조
    위의 링크에서 얻은 토큰과 App ID는 app_config.py  에 추가.
      access_token='---------------'
      app_id = '-----------'
    
    example.py에 main 함수를 확인

