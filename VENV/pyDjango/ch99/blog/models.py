from django.db import models

# Create your models here.
from django.db import models
#reverse() 함수는 URL패턴을 만들어주는 장고의 내장함수
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    #SlugField에 unique옵션을 추가해 특정 포스트를 검색할때 기본 키 대신 사용 
    slug = models.SlugField('SLUG', unique = True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField("DESCRIPTION", max_length=100, blank=True, help_text='Simple decription text.')
    content = models.TextField('CONTENT')
    #날짜와 시간을 입력하는 DataTimeField이며, auto_now_add 속성은 객체가 생성될 때의 시각을 자동으로 기록함 
    create_dt= models.DateTimeField('CREATE DATE', auto_now_add=True)
    #컬럼은 날짜와 시간을 입력하는 DataTimeField이며 auto_now 속성은 객체가 데이터베이스에 저장될 때의 시각을 자동으로 기록
    # 즉, 객체가 변결됭 때의 시각이 기록    
    modify_dt=models.DateTimeField('MODIFY DATE',auto_now =True)
    
    #필드 속성 외에 필요한 파라미터가 있으면, Meta 내부 클래스로 정의합니다.
    class Meta:
        verdose_name = 'post'
        verdose_name_plural = 'posts'
        db_table = 'blog_posts'
        #모델 객체의 리스트 풀력시 modify_dt 칼럼을 기준으로 내림차순으로 표시 
        ordering = ('-modify_dt',)
    
    def __str__(self):
        return self.title
    #메소드가 정의된 객체를 지칭하는 URL을 반환함, 메서드 내에서는 장고 내부함수인 reverse() 호출
    def get_absolute_url(self): 
        return reverse('blog:post_detail', args=(self.slug,))
    #최신 포스트를 먼저 보여주고 있으므로get_previous_by_modify_dt()함수는 modify_dt컬럼을 기준으로 최신포스트 반환
    def get_orevious(self):    
        return self.get_previous_by_modify_dt()
    def get_next(self):
        return self.get_next_by_modify_dt()
    
        