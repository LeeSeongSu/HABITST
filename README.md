## [LIKELION_HACKATHON] 취미 공유 사이트

- ### Main

![main](C:\Users\oplm1\OneDrive\바탕 화면\GIT파일\habitst\main-1616051176147.PNG)

- ####  설명

> - 작성자
> - 작성일
> - 제목/내용/이미지/글
> - 조회수/좋아요수

------



- ### write

![write](C:\Users\oplm1\OneDrive\바탕 화면\GIT파일\habitst\write.PNG)

- #### 설명

> - Summernote 기능 적용

------



- ### meeting

![shop](C:\Users\oplm1\OneDrive\바탕 화면\GIT파일\habitst\shop.PNG)

- #### 설명

> - 작성자
> - 작성일
> - 제목/내용/이미지/글
> - 조회수/좋아요수

------



- ### meetingDetail1

![shop_detail](C:\Users\oplm1\OneDrive\바탕 화면\GIT파일\habitst\shop_detail.PNG)

- #### 설명

> - 모임을 주최한 사람 정보
> - 모임 장소 & 시간
> - 모임에 대한 소개
> - 기타 내용
> - 사진첨부

------



- ### meetingDetail2

![shop_detail2](C:\Users\oplm1\OneDrive\바탕 화면\GIT파일\habitst\shop_detail2.PNG)

- #### 설명

> - 모임을 주최한 사람 정보
> - 모임 장소 & 시간
> - 모임에 대한 소개
> - 기타 내용
> - 사진첨부

------



- ### payment

![payment](C:\Users\oplm1\OneDrive\바탕 화면\GIT파일\habitst\payment.PNG)

- #### 설명

> - Iamport 사용(결제 api)

------



- ### mypage

![mypage](C:\Users\oplm1\OneDrive\바탕 화면\GIT파일\habitst\mypage.PNG)

- #### 설명

> - 개인정보(회원 가입할 때 기입한 것)
> - 내가 쓴 글
> - 자기소개 페이지 - 왼쪽 상단에 자기 프로필 사진이랑 사진 밑에 간단한 자기소개 보여지기.
> - 결제내역

------



- ### chat

![chat](C:\Users\oplm1\OneDrive\바탕 화면\GIT파일\habitst\chat.PNG)

- #### 설명

> - Iamport 사용(결제 api)
> - redis-server 적용(채팅)

------



- ### hobby

![hobby](C:\Users\oplm1\OneDrive\바탕 화면\GIT파일\habitst\hobby.PNG)

- #### 설명

> - 취미테스트 및 SNS 공유

------



#### 실행방법

- redis설치 및 (필수)
- pip install django-allauth
- pip install django-crispy-forms
- pip install django-summernote
- pip install iamport-rest-client
- pip install django_social_share
- python -m pip install -U channels
- pip install channels_redis
- python -m pip install Pillow
- python manage.py runserver
- runserver시 no module에 관한 부분은 pip install django_xxxxxx형태로 설치

[]: https://www.youtube.com/watch?v=Vm178O1kYVI	"동영상 링크"