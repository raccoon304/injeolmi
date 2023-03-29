from django.contrib import admin
from django.urls import path,include

#URLconf 뷰를 호출하므로 뷰 모듈의 관련 클래스를 임포트함
#from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [    
    path('admin/',admin.site.urls),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    #path('bookmark/',BookmarkLV.as_view(),name='index'),
    #path('bookmark/<int:pk>/',BookmarkDV.as_view(),name='detail'),

]
