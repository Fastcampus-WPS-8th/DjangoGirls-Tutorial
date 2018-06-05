from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-id')
    context = {
        'posts': posts,
    }
    # render는 주어진 인수를 사용해서
    #  1번째 인수: HttpRequest인스턴스
    #  2번째 인수: 문자열 (TEMPLATE['DIRS']를 기준으로 탐색할 템플릿 파일의 경로)
    #  3번째 인수: 템플릿을 렌더링할때 사용할 객체 모음
    # return render(request, 'blog/post_list.html', context)
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context,
    )


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
    }
    # post_detail view function이 올바르게 동작하는 html을 작성해서 결과 보기
    # 1. blog/post_detail.html
    return render(request, 'blog/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        # request의 method값이 'POST'일 경우 (POST method로 요청이 왔을 경우)
        # request.POST에 있는 title, text값과
        # request.user에 있는 User인스턴스(로그인한 유저)속성을 사용해서
        # 새 Post인스턴스를 생성
        # HttpResponse를 사용해 새로 생성된 인스턴스의 id, title, text정보를 출력 (string)
        post = Post.objects.create(
            author=request.user,
            title=request.POST['title'],
            text=request.POST['text'],
        )
        # HTTP Redirection을 보낼 URL
        #  http://localhost:8000/
        #  / 로 시작하면 절대경로, 절대경로의 시작은 도메인 (http://localhost:8000)
        return redirect('post-list')
    else:
        return render(request, 'blog/post_create.html')


def post_delete(request, post_id):
    # 1. 연결되는 URL
    #   ex1) localhost:8000/3/delete/
    #   ex2) localhost:8000/35/delete/
    # 2. 템플릿을 사용하지 않음 (render하는 경우가 없음)

    # view function의 동작
    # 1. 오로지 request.method가 'POST'일 때만 동작
    #    (request.method가 'GET'일 때는 아무 동작도 안 해도 됨
    # 2. request.method가 'POST'일때의 동작
    #   post_id에 해당하는 Post인스턴스에서
    #   delete()를 호출해서 DB에서 삭제
    #   이후 post-list(url name)로 redirect

    # post_list.html템플릿에서
    #  for문을 순회하는 각 요소마다 form을 하나씩 추가
    #  action은 post_delete() view function으로 연결되는 url
    #    -> url태그를 사용한다, post_list.html에서 post_detail()로 연결하는 url생성법 참조
    #  method는 POST
    #  내부에 있어야 할 input요소는 없음, 버튼하나만 존재 (삭제)
    #  POST요청이므로 csrf_token태그를 각 form안에 사용할 것

    # 실제 동작: post_list.html의 각 요소에 생성된 버튼을 클릭하면 이 함수가 실행되어야 함
    # breakpoint를 아래 리턴에 걸어놓은 후 request내의 내용을 확인
    return HttpResponse('post_delete view function')
