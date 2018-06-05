from django.conf.urls import url

# from blog.views import post_list
from .views import post_list, post_detail


urlpatterns = [
    # url의 첫 번째 인자: 매치될 URL정규표현식
    # url의 두 번째 인자: view function
    #   view function
    #    -> request를 받아서 response를 돌려주는 함수

    # blog.views에 있는 post_list함수를
    # 아래 url함수의 두 번째 인자로 전달
    #  (함수호출 아님)
    url(r'^$', post_list, name='post-list'),
    # ex1) 3/
    # ex2) 235/
    # 정규표현식에 그룹을 지정해서 view function의
    #  인수로 전달한다
    url(r'^(\d+)/', post_detail, name='post-detail'),
]
