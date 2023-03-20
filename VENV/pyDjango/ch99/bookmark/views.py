from django.shortcuts import render
#클래스형 제네릭 뷰를 사용하기 위한 클래스 import 
from django.views.generic import ListView, DetailView
#테이블 조회를 위한 모델 클래스 import 
from bookmark.models import Bookmark

#Bookmark 테이블의 레코드 리스트를 보여주기 위한 뷰 
#ListView를 상속 받는경우는 객체가 들어있는 리스트를 구성해 이를 컨텍스트 변수로 템플릿 시스템에 넘겨주면 됨 

#장고의 경우 컨텍스트 변수로 object_list , 템플릿 파일명을 모델명소문자_list.html 형식은 명시적으로 지정하지 않아도 장고가 디폴트로 알아서 지정 해줌 
class BookmarkLV(ListView):
    model = Bookmark 

#Bookmark 테이블의 특정 레코드에 대한 살세 정보를 부여주기 위한 뷰 
#DetailView를 상속받는 경우 특정 객체 하나를 컨텍스트 변수에 담아서 템플릿 시스템에 넘겨주면 됨 
#장고의 경우 컨텍스트 변수로 object , 템플릿 파일명을 모델명소문자_detail.html 형식은 명시적으로 지정하지 않아도 장고가 디폴트로 알아서 지정 해줌 
class BookmarkDV(DetailView):
    model = Bookmark
