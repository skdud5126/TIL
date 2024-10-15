from django.shortcuts import render

# Create your views here.
# view 함수의 첫번째 인자가 항상 request인 이유?
# 그 view 함수를 호출할때, 첫번째 인자를 무조건 넣어주기 때문이다.
def hello(request):
    # print(dir(request))
    '''
        함수 : input에 대한 output 반환
        인터넷 서비스 : 특정 경로로 요청이 들어오면 html 문서를 반환
    '''
    # template name -> template path
    # html 파일 이름 x -> HTML 파일 위치!!!!
    return render(request, 'hello.html')