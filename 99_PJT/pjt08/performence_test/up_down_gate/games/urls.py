from . import views
from django.urls import path

urlpatterns = [
    # 1. 게임 화면 출력
    path('start/', views.start_game, name='start_game'),
    # 2. 정답을 체크할 수 있는 URL
    path('make_guess/<int:game_session_id>/', views.make_guess, name='make_guess')
]
