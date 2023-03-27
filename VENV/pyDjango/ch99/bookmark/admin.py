from django.contrib import admin
from bookmark.models import Bookmark

#해당 데코레이터를 통해 어드민 사이트에 등록
#admin.site.register(Bookmark, BookmarkAdmin) 으로 사용해도 무관
@admin.register(Bookmark)
#BookmarkAdmin 클래스는 Bookmark 클래스가 Admin 사이트에서 어떤모습으로 보여줄지를 정의하는 클래스
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')
    
    


