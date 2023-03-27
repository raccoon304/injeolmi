from django.db import models

class Bookmark(models.Model):
    
    title = models.CharField('TITLE', max_length=100, blank=True)
    #URLFild() 필드 클래스의 첫 번째 파라미터인 'URL'문구는 url 칼럼에 대한 별칭임.
    url = models.URLField('URL', unique=True)
    
    # __str__함수는 객체를 문자열로 표현할 때 사용하는 함수
    def __str__(self):
        return self.title
